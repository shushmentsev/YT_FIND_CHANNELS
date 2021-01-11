# -*- coding: utf-8 -*-

from filt_0 import filt_0
from filt_1 import filt_1
from filt_2 import filt_2
from filt_3 import filt_3
from filt_4 import filt_4

from tkinter import *
from tkinter import ttk

def start():
    
    var_list.append(var_mail.get())

def main_func():
    
    # Парсинг ссылок на YouTube-каналы:
    filt_0(var_req.get())

    # Фильтр по количеству подписчиков:
    filt_1("filt_0.txt", int(var_sb_n1.get()), int(var_sb_n2.get()))

    # Фильтр по дате регистрации:
    filt_2("filt_1.txt", int(var_date_n1.get()), int(var_date_n2.get()))

    # Фильтр по количеству роликов:
    filt_3("filt_1.txt", int(var_video_n1.get()), int(var_video_n2.get()))

    # Фильтр по наличию почты:
    if var_mail.get() == True:
        filt_4("filt_1.txt")

    # Формирование итогового файла с ссылками:
    f_filt_0 = open("filt_0.txt", 'r')
    f_filt_1 = open("filt_1.txt", 'r')
    f_filt_2 = open("filt_2.txt", 'r')
    f_filt_3 = open("filt_3.txt", 'r')

    try:
        f_filt_4 = open("filt_4.txt", 'r')
    except:
        pass
    
    f_filters = open("filters.txt", 'w')

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

def start_gui():
    
    # Настройка окна:
    win = Tk()
    win.geometry("750x200")
    win.title("YouTube Project")

    # Поле для ввода поискового запроса:
    global var_req
    var_req = StringVar()
    txt_atk = Entry(win, textvariable=var_req)  
    txt_atk.place(anchor="nw", relx=0.0, y=0, relwidth=0.8, height=40)

    # Кнопка "Запустить скрипт"
    btn_start = Button(win, text="Запустить", command=main_func)
    btn_start.place(anchor="nw", relx=0.8, y=0, relwidth=0.2, height=40)

    # Поля для ввода количества подписчиков:
    global var_sb_n1
    var_sb_n1 = StringVar()
    txt_sb_n1 = Entry(win, textvariable=var_sb_n1, width=50)
    txt_sb_n1.place(anchor="nw", relx=0.0, y=60, relwidth=0.3, height=20)
    lbl_sb_n1 = Label(win, text="n1")
    lbl_sb_n1.place(anchor="nw", relx=0.3, y=60, relwidth=0.1, height=20)

    global var_sb_n2
    var_sb_n2 = StringVar()
    txt_sb_n2 = Entry(win, textvariable=var_sb_n2, width=50)
    txt_sb_n2.place(anchor="nw", relx=0.4, y=60, relwidth=0.3, height=20)
    lbl_sb_n2 = Label(win, text="n2")
    lbl_sb_n2.place(anchor="nw", relx=0.7, y=60, relwidth=0.1, height=20)

    lbl_sb = Label(win, text="Подписчики")
    lbl_sb.place(anchor="nw", relx=0.8, y=60, relwidth=0.2, height=20)

    # Дата регистрации:
    global var_date_n1
    var_date_n1 = StringVar()
    txt_date_n1 = Entry(win, textvariable=var_date_n1, width=50)
    txt_date_n1.place(anchor="nw", relx=0.0, y=90, relwidth=0.3, height=20)
    lbl_date_n1 = Label(win, text="n1")
    lbl_date_n1.place(anchor="nw", relx=0.3, y=90, relwidth=0.1, height=20)

    global var_date_n2
    var_date_n2 = StringVar()
    txt_date_n2 = Entry(win, textvariable=var_date_n2, width=50)
    txt_date_n2.place(anchor="nw", relx=0.4, y=90, relwidth=0.3, height=20)
    lbl_date_n2 = Label(win, text="n2")
    lbl_date_n2.place(anchor="nw", relx=0.7, y=90, relwidth=0.1, height=20)

    lbl_date = Label(win, text="Возраст канала в днях")
    lbl_date.place(anchor="nw", relx=0.8, y=90, relwidth=0.2, height=20)

    # Количество роликов:
    global var_video_n1
    var_video_n1 = StringVar()
    txt_video_n1 = Entry(win, textvariable=var_video_n1, width=50)
    txt_video_n1.place(anchor="nw", relx=0.0, y=120, relwidth=0.3, height=20)
    lbl_video_n1 = Label(win, text="n1")
    lbl_video_n1.place(anchor="nw", relx=0.3, y=120, relwidth=0.1, height=20)

    global var_video_n2
    var_video_n2 = StringVar()
    txt_video_n2 = Entry(win, textvariable=var_video_n2, width=50)
    txt_video_n2.place(anchor="nw", relx=0.4, y=120, relwidth=0.3, height=20)
    lbl_video_n2 = Label(win, text="n2")
    lbl_video_n2.place(anchor="nw", relx=0.7, y=120, relwidth=0.1, height=20)

    lbl_video = Label(win, text="Количество видео")
    lbl_video.place(anchor="nw", relx=0.8, y=120, relwidth=0.2, height=20)

    # Наличие почты:
    global var_mail
    var_mail = BooleanVar()
    var_mail.set(1)
    c_btn = Checkbutton(win, text="Наличие почты",
                     variable=var_mail,
                     onvalue=1, offvalue=0)

    c_btn.place(anchor="nw", relx=0.0, y=150, relwidth=0.2, height=20)

    # Индикатор загрузки:
    #pb = ttk.Progressbar(win,orient='horizontal',mode='determinate',length=200)
    #pb.place(anchor="nw", relx=0.0, y=180, relwidth=1.0, height=20)
    #pb.start()

    # Mainloop():
    win.mainloop()

if __name__ == "__main__":

    # Графический интерфейс:
    start_gui()

    

    
    
    
    
