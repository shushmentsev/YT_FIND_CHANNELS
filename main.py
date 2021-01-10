# -*- coding: utf-8 -*-

from filt_0 import filt_0
from filt_1 import filt_1
from filt_2 import filt_2
from filt_3 import filt_3
from filt_4 import filt_4

if __name__ == "__main__":

    # Парсинг ссылок на YouTube-каналы:
    filt_0("Школьная физика")

    # Фильтр по количеству подписчиков:
    filt_1("filt_0.txt")

    # Фильтр по дате регистрации:
    filt_2("filt_1.txt")

    # Фильтр по количеству роликов:
    filt_3("filt_1.txt")

    # Фильтр по наличию почты:
    filt_4("filt_1.txt")

    # Формирование итогового файла с ссылками:
    f_filt_0 = open("filt_0.txt", 'r')
    f_filt_1 = open("filt_1.txt", 'r')
    f_filt_2 = open("filt_2.txt", 'r')
    f_filt_3 = open("filt_3.txt", 'r')
    f_filt_4 = open("filt_4.txt", 'r')
    f_filters = open("filters.txt", 'r')

    # Пересечение множеств со ссылками и запись результата в файл:
    urls_0 = set()
    for url in f_filt_0:
        urls_0.add(url)

    urls_1 = set()
    for url in f_filt_1:
        urls_1.add(url)

    urls_2 = set()
    for url in f_filt_2:
        urls_2.add(url)

    urls_3 = set()
    for url in f_filt_3:
        urls_3.add(url)

    urls_4 = set()
    for url in f_filt_4:
        urls_4.add(url)

    urls = urls_1 & urls_2 & urls_3 & urls_4
    for url in urls:
        f_filters.write(url + "\n")

    # Закрытие файлов:
    f_filt_0.close()
    f_filt_1.close()
    f_filt_2.close()
    f_filt_3.close()
    f_filt_4.close()
    f_filters.close()

    print(urls)

    
    
    
    
