# -*- coding: utf-8 -*-

# Библиотеки:
from get_drv import get_drv
from selenium.webdriver.common.keys import Keys
from time import sleep

# Фильтр по количеству роликов:
def filt_3(path_to_urls, video_n1, video_n2):

    # Открытие файлов:
    yt_ch_urls = open(path_to_urls, "r")
    f_filt_3 = open("filt_3.txt", 'w')

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

        if (x >= video_n1) and (x <= video_n2):
            f_filt_3.write(obj.get_attribute("href") + "\n")
            print("Записал ссылку в файл")

        print("Количество видео на канале: ", x)

        print(x, " из ", count)
        x += 1

    # Закрытие файлов:
    yt_ch_urls.close()
    f_filt_3.close()
    
    # Закрытие браузера:
    drv.quit()

if __name__ == "__main__":

    filt_3("filt_1.txt")
