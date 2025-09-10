import os
import shutil
from datetime import datetime

BASE_DIR = os.getcwd()


# Secondary functions: use to decrease code in main functions
def print_and_save(message):
    print(message)
    save_info(message)


def write_to_file(name, choice, text=None, status='created'):
    with open(name, choice, encoding='utf-8') as file:
        if text:
            file.write(text)
    print_and_save(f'The file {name} was {status}.')


# Main functions: implement the manager logic
def save_info(message):
    current_time = datetime.now()
    result = f'{current_time}:\t{message}'
    with open(os.path.join(BASE_DIR, 'log.txt'), 'a', encoding='utf-8') as file:
        file.write(f'{result}\n')


def change_dir(path):
    if os.path.exists(path):
        os.chdir(path)
        print_and_save(f'Directory was changed to {path}')
    else:
        print(f'The directory {path} does not exist.')
    save_info('Command "change_dir" completed')


def get_list(folders_only=False, files_only=False):
    result = os.listdir(path=os.getcwd())
    elements = 'all elements'
    if folders_only and not files_only:
        result = [f for f in result if os.path.isdir(f)]
        elements = 'folders'
    elif files_only and not folders_only:
        result = [f for f in result if not os.path.isdir(f)]
        elements = 'files'
    print(f'The list of {elements} in this directory:')
    print(*result, sep='\n', end='\n')
    save_info('Command "get_list" completed')


def create_file(name, text=None):
    if name not in os.listdir(path=os.getcwd()):
        write_to_file(name, 'w', text, 'created')
    else:
        print(f'The file {name} already exists.')
        condition = False
        while not condition:
            choice = input('Do you want to re(w)rite it or (a)dd new text to the end of file? (w/a):')
            choice = choice.lower()
            if choice == 'w' or choice == 'a':
                condition = True
                write_to_file(name, choice, text, 'updated')


def create_folder(name):
    try:
        os.mkdir(name)
        print_and_save(f'The folder {name} was created.')
    except FileExistsError:
        print(f'The folder {name} already exists.')


def delete(name):
    try:
        if os.path.isdir(name):
            os.rmdir(name)
        else:
            os.remove(name)
    except FileNotFoundError:
        print(f'The element {name} does not exist.')
    else:
        print_and_save(f'The element {name} was deleted.')


def copy(name):
    current_path = os.getcwd()
    if name not in os.listdir(path=current_path):
        print(f'The element {name} does not exist. The copy was not created.')
    else:
        count = 0
        name_of_copy = name
        if os.path.isdir(name):
            while name_of_copy in os.listdir(path=current_path):
                count += 1
                name_of_copy = f'{name}_{count}'
            shutil.copytree(name, name_of_copy)
        else:
            end_of_name = name.rfind('.')
            while name_of_copy in os.listdir(path=current_path):
                count += 1
                name_of_copy = name.replace(name[end_of_name], f'_{count}.')
            shutil.copy(name, name_of_copy)
        print_and_save(f'The copy of {name} was created as {name_of_copy}.')


if __name__ == '__main__':
    # test of main functions
    get_list()
    get_list(folders_only=True)
    get_list(files_only=True)
    save_info('Checked function save_info')
    create_folder('new_folder')
    create_folder('new_folder')
    copy('new_folder')
    copy('new_folder')
    delete('new_folder')
    delete('new_folder')
    delete('new_folder_1')
    delete('new_folder_2')
    copy('new_folder')
    create_file('text.dat', 'some text')
    create_file('text.dat', 'new text')
    copy('text.dat')
    copy('text.dat')
    delete('text.dat')
    delete('text.dat')
    delete('text_1.dat')
    delete('text_2.dat')
    copy('text.dat')
    create_folder('new_folder')
    change_dir(os.path.join(BASE_DIR, 'new_folder'))
    print(os.getcwd())
    save_info('Checked function save_info after change')
    change_dir(BASE_DIR)
    delete('new_folder')
