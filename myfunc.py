import os
import shutil
from glob import glob


# unify path name
def unify_path_name(organize_dirctrory_path):
    organize_dirctrory_path = organize_dirctrory_path.replace('\ ', ' ')
    organize_dirctrory_path = organize_dirctrory_path.strip(' ')
    if organize_dirctrory_path[-1] != '/':
        organize_dirctrory_path = organize_dirctrory_path + '/'
    
    return organize_dirctrory_path


# get extension to create files every extension
def check_file_extensions(organize_dirctrory_path):
    file_list = glob(organize_dirctrory_path + '*')
    file_extensions = []
    
    for file in file_list:
        if os.path.isfile(file) == True:
            file_extensions.append(file.split('.')[-1])
        
    file_extensions = list(set(file_extensions))
    
    return file_extensions


# create directories to move files
def make_directories(organize_dirctrory_path):
    file_extensions = check_file_extensions(organize_dirctrory_path)
    created_directory = []
    for file_extension in file_extensions:
        mkdir_to_path = organize_dirctrory_path + file_extension
        try:
            os.makedirs(mkdir_to_path)
        except FileExistsError:
            check = ''
            while True:
                print(f'すでに{organize_dirctrory_path}ディレクトリに{file_extension}ディレクトリが存在します。')
                print('このまま続けても良いですか？[y/n]')
                check = input()
                if check == 'y' or check ==  'n':
                    break
                else:
                    print('yかnを入力してください。')
                
            if check == 'y':
                continue
            elif check == 'n':
                break
        
        
# move files
def move_f(file_extension, move_path):
    file_ls = glob(move_path + '*')
    for file in file_ls:
        move_f = move_path + file[-3:]
        shutil.move(file, move_f)