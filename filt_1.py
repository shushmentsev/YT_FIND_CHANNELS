# -*- coding: utf-8 -*-

from get_drv import get_drv

def filt_1(path_to_urls):
    #
    #from conf import PTH_H_SUBS_URLS
    yt_ch_urls = open(path_to_urls, "r")

    # Файл для записи:
    f_filt_1 = open("filt_1.txt", "w")

    drv = get_drv()
    for yt_ch_url in yt_ch_urls:

        # Открытие вкладки:
        drv.get(yt_ch_url)

        # Фильтр по числу подписчиков:
        obj = drv.find_element_by_xpath("//yt-formatted-string[@id='subscriber-count']")
        print(obj.get_attribute("innerHTML"))

        if "тыс" not in obj.get_attribute("innerHTML"):
            print(True)
            try:
                my_lst = obj.get_attribute("innerHTML").split(' ')
                print(int(my_lst[0]))

                if int(my_lst[0]) <= 50:

                    print("То, что нужно")
                    f_filt_1.write(yt_ch_url)

            except:

                print("Ошибка")    

    # Закрытие файлов:
    yt_ch_urls.close()
    f_filt_1.close()

    # Закрытие браузера:
    drv.quit()

if __name__ == "__main__":

    filt_1("filt_0.txt")
