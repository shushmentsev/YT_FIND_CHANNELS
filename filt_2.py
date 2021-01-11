# -*- coding: utf-8 -*-

# Библиотеки:
from get_drv import get_drv
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import date
from datetime import datetime

# Фильтр по дате регистрации:
def filt_2(path_to_urls, days_1, days_2):
    
    # Открытие файлов:
    yt_ch_urls = open(path_to_urls, "r")
    f_filt_2 = open("filt_2.txt", 'w')

    # Получение драйвера:
    drv = get_drv()

    count = len(yt_ch_urls)
    x = 1
    for yt_ch_url in yt_ch_urls:

        # Переход на сайт:
        drv.get(yt_ch_url)

        sleep(3)

        #butt = driver.find_element_by_id('selectionBar')

        # Нажатие для обхода всплывающих окон:
        drv.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)

        sleep(1)

        try:
        
            butt = drv.find_element_by_xpath("//div[@id='tabsContent']/paper-tab[6]")
            butt.click()

        except:

            butt = drv.find_element_by_xpath("//div[@id='tabsContent']/paper-tab[5]")
            butt.click()

        sleep(3)
        # Фильтр по дате:
        obj = drv.find_element_by_xpath("//div[@id='right-column']/yt-formatted-string[2]/span[2]")
        list_1 = obj.get_attribute("innerHTML").split(' ')
        print(list_1)
        list_1 = list_1[:3]
        if "янв" in list_1[1]:
            list_1[1] = 1
        elif "фев" in list_1[1]:
            list_1[1] = 2
        elif "мар" in list_1[1]:
            list_1[1] = 3
        elif "апр" in list_1[1]:
            list_1[1] = 4
        elif "мая" in list_1[1]:
            list_1[1] = 5
        elif "июн" in list_1[1]:
            list_1[1] = 6
        elif "июл" in list_1[1]:
            list_1[1] = 7
        elif "авг" in list_1[1]:
            list_1[1] = 8
        elif "сен" in list_1[1]:
            list_1[1] = 9
        elif "окт" in list_1[1]:
            list_1[1] = 10
        elif "ноя" in list_1[1]:
            list_1[1] = 11
        elif "дек" in list_1[1]:
            list_1[1] = 12

        list_1.reverse()
        print(list_1)

        list_2 = str(datetime.now())
        list_2 = list_2.split(" ")[0].split("-")
        print(list_2)
        
        date_1 = date(int(list_1[0]), int(list_1[1]), int(list_1[2]))
        date_2 = date(int(list_2[0]), int(list_2[1]), int(list_2[2]))
        date_21 = date_2 - date_1
        print(date_21)

        days = int(str(date_21).split(" ")[0])
        print(days)

        if (days >= days_1) and (days < days_2):
            print("Канал подходит по дате регистрации")
            f_filt_2.write(yt_ch_url)

        print(x, " из ", count)
        x += 1
        

    # Закрытие файлов:
    yt_ch_urls.close()
    f_filt_2.close()

    # Закрытие браузера:
    drv.quit()

if __name__ == "__main__":

    filt_2("filt_1.txt", int(0.5 * 365), int(2 * 365))
