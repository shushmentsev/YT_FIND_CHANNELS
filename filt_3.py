# -*- coding: utf-8 -*-

# Библиотеки:
from get_drv import get_drv
from selenium.webdriver.common.keys import Keys
from time import sleep

def filt_3():

    # Открытие файлов:
    yt_ch_urls = open("filt_1.txt", "r")
    f_filt_3 = open("filt_3.txt", 'w')

    # Получение драйвера:
    drv = get_drv()

    for yt_ch_url in yt_ch_urls:

        # Переход на сайт:
        drv.get(yt_ch_url)

        sleep(3)

        #butt = driver.find_element_by_id('selectionBar')

        # Нажатие для обхода всплывающих окон:
        drv.find_element_by_tag_name('body').send_keys(Keys.ESCAPE)
        
        butt = drv.find_element_by_xpath("//div[@id='tabsContent']/paper-tab[2]")
        butt.click()

        sleep(3)

        # Прокручивание до конца страницы:
        for i in range(50):
            drv.find_element_by_tag_name('body').send_keys(Keys.END)
            sleep(0.1)
            print(i)

        # Парсинг всех ссылок:
        objects = drv.find_elements_by_xpath(
            "//div[@id='items']/ytd-grid-video-renderer/div[@id='dismissable']/ytd-thumbnail/a[@id='thumbnail']")
        x = 0
        for obj in objects:
            # print(obj.get_attribute("href"))
            x += 1

        if (x >= 5) and (x <= 30):
            f_filt_3.write(obj.get_attribute("href") + "\n")
            print("Записал ссылку в файл")

        print("Количество видео на канале: ", x)

    # Закрытие файлов:
    yt_ch_urls.close()
    f_filt_3.close()
    
    # Закрытие браузера:
    drv.quit()

if __name__ == "__main__":

    filt_3()
