import builtins
import optprompt
import os


inputs = []


def fake_input(prompt_string):
    return inputs.pop()


builtins.input = fake_input


def test_basic():
    parser = optprompt.OptionPrompter()
    parser.add_argument('-n', '--name')
    opts = parser.parse_args(['--name', 'Bob'])
    assert opts.name == 'Bob'


def test_config_file(tmpdir):
    with open(os.path.join(tmpdir, 'test.conf'), 'w') as f:
        f.write('[defaults]\nname = "James"')
    parser = optprompt.OptionPrompter(config_files=[os.path.join(tmpdir, 'test.conf')])
    parser.add_argument('-n', '--name')
    opts = parser.parse_args([])
    assert opts.name == 'James'

def test_config_file_non_default(tmpdir):
    with open(os.path.join(tmpdir, 'test.conf'), 'w') as f:
        f.write('[defaults]\nname = "James"')
    parser = optprompt.OptionPrompter(config_files=[os.path.join(tmpdir, 'test.conf')])
    parser.add_argument('-n', '--name', default='Bob')
    opts = parser.parse_args([])
    assert opts.name == 'James'


def test_prompt():
    parser = optprompt.OptionPrompter()
    parser.add_argument('-n', '--name', prompt='What is your name')
    inputs.append('Alice')
    opts = parser.parse_args([])
    assert opts.name == 'Alice'


def test_default():
    parser = optprompt.OptionPrompter()
    parser.add_argument('-n', '--name', default='Janet')
    inputs.append('')
    opts = parser.parse_args([])
    assert opts.name == 'Janet'
