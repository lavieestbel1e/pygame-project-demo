import os


def human_read_format(size):
    if 0 <= size < 1024:
        return f'{size}B'
    elif 1024 <= size <= 1024 ** 2 - 1:
        value = int(round((size / 1024), 0))
        return f'{value}KB'
    elif 1024 ** 2 <= size <= 1024 ** 3 - 1:
        value = int(round((size / 1024 ** 2), 0))
        return f'{value}MB'
    elif 1024 ** 3 <= size <= 1024 ** 4 - 1:
        value = int(round((size / 1024 ** 3), 0))
        return f'{value}GB'


def get_files_sizes():
    result = []
    for name in os.listdir(os.getcwd()):
        if os.path.isfile(name):
            size = os.path.getsize(name)
            r_size = human_read_format(size)
            result.append(f'{name} {r_size}')
    return '\n'.join(result)


print(get_files_sizes())