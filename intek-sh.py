#!/usr/bin/env python3
import os
import subprocess


def check_command(argv):
    if argv in ['cd', 'printenv', 'export', 'unset', 'exit', 'pwd']:
        return True
    else:
        return False


def change_path(argv):
    if len(argv) == 1:
        os.chdir(os.environ['HOME'])
    else:
        path = os.path.abspath(argv[1])
        if argv[1] == '$HOME':
            os.chdir(os.environ['HOME'])
        elif os.path.isdir(path):
            os.chdir(path)
        elif os.path.isfile(path):
            print('-bash: cd:' + argv[1] + ': Not a directory')
        else:
            print('-bash: cd:' + argv[1] + ': No such file or directory')


def printenv_value(list):
    if len(list) == 1:
        for key in os.environ.keys():
            print(key + '=' + os.environ[key])
    else:
        for key in list [1:]:
            if key in os.environ:
                print(os.environ[key])
def set_env(list):
    if len(list) == 1:
        print(1)
    else:
        for item in list[1:]:
            key = item.split('=')[0]
            value = item.split('=')[1]
            os.environ[key] = value

def unset_env(list):
    if len(list) != 1:
        for key in list[1:]:
            if key in os.environ.keys():
                del os.environ[key]


def run_file(argv):
    if os.access(argv[0][2:], os.X_OK):
        args_sub = args.append(argv[0])
        for args in argv[1:]:
            args_sub.append(args)
        subprocess.Popen(args_sub)
    else:
        print('Permission denied')




def main():
    command = ''
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
                    exit()


if __name__ == '__main__':
    main()
