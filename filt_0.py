# -*- coding: utf-8 -*-

# Функция для получения драйвера:
from get_drv import get_drv

from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

def get_yt_req_url(ans):

    # ans = input("Искать материал по следующим словам (слова разделяются пробелом): ")
    ans_list = ans.split()
    print("ans_list: ", ans_list)
    ans = "+".join(ans_list)
    print("ans: ", ans)
    yt_url = "https://www.youtube.com/results?search_query="
    yt_url = yt_url + ans
    # yt_url = yt_url + "&sp=EgIoAQ%253D%253D"
    print("yt_url: ", yt_url)

    return yt_url

# Получение списка каналов по видеороликам, найденным по поисковому запросу
def filt_0(search_query):

    yt_req_url = get_yt_req_url(search_query)

    # Получение драйвера:
    drv = get_drv()

    # Переход на сайт:
    print(yt_req_url)
    drv.get(str(yt_req_url))

    #sleep(3)

    #butt = driver.find_element_by_id('selectionBar')
    #butt = drv.find_element_by_xpath("//div[@id='tabsContent']/paper-tab[2]")
    #butt.click()

    #sleep(3)

    # Прокручивание до конца страницы:
    for i in range(100):
        drv.find_element_by_tag_name('body').send_keys(Keys.END)
        sleep(0.1)
        print(i)

    # Парсинг всех ссылок:
    f = open("filt_0.txt", 'w')

    # TODO: Находит пары одинаковых ссылок:
    objects = drv.find_elements_by_xpath("//ytd-channel-name[@id='channel-name']/div[@id='container']/div[@id='text-container']/yt-formatted-string[@id='text']/a")
    x = 0
    x_2 = 0
    curr_list = list()
    for obj in objects:
        # print(obj.get_attribute("title"))
        if x % 2 == 0:
            if obj.get_attribute("href") not in curr_list:
                f.write(obj.get_attribute("href") + "\n")
                x_2 += 1
            curr_list.append(obj.get_attribute("href"))
        x += 1
    f.close()

    print("Count 1: ", x)
    print("Количество видеороликов: ", x_2)

    # Закрытие браузера:
    drv.quit()

if __name__ == "__main__":

    filt_0("Репитотор по физике ЕГЭ")
