import argparse
import toml


class OptionPrompterError(Exception):
    pass


class OptionPrompter():

    def __init__(self, *args, config_files=None, section_header='defaults', **kwargs):
        self.opts = list()
        self.config_files = list()
        self.config_opts = list()
        self.argparser = argparse.ArgumentParser(*args, **kwargs)
        if config_files:
            for config_file in config_files:
                self.config_files.append(config_file)
        self.section_header = section_header

    def add_config_option(self, opt_string, help=None):
        opt = self.argparser.add_argument(self, opt_string, action='store', help=help)
        self.config_opts.append(opt)

    def add_argument(self, *args, prompt=None, opt_default=None, **kwargs):
        opt = self.argparser.add_argument(*args, **kwargs)
        opt.prompt = prompt
        if opt_default is not None and opt.prompt is None:
            opt.default = opt_default
        opt.opt_default = opt_default
        self.opts.append(opt)

    def parse_args(self, *args, **kwargs):
        opts = self.argparser.parse_args(*args, **kwargs)
        self.parse_configs(opts)
        self.parse_prompt(opts)
        return opts

    def parse_configs(self, opts):
        if not self.config_files:
            return
        fileconf = toml.load(self.config_files)[self.section_header]
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
                if callable(opt.prompt):
                    opt.prompt = opt.prompt(opts)
                    if getattr(opts, opt.dest) is not None:
                        continue
                setattr(opts, opt.dest,
                        input(f'{opt.prompt} {f"[{opt.opt_default}]" if opt.opt_default is not None else ""}: '))
                if getattr(opts, opt.dest) == '':
                    setattr(opts, opt.dest, opt.opt_default)
