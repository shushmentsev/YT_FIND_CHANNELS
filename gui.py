# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

def start():
    pass

def show():
    pass

# Настройка окна:
win = Tk()
win.geometry("750x200")
win.title("YouTube Project")

# Поле для ввода поискового запроса:
txt_atk = Entry(win)  
txt_atk.place(anchor="nw", relx=0.0, y=0, relwidth=0.8, height=40)

# Кнопка "Запустить скрипт"
btn_start = Button(win, text="Запустить")
btn_start.place(anchor="nw", relx=0.8, y=0, relwidth=0.2, height=40)
btn_start.bind("<Button-1>", start)

# Поля для ввода количества подписчиков:
txt_sb_n1 = Entry(win,width=50)
txt_sb_n1.place(anchor="nw", relx=0.0, y=60, relwidth=0.3, height=20)
lbl_sb_n1 = Label(win, text="n1")
lbl_sb_n1.place(anchor="nw", relx=0.3, y=60, relwidth=0.1, height=20)

txt_sb_n2 = Entry(win,width=50)
txt_sb_n2.place(anchor="nw", relx=0.4, y=60, relwidth=0.3, height=20)
lbl_sb_n2 = Label(win, text="n2")
lbl_sb_n2.place(anchor="nw", relx=0.7, y=60, relwidth=0.1, height=20)

lbl_sb = Label(win, text="Подписчики")
lbl_sb.place(anchor="nw", relx=0.8, y=60, relwidth=0.2, height=20)

# Дата регистрации:
txt_date_n1 = Entry(win,width=50)
txt_date_n1.place(anchor="nw", relx=0.0, y=90, relwidth=0.3, height=20)
lbl_date_n1 = Label(win, text="n1")
lbl_date_n1.place(anchor="nw", relx=0.3, y=90, relwidth=0.1, height=20)

txt_date_n2 = Entry(win,width=50)
txt_date_n2.place(anchor="nw", relx=0.4, y=90, relwidth=0.3, height=20)
lbl_date_n2 = Label(win, text="n2")
lbl_date_n2.place(anchor="nw", relx=0.7, y=90, relwidth=0.1, height=20)

lbl_date = Label(win, text="Возраст канала в днях")
lbl_date.place(anchor="nw", relx=0.8, y=90, relwidth=0.2, height=20)

# Количество роликов:
txt_video_n1 = Entry(win,width=50)
txt_video_n1.place(anchor="nw", relx=0.0, y=120, relwidth=0.3, height=20)
lbl_video_n1 = Label(win, text="n1")
lbl_video_n1.place(anchor="nw", relx=0.3, y=120, relwidth=0.1, height=20)

txt_video_n2 = Entry(win,width=50)
txt_video_n2.place(anchor="nw", relx=0.4, y=120, relwidth=0.3, height=20)
lbl_video_n2 = Label(win, text="n2")
lbl_video_n2.place(anchor="nw", relx=0.7, y=120, relwidth=0.1, height=20)

lbl_video = Label(win, text="Количество видео")
lbl_video.place(anchor="nw", relx=0.8, y=120, relwidth=0.2, height=20)

# Наличие почты:
var = BooleanVar()
var.set(1)
c_btn = Checkbutton(win, text="Наличие почты",
                 variable=var,
                 onvalue=1, offvalue=0,
                 command=show)

c_btn.place(anchor="nw", relx=0.0, y=150, relwidth=0.2, height=20)

# Индикатор загрузки:
pb = ttk.Progressbar(win,orient='horizontal',mode='determinate',length=200)
pb.place(anchor="nw", relx=0.0, y=180, relwidth=1.0, height=20)
pb.start()

# Mainloop():
win.mainloop()
