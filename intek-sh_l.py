#!/usr/bin/env python3
import os


def check_command(argu):
    if argu in ['cd', 'printenv', 'export', 'unset', 'exit', 'pwd']:
        return 1
    else:
        return 0


def change_dir(argu):
    if len(argu) == 1:
        os.chdir(os.environ['HOME'])
    elif os.path.isdir(os.path.abspath(argu[1])):
        os.chdir(os.path.abspath(argu[1]))


def print_env_value(list):
    if len(list) != 1:
        for name in list[1:]:
            if name in os.environ:
                print(os.environ[name])
    else:
        for x in os.environ.keys():
            print(x + '=' + os.environ[x])


def set_env(argu):
    if len(argu) == 2:
        tmp = argu[1].split('=')
        if len(tmp) == 2:
            os.environ[tmp[0]] = tmp[1]


def unset(list):
    if len(list) != 1:
        for name in list[1:]:
            if name in os.environ:
                del os.environ[name]


def print_exit_code(argu):
    if len(argu[1:]) > 0:
        print('intek-sh: exit:', end='')
        print(' '.join(argu[1:]))


def main():
    command = 'abc'
    while command != 'exit':
        argu = input('intek-sh$ ').split(' ')
        argu = [x for x in argu if x]
        if len(argu) != 0:
            if not check_command(argu[0]):
                print('intek-sh$ ' + argu[0] + ': command not found')
                command = ''
            else:
                command = argu[0]
            if command == 'cd':
                change_dir(argu)
            elif command == 'pwd':
                print(os.getcwd())
            elif command == 'printenv':
                print_env_value(argu)
            elif command == 'export':
                set_env(argu)
            elif command == 'unset':
                unset(argu)
            elif command == 'exit':
                print_exit_code(argu)


main()
