def sorted_files(files):
    files_list = []
    for file_name in files:
        with open(file_name, encoding='utf-8') as f:
            file_info = (file_name, len(f.readlines()))
            files_list.append(file_info)
    sorted_files_list = sorted(files_list, key=lambda x: x[1])
    return sorted_files_list


def merge_files(files):
    sorted_files_list = sorted_files(files)
    with open('result.txt', 'w', encoding='utf-8') as f:
        for file in sorted_files_list:
            with open(file[0], encoding='utf-8') as d:
                f.write(
                    f'{file[0]}\n'
                    f'{file[1]}\n'
                    f'{"".join(d.readlines())}\n'
                )


merge_files(['1.txt', '2.txt', '3.txt'])
