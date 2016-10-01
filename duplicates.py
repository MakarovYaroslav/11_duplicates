import os


def are_files_duplicates(file_path_1, file_path_2):
    file_size_1 = os.path.getsize(file_path_1)
    file_size_2 = os.path.getsize(file_path_2)
    if file_size_1 == file_size_2:
        return True
    return False


def is_name_in_list(paths_list, filename):
    for path in paths_list:
        if filename in path:
            return True, path
    return False

if __name__ == '__main__':
    all_paths = []
    for d, dirs, files in os.walk(os.getcwd()):
        for f in files:
            full_path = os.path.join(d, f)
            file_name = os.path.basename(full_path)
            check_name = is_name_in_list(all_paths, file_name)
            if check_name is not False:
                file_path_from_list = check_name[1]
                if are_files_duplicates(full_path, file_path_from_list):
                    print('Дубликаты:\n%s\n%s' % (
                        full_path, file_path_from_list
                    ))
            all_paths.append(full_path)
