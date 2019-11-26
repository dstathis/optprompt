# Optprompt
A prompting option parser

## Example

```python
import optprompt

parser = optprompt.OptionPrompter(config_files=['./example.toml'])
parser.add_argument('-n', '--name', prompt='What is your name')
parser.add_argument('-r', '--race', prompt='What is your race', default='elf')
parser.add_argument('-e', '--edition')
opts = parser.parse_args()
print(opts)
```

With the config file

```
[defaults]
edition = '3.5'
```

Will produce the following output

```
(venv) [dylan@voyager examples]$ PYTHONPATH=$(pwd)/.. python example.py
What is your name : Bob
What is your race [elf]:
Namespace(edition='3.5', name='Bob', race='elf')
```
