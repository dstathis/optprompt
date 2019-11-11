import argparse
import toml


class OptionPrompterError(Exception):
    pass


class OptionPrompter(argparse.ArgumentParser):

    def __init__(self, config_files=None, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.opts = list()
        self.config_files = list()
        self.config_opts = list()
        if config_files:
            for config_file in config_files:
                self.config_files.append(config_file)

    def add_config_option(self, opt_string, help=None):
        opt = super().add_argument(self, opt_string, action='store', help=help)
        self.config_opts.append(opt)

    def add_argument(self, *args, prompt=None, opt_default=None, **kwargs):
        opt = super().add_argument(*args, **kwargs)
        if opt.dest == 'help':
            return
        opt.prompt = prompt
        if opt_default is not None and opt.prompt is None:
            opt.default = opt_default
        opt.opt_default = opt_default
        if opt.opt_default is None and opt.prompt is None:
            raise OptionPrompterError('Argument must have either an opt_default or a prompt')
        self.opts.append(opt)

    def parse_args(self, *args, **kwargs):
        opts = super().parse_args(*args, **kwargs)
        self.parse_configs(opts)
        self.parse_prompt(opts)
        return opts

    def parse_configs(self, opts):
        if not self.config_files:
            return
        fileconf = toml.load(self.config_files)
        for opt in self.opts:
            fileopt = opt.dest.replace('_', '-')
            if getattr(opts, opt.dest) is None and fileopt in fileconf:
                if opt.type:
                    value = opt.type(fileconf[fileopt])
                else:
                    value = fileconf[fileopt]
                setattr(opts, opt.dest, value)

    def parse_prompt(self, opts):
        for opt in self.opts:
            while getattr(opts, opt.dest) is None:
                if opt.prompt is None:
                    setattr(opts, opt.dest, opt.opt_default)
                    break
                setattr(opts, opt.dest,
                        input(f'{opt.prompt} {f"[{opt.opt_default}]" if opt.opt_default is not None else ""}: '))
                if getattr(opts, opt.dest) == '':
                    setattr(opts, opt.dest, opt.opt_default)
