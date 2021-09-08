import json


class country_iter():
    def __init__(self, file_url):
        self.cursor = None
        self.file_url = file_url

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        with open(self.file_url, encoding='utf-8') as f:
            try:
                country = json.load(f)[self.cursor]['translations']['rus']['common'].strip("'")
            except IndexError:
                raise StopIteration
        self.cursor += 1
        return country
