#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import argparse
import os


def _script_path():
    return os.path.dirname(os.path.realpath(__file__))


def _write_template(src, dest):
    with open(src, 'r') as fs:
        with open(dest, 'w') as fd:
            fd.write(fs.read())
            print(f'Wrote: {src} -> {dest}')


def _module_path(module_name):
    return '{}/{}'.format(os.getcwd(), module_name)


def touch_files(module_name):
    base_dir = _module_path(module_name)
    src_files = (
        ('templates', 'App.js'),
        ('templates', 'ContApp.js'),
    )
    dest_files = (
        ('components', 'App.js'),
        ('containers', f'{module_name.title()}App.js'),
    )
    for src_file, dest_file in zip(src_files, dest_files):
        src = f'{_script_path()}/{src_file[0]}/{src_file[1]}'
        dest = f'{base_dir}/{dest_file[0]}/{dest_file[1]}'
        _write_template(src, dest)


def mkreduxdir(module_name):
    base_dir = _module_path(module_name)
    os.mkdir(base_dir)
    print('Made {}'.format(base_dir))

    mod_dirs = ('actions', 'components', 'containers', 'reducers')

    for dir in mod_dirs:
        mod_dir = os.path.join(base_dir, dir)
        os.mkdir(mod_dir)
        print('Made {}'.format(mod_dir))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Make redux module directory stucture.')
    parser.add_argument('module_name', metavar='M', type=str, help='name of redux module')

    args = parser.parse_args()

    mkreduxdir(args.module_name)
    print('\n')
    touch_files(args.module_name)
