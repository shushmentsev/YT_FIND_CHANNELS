# Функция для получения драйвера:
from get_drv import get_drv

from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

def get_yt_pg_urls(search_query):

    from get_yt_url import get_yt_url
    yt_url = get_yt_url(search_query)

    # Получение драйвера:
    drv = get_drv()

    # Переход на сайт:
    print(yt_url)
    drv.get(str(yt_url))

    sleep(3)

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
    f = open("yt_pg_urls.txt", 'w')

    # TODO: Находит пары одинаковых ссылок:
    objects = drv.find_elements_by_xpath("//ytd-channel-name[@id='channel-name']/div[@id='container']/div[@id='text-container']/yt-formatted-string[@id='text']/a")
    x = 1
    curr_list = list()
    for obj in objects:
        # print(obj.get_attribute("title"))
        if x % 2 == 0:
            if obj.get_attribute("href") not in curr_list:
                f.write(obj.get_attribute("href") + "\n")
            
            curr_list.append(obj.get_attribute("href"))
        x += 1
    f.close()

    print("Count: ", x)

    # Закрытие браузера:
    drv.quit()

if __name__ == "__main__":

    get_yt_pg_urls("Репитотор по физике ЕГЭ")
