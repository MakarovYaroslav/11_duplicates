import os


def files_have_same_size(file_path_1, file_path_2):
    file_size_1 = os.path.getsize(file_path_1)
    file_size_2 = os.path.getsize(file_path_2)
    if file_size_1 == file_size_2:
        return True
    return False


def find_name_in_list(paths_list, filename):
    for path in paths_list:
        if filename in path:
            return path
    return None

if __name__ == '__main__':
    all_paths = []
    for d, dirs, files in os.walk(os.getcwd()):
        for f in files:
            full_path = os.path.join(d, f)
            file_name = os.path.basename(full_path)
            file_path_from_list = find_name_in_list(all_paths, file_name)
            if file_path_from_list is not None:
                if files_have_same_size(full_path, file_path_from_list):
                    print('Дубликаты:\n%s\n%s' % (
                        full_path, file_path_from_list
                    ))
            all_paths.append(full_path)
