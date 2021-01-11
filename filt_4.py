# -*- coding: utf-8 -*-

# Библиотеки:
from get_drv import get_drv
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import date
from datetime import datetime

def filt_4(path_to_urls):
    
    # Открытие файлов:
    yt_ch_urls = open(path_to_urls, "r")
    f_filt_4 = open("filt_4.txt", 'w')

    # Получение драйвера:
    drv = get_drv()

    # Вход в аккаунт:
    drv.get("https://www.youtube.com/")
    sleep(3)
    
    # Нажатие для обхода всплывающих окон:
    drv.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)

    count = 0
    for yt_ch_url in yt_ch_urls:
        count += 1

    yt_ch_urls.seek(0)
    
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

        # Фильтр по наличию почты для связи:
        objects = drv.find_elements_by_xpath("//span[@dir='auto']")

        for obj in objects:
            if obj.get_attribute("innerHTML") == "Чтобы посмотреть адрес электронной почты, ":
                print("Есть адрес электронной почты!!!")
                print(yt_ch_url)
                
                f_filt_4.write(yt_ch_url)
                

        del objects

        print("Фильтр 4: ", x, " из ", count)
        x += 1
        

    # Закрытие файлов:
    yt_ch_urls.close()
    f_filt_4.close()

    # Закрытие браузера:
    drv.quit()

if __name__ == "__main__":

    filt_4("filt_0.txt")
