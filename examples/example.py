import optprompt


def get_classes(opts):
    if opts.edition == '3.5':
        return 'wizard or sorcerer'
    else:
        return 'wizard, sorcerer, or warlock'


parser = optprompt.OptionPrompter(config_files=['./example.toml'])
parser.add_argument('-n', '--name', prompt='What is your name')
parser.add_argument('-r', '--race', prompt='What is your race', default='elf')
parser.add_argument('-c', '--class', prompt=get_classes, default='wizard')
parser.add_argument('-e', '--edition')
opts = parser.parse_args()
print(opts)
