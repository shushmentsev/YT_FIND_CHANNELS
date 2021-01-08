# Функция для получения драйвера:
from get_drv import get_drv

from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

def get_ch_urls(req_url):

    # Получение драйвера:
    drv = get_drv()

    # Переход на сайт:
    drv.get(req_url)

    sleep(3)

    #butt = driver.find_element_by_id('selectionBar')
##    butt = drv.find_element_by_xpath("//div[@id='tabsContent']/paper-tab[2]")
##    butt.click()
##
##    sleep(3)

    # Прокручивание до конца страницы:
    for i in range(100):
        drv.find_element_by_tag_name('body').send_keys(Keys.END)
        sleep(0.1)
        print(i)

    # Парсинг всех ссылок:
##    f = open(PTH_YT_CH_URLS, 'w')
##    objects = drv.find_elements_by_xpath(
##        "//div[@id='items']/ytd-grid-video-renderer/div[@id='dismissable']/ytd-thumbnail/a[@id='thumbnail']")
##    i1 = 1
##    for obj in objects:
##        f.write(obj.get_attribute("href") + "\n")
##        # print(obj.get_attribute("href"))
##        i1 += 1
##
##    f.close()
##
##    print("i1: ", i1)

    # Закрытие браузера:
    drv.quit()

    # # Поиск субтитров:
    # objects_2 = drv.find_elements_by_xpath(
    #     "//div[@id='items']/ytd-grid-video-renderer/div[@id='dismissable']/div[@id='details']/ytd-badge-supported-renderer[@id='video-badges']/div/span")
    #
    # i2 = 0
    # for obj_2 in objects_2:
    #     # print(obj_2)
    #     i2 += 1
    #
    # print("i2: ", i2)

if __name__ == "__main__":

    get_ch_urls("https://www.youtube.com/results?search_query=%D1%84%D0%B8%D0%B7%D0%B8%D0%BA%D0%B0+%D1%80%D0%B5%D0%BF%D0%B5%D1%82%D0%B8%D1%82%D0%BE%D1%80&sp=EgIQAg%253D%253D")
