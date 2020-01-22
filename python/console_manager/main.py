import sys
import os
from core import get_list, create_folder, create_file, copy, delete, save_info, change_dir


def main():
    save_info('Start')
    command = ''
    try:
        command = sys.argv[1]
    except IndexError:
        print('Name of command is absent.')

    if command == 'get_list':
        if len(sys.argv) == 3:
            if sys.argv[2] == 'folders':
                get_list(folders_only=True)
            elif sys.argv[2] == 'files':
                get_list(files_only=True)
            else:
                get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Name of file is absent.')
        else:
            if len(sys.argv) > 3:
                create_file(name, ' '.join(sys.argv[3:]))
            else:
                create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Name of folder is absent.')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Name of element is absent.')
        else:
            delete(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Name of element is absent.')
        else:
            copy(name)
    elif command == 'help':
        help_list = ['Help:',
                     'get_list - command, which prints the list of elements in the directory:',
                     'create_file - command, which creates the file',
                     'create_folder - command, which creates the folder',
                     'delete - command, which deletes files or folders',
                     'copy - command, which copies files or folders',
                     'change_dir - command, which changes directory',
                     ]
        print('\n'.join(help_list))
        save_info('Command "Help" completed')
    elif command == 'change_dir':
        try:
            path = sys.argv[2]
        except IndexError:
            print('New path is absent.')
        else:
            change_dir(path)
            print(f'Current directory: {os.getcwd()}')
    else:
        print("If you don't know, which commands can be inputted, enter 'help'")

    save_info('Finish\n')


if __name__ == '__main__':
    main()
