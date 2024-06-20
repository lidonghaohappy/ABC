import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
import time
import tkinter as tk
import Sql

class Ui_windows():
    def __init__(self):
        self.setupPara()
        self.setupUi()

    def setupPara(self):
        self.window_width = 400
        self.window_height = 400
        # 设置 RGB 颜色
        self.da_red = "#9c0c13"  # RGB(156, 12, 19)

    def setupUi(self):
        self.win = Tk()
        self.win.title('山东大学校园卡管理系统')
        screenwidth = self.win.winfo_screenwidth()
        screenheight = self.win.winfo_screenheight()
        size = '%dx%d+%d+%d' % (400, 400, (screenwidth - 400) / 2, (screenheight - 400) / 2)
        self.win.geometry(size)
        self.win.resizable(False, False)

        # 获取屏幕尺寸并设置窗口居中的位置和大小
        screenwidth = self.win.winfo_screenwidth()
        screenheight = self.win.winfo_screenheight()

        outer_frame_padding = 20  # 外层框与窗口边框的距离
        outer_frame_width = self.window_width - 2 * outer_frame_padding
        outer_frame_height = self.window_height - 2 * outer_frame_padding

        size = f'{self.window_width}x{self.window_height}+{(screenwidth - self.window_width) // 2}+{(screenheight - self.window_height) // 2}'
        self.win.geometry(size)
        self.win.resizable(False, False)

        # 创建最外层的 Frame
        outer_frame = tk.Frame(self.win, bg="white", bd=5, relief='sunken')  # 使用 da_red 作为背景色
        outer_frame.place(x=outer_frame_padding, y=outer_frame_padding, width=outer_frame_width, height=outer_frame_height)



        # 登录**页面布局
        lab1 = Label(outer_frame, text='山东大学一卡通', font='楷体 25', background="white",fg=self.da_red)
        lab1.place(x=55, y=20)
        self.frame1 = Frame(outer_frame, height=200, width=320, bd=5, relief='sunken',background="white")
        self.frame1.place(x=20, y=70)
        lab_username = Label(self.frame1, text='用户名', font='楷体 15',background="white")
        lab_username.place(x=30, y=30)
        self.entry_username = Entry(self.frame1, width=20,bd=3, relief='sunken')
        self.entry_username.place(x=110, y=30)
        lab_passwd = Label(self.frame1, text='密 码', font='楷体 15',background="white")
        lab_passwd.place(x=30, y=70)
        self.entry_passwd = Entry(self.frame1, width=20, show='*',bd=3, relief='sunken')
        self.entry_passwd.place(x=110, y=70)
        lab4 = Label(self.frame1, text='选择登录类型', font='楷体 12',background="white")
        lab4.place(x=30, y=110)
        self.combo4 = ttk.Combobox(self.frame1, width=10, values=('学生','教职工', '管理员'), state="readonly")
        self.combo4.place(x=150, y=110)
        self.combo4.current(0)  # 默认值
        self.btn1 = ttk.Button(outer_frame, text='登录')
        self.btn1.place(x=50, y=300)
        self.btn2 = ttk.Button(outer_frame, text='取消', command=lambda: self.win.quit())
        self.btn2.place(x=220, y=300)

        # 将 self.win 窗口的背景设置为白色
        self.win.config(background=self.da_red)

    def loop(self):
        self.win.mainloop()

if __name__ == '__main__':
    win = Ui_windows()
    win.loop()