from  common.file_operations import save_to_file


def find_in(iterable, finder, expected):
    for i in iterable:
        if finder(i) == expected:
            return i
    raise NotFoundError(f'{expected} not found in iterable.')


class NotFoundError(Exception):
    pass

save_to_file()
print(__name__)