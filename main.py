import myfunc as f

# 整理したいフォルダのパスを入力
print('整理したいフォルダのパスを入力してください')
path = input()

path = f.unify_path_name(path)
file_extension = f.check_file_extension(path)
f.make_dir(file_extension, path)
f.move_f(file_extension, path)