import json


def save_json(content, file_name):
    file_name += '.json'
    with open(file_name, 'w+') as file:
        json.dump(content, file, ensure_ascii=False, indent=2)


def save_file(content, file_name):
    file_name += '.txt'
    with open(file_name, 'a') as f:
        f.write(json.dumps(content, ensure_ascii=False, indent=2))
        f.write(',\n')
