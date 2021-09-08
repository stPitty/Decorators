from hashlib import md5


def hash_gen(file_path):
    with open(file_path, encoding='utf-8') as file:
        line = file.readline().encode()
        while line:
            yield md5(line).hexdigest()
            line = file.readline().encode()
