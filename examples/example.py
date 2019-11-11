import optprompt

parser = optprompt.OptionPrompter(config_files=['./example.toml'])
parser.add_argument('-n', '--name', prompt='What is your name')
parser.add_argument('-r', '--race', prompt='What is your race', opt_default='elf')
parser.add_argument('-e', '--edition')
opts = parser.parse_args()
print(opts)
