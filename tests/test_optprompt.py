import builtins
import contextlib
import os

import optprompt


@contextlib.contextmanager
def mock_input(inputs=None):
    if inputs is None:
        inputs = []
    def fake_input(prompt_string):
        return inputs.pop()
    old_input = builtins.input
    builtins.input = fake_input
    try:
        yield inputs
    finally:
        builtins.input = old_input


def test_basic():
    with mock_input():
        parser = optprompt.OptionPrompter()
        parser.add_argument('-n', '--name')
        opts = parser.parse_args(['--name', 'Bob'])
    assert opts.name == 'Bob'


def test_config_file(tmpdir):
    with open(os.path.join(tmpdir, 'test.conf'), 'w') as f:
        f.write('[defaults]\nname = "James"')
    with mock_input():
        parser = optprompt.OptionPrompter(config_files=[os.path.join(tmpdir, 'test.conf')])
        parser.add_argument('-n', '--name')
        opts = parser.parse_args([])
    assert opts.name == 'James'


def test_config_file_non_default(tmpdir):
    with open(os.path.join(tmpdir, 'test.conf'), 'w') as f:
        f.write('[defaults]\nname = "James"')
    with mock_input():
        parser = optprompt.OptionPrompter(config_files=[os.path.join(tmpdir, 'test.conf')])
        parser.add_argument('-n', '--name', default='Bob')
        opts = parser.parse_args([])
    assert opts.name == 'James'


def test_prompt():
    with mock_input(['Alice']):
        parser = optprompt.OptionPrompter()
        parser.add_argument('-n', '--name', prompt='What is your name')
        opts = parser.parse_args([])
    assert opts.name == 'Alice'


def test_default():
    with mock_input(['']):
        parser = optprompt.OptionPrompter()
        parser.add_argument('-n', '--name', default='Janet')
        opts = parser.parse_args([])
    assert opts.name == 'Janet'
