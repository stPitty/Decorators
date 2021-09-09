from tqdm import tqdm
from os import remove as rm
from country_iter import country_iter
import file_manager as fm
from api import wiki_api
from md5_hash import hash_gen
from decorator import loger2


if __name__ == '__main__':
    #-------------------------Включаем декораторы-----------------
    fm.save_json = loger2(fm.save_json)
    fm.save_file = loger2(fm.save_file)
    hash_gen = loger2(hash_gen)
    wiki_api = loger2(wiki_api)

    # --------------------Задание №1-----------------------------

    one = country_iter('files/countries.json')
    new_countries = []
    try:
        rm('files/write_per_line.txt')
    except FileNotFoundError:
        pass
    for item in tqdm(one,
                     unit=' итерация',
                     desc='Итерируемся по файлу'):
        content = {item: wiki_api(item).json()[-1][0]}
        fm.save_file(content, 'files/write_per_line')
        new_countries.append(content)
    fm.save_json(new_countries, 'files/new_countries')

    # --------------------Задание №2-----------------------------

    for item in hash_gen('files/write_per_line.txt'):
        print(item)
