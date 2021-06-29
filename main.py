import myfunc as f

# 整理したいフォルダのパスを入力
if __name__ == '__main__':
    print('整理したいフォルダのパスを入力してください')
    path = input()

    path = f.unify_path_name(path)
    file_extension = f.check_file_extensions(path)
    f.make_directories(path)
    f.move_f(file_extension, path)