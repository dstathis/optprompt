import optprompt
import os
import pytest


def get_classes(opts):
    if opts.edition == '3.5':
        return 'wizard or sorcerer'
    else:
        return 'wizard, sorcerer, or warlock'


def test_basic_opt():
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
