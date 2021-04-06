import os
import shutil
from glob import glob


# unify path name
def unify_path_name(path):
    if path[-1] != '/':
        path = path + '/'
    
    return path


# get extension to create files every extension
def check_file_extension(path):
    file_ls = glob(path + '*')
    file_extension = []
    
    for f in file_ls:
        if os.path.isfile(f) == True:
            file_extension.append(f.split('.')[-1])
        
    file_extension = list(set(file_extension))
    
    return file_extension


# create directories to move files
def make_dir(file_extension, move_path):
    for f_e in file_extension:
        mkdir_p = move_path + f_e
        os.makedirs(mkdir_p)
        
        
# move files
def move_f(file_extension, move_path):
    file_ls = glob(move_path + '*')
    for file in file_ls:
        move_f = move_path + file[-3:]
        shutil.move(file, move_f)