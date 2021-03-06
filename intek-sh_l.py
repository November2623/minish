#!/usr/bin/env python3
import os
import subprocess


def check_command(argv):
    if argv in ['cd', 'printenv', 'export', 'unset', 'exit', 'pwd']:
        return True
    else:
        return False


def change_path(argv):
    if len(argv) == 1 and 'HOME' in os.environ:
        os.chdir(os.environ['HOME'])
    elif len(argv) > 1:
        path = os.path.abspath(argv[1])
        if os.path.isdir(path):
            os.chdir(path)
    elif 'HOME' not in os.environ:
        print('intek-sh: cd: HOME not set')


def printenv_value(list):
    if len(list) == 1:
        for key in os.environ.keys():
            print(key + '=' + os.environ[key])
    else:
        for key in list[1:]:
            if key in os.environ:
                print(os.environ[key])


def set_env(list):
    if len(list) > 1:
        for item in list[1:]:
            if '=' in item:
                key = item.split('=')[0]
                value = item.split('=')[1]
                os.environ[key] = value
            else:
                os.environ[item] = ""


def unset_env(list):
    if len(list) != 1:
        for key in list[1:]:
            if key in os.environ.keys():
                del os.environ[key]


def run_file(argv):
    if '.' in argv[0]:
        try:
            subprocess.run(argv)
        except FileNotFoundError:
            print('intek-sh: ' + argv[0] + ': command not found')
        except PermissionError:
            print('intek-sh: ' + argv[0] + ': Permission denied')
    else:
        if 'PATH' in os.environ:
            paths = os.environ['PATH'].split(':')
            check = 0
            for path in paths:
                if os.path.exists(path + '/' + argv[0]):
                    argv[0] = path + '/' + argv[0]
                    check = 1
                try:
                    subprocess.run(argv)
                except PermissionError:
                    print('intek-sh: ' + argv[0] + ': Permission denied')
                break
            if check == 0:
                print('intek-sh: ' + argv[0] + ': command not found')
        else:
            print('intek-sh: ' + argv[0] + ': command not found')


def exit(argv):
    if len(argv[1:]) > 0:
        if argv[1] not in '0123456789':
            print('intek-sh: exit:', end='')
            print(' '.join(argv[1:]))


def main():
    command = ''
    try:
        while command != 'exit':
            argv = input('intek-sh$').split(' ')
            argv = [x for x in argv if x]
            if len(argv) != 0:
                if not check_command(argv[0]):
                    print(argv[0] + ': command not found')
                else:
                    command = argv[0]
                    if command == 'cd':
                        change_path(argv)
                    elif command == 'pwd':
                        print(os.getcwd())
                    elif command == 'printenv':
                        printenv_value(argv)
                    elif command == 'export':
                        set_env(argv)
                    elif command == 'unset':
                        unset_env(argv)
                    elif command == 'exit':
                        exit(argv)
    except EOFError:
        pass


if __name__ == '__main__':
    main()
