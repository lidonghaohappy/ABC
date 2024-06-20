from tkinter import *
from tkinter import ttk, messagebox
import time
import tkinter as tk
import Sql
import Utils
from Windows import Ui_windows


class Ui_main(Ui_windows):
    def __init__(self):
        super().__init__()
        self.setupSql()
        self.setupAction()
        self.ID = '0'
        self.varmoney = StringVar()
        self.infoID = StringVar()
        self.sexSelect = StringVar()
        self.peopleSelect = StringVar()
        self.time1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    def setupSql(self):
        self.sql = Sql.Sql()

    def setupAction(self):
        self.btn1.bind('<Button-1>', self.login)

    def infoWin(self):
        '''详细信息——窗口'''
        self.winInfo = Toplevel()
        screenwidth = self.winInfo.winfo_screenwidth()
        screenheight = self.winInfo.winfo_screenheight()
        sizeWinInfo = '%dx%d+%d+%d' % (500, 500, (screenwidth - 500) / 2, (screenheight - 500) / 2)
        self.winInfo.geometry(sizeWinInfo)
        self.winInfo.title('详细信息')
        self.winInfo.attributes("-toolwindow", 1)  # 新窗口在最上面
        self.winInfo.config(background=self.da_red)
        # 定义外层 Frame
        self.outer_frame_info = tk.Frame(self.winInfo, bg="white", borderwidth=5, relief="sunken")
        self.outer_frame_info.place(x=20, y=20, width=460, height=460)  # 留出一定的距离

        lab11InfoID = Label(self.outer_frame_info, text='卡号', font='楷体 12', fg='red', bg="white").place(x=120, y=10)
        lab12InfoID = Label(self.outer_frame_info, textvariable=self.infoID, font='楷体 12', fg='red', bg="white").place(x=200, y=10)

        lab2InfoName = Label(self.outer_frame_info, text='姓名', font='楷体 12', bg="white").place(x=120, y=60)
        self.entryInfoName = Entry(self.outer_frame_info, width=20)
        self.entryInfoName.place(x=200, y=62)

        lab3InfoName = Label(self.outer_frame_info, text='性别', font='楷体 12', bg="white").place(x=120, y=140)
        self.comboInfoSex = ttk.Combobox(self.outer_frame_info, width=5, height=20, textvariable=self.sexSelect, values=('男', '女'),state="readonly")
        self.comboInfoSex.place(x=200, y=142)
        self.sexSelect.set('男')

        lab41InfoNum = Label(self.outer_frame_info, text='班级', font='楷体 12', bg="white").place(x=120, y=220)
        self.entryInfoNum = Entry(self.outer_frame_info, width=20)
        self.entryInfoNum.place(x=200, y=222)

        lab5Infomajor = Label(self.outer_frame_info, text='专业', font='楷体 12', bg="white").place(x=120, y=300)
        self.entryInfomajor = Entry(self.outer_frame_info, width=20)
        self.entryInfomajor.place(x=200, y=302)

        self.btn1Info = ttk.Button(self.outer_frame_info, text='确定', width=15)
        self.btn1Info.place(x=80, y=400)

        self.btn2Info = ttk.Button(self.outer_frame_info, text='清除', width=15)
        self.btn2Info.place(x=290, y=400)

        self.sql.connectSql()
        cursor = self.sql.conn.execute('select * from USERINFO where ID = "' + self.infoID.get() + '"')
        temp = cursor.fetchall()[0]
        self.entryInfoName.insert(0, temp[1])
        self.sexSelect.set(temp[2])
        self.entryInfoNum.insert(0, temp[3])
        self.entryInfomajor.insert(0, temp[4])

        self.btn1Info.bind('<Button-1>', self.checkinfoWin)
        self.btn2Info.bind('<Button-1>', self.clearinfoWin)

    def checkinfoWin(self, event):
        self.ID = self.infoID.get()
        name = self.entryInfoName.get()
        sex = self.comboInfoSex.get()
        banji = self.entryInfoNum.get()
        major = self.entryInfomajor.get()

        if Utils.checkinfoWin(self.sql, self.ID, name, sex, banji, major):
            self.winInfo.destroy()

    def clearinfoWin(self, event):
        self.entryInfoName.delete(0, END)
        self.entryInfoNum.delete(0, END)
        self.entryInfomajor.delete(0, END)
        self.comboInfoSex.current(0)

    def jianMoneyWin(self):
        '''消费——窗口'''
        self.winjianMoney = Toplevel()
        screenwidth = self.winjianMoney.winfo_screenwidth()
        screenheight = self.winjianMoney.winfo_screenheight()
        sizeWinjianMoney = '%dx%d+%d+%d' % (400, 250, (screenwidth - 400) / 2, (screenheight - 250) / 2)
        self.winjianMoney.geometry(sizeWinjianMoney)
        self.winjianMoney.title('消费')
        self.winjianMoney.attributes("-toolwindow", 1)  # 新窗口在最上面
        self.winjianMoney.config(background=self.da_red)
        # 定义外层 Frame 并设置边框样式和距离
        self.outer_frame_jianMoney = tk.Frame(self.winjianMoney, bg="white", borderwidth=5, relief="sunken")
        self.outer_frame_jianMoney.place(x=20, y=20, width=360, height=220)  # 留出一定的距离

        # 以下代码是其他组件的设置，它们都应该被添加到 outer_frame_jianMoney 中
        self.framejianMoney = Frame(self.outer_frame_jianMoney, height=200, width=340, bd=1, relief='sunken', bg="white")
        self.framejianMoney.place(x=5, y=5)  # 相对于外层 Frame 的位置
        lab1jianMoney = Label(self.framejianMoney, text='消费金额：', font='楷体 12', bg="white").place(x=50, y=30)
        self.entry1jianMoney = Entry(self.framejianMoney, width=20)
        self.entry1jianMoney.place(x=130, y=32)
        self.btn1jianMoney = ttk.Button(self.framejianMoney, text='确认')
        self.btn1jianMoney.place(x=40, y=150)
        self.btn2jianMoney = ttk.Button(self.framejianMoney, text='清除')
        self.btn2jianMoney.place(x=200, y=150)

        self.btn1jianMoney.bind('<Button-1>', self.jian)
        self.btn2jianMoney.bind('<Button-1>', self.clearJianMoney)

    def clearJianMoney(self, event):
        self.entry1jianMoney.delete(0, END)

    def jian(self, event):
        money = self.entry1AddMoney.get()
        money2 = Utils.jian(self.sql, self.ID, self.time1, money)
        if money2:
            self.varmoney.set(money2)
            self.winjianMoney.destroy()

    def addMoneyWin(self):
        '''充值——窗口'''
        self.winAddMoney = Toplevel()
        # 获取屏幕尺寸并设置窗口居中的位置和大小
        screenwidth = self.winAddMoney.winfo_screenwidth()
        screenheight = self.winAddMoney.winfo_screenheight()
        sizeWinAddMoney = '%dx%d+%d+%d' % (400, 250, (screenwidth - 400) / 2, (screenheight - 250) / 2)
        self.winAddMoney.geometry(sizeWinAddMoney)
        self.winAddMoney.title('充值')
        self.winAddMoney.attributes("-toolwindow", 1)  # 新窗口在最上面
        self.winAddMoney.config(background=self.da_red)
        # 定义外层 Frame 并设置边框样式和距离
        self.outer_frame_addMoney = tk.Frame(self.winAddMoney, bg="white", borderwidth=5, relief="sunken")
        # 留出一定的距离，此处假设距离为 20 像素
        self.outer_frame_addMoney.place(x=20, y=20, width=360, height=220)

        # 以下代码是其他组件的设置，它们都应该被添加到 outer_frame_addMoney 中
        self.frameAddMoney = Frame(self.outer_frame_addMoney, height=200, width=340, bd=1, relief='sunken', bg="white")
        self.frameAddMoney.place(x=5, y=5)  # 相对于外层 Frame 的位置
        lab1AddMoney = Label(self.frameAddMoney, text='充值金额：', font='楷体 12', bg="white").place(x=50, y=30)
        self.entry1AddMoney = Entry(self.frameAddMoney, width=20)
        self.entry1AddMoney.place(x=130, y=32)
        self.btn1AddMoney = ttk.Button(self.frameAddMoney, text='确认')
        self.btn1AddMoney.place(x=40, y=150)
        self.btn2AddMoney = ttk.Button(self.frameAddMoney, text='清除')
        self.btn2AddMoney.place(x=200, y=150)

        self.btn1AddMoney.bind('<Button-1>', self.add)
        self.btn2AddMoney.bind('<Button-1>', self.clearAddMoney)

    def clearAddMoney(self, event):
        self.entry1AddMoney.delete(0, END)

    def add(self, event):
        money = self.entry1AddMoney.get()
        money2 = Utils.add(self.sql, self.ID, money, self.time1)
        if money2:
            self.varmoney.set(money2)
            self.winAddMoney.destroy()

    def lookWin(self):
        '''查看历史——窗口'''
        self.winLookWin = Toplevel()
        # 获取屏幕尺寸并设置窗口居中的位置和大小
        screenwidth = self.winLookWin.winfo_screenwidth()
        screenheight = self.winLookWin.winfo_screenheight()
        sizeLookWin = '%dx%d+%d+%d' % (550, 300, (screenwidth - 550) / 2, (screenheight - 300) / 2)
        self.winLookWin.geometry(sizeLookWin)
        self.winLookWin.title('流水查询')
        self.winLookWin.attributes("-toolwindow", 1)  # 新窗口在最上面
        self.winLookWin.config(background=self.da_red)
        # 定义外层 Frame 并设置边框样式和距离
        self.outer_frame_lookWin = tk.Frame(self.winLookWin, bg="white", borderwidth=5, relief="sunken")
        # 留出一定的距离，此处假设距离为 20 像素
        self.outer_frame_lookWin.place(x=20, y=20, width=510, height=260)

        # 在外层 Frame 上放置用来显示表格信息的表格组件
        self.frame = Frame(self.outer_frame_lookWin, height=300, width=500, bd=1, relief='sunken', bg="white")
        self.frame.place(x=3, y=3)
        # 滚动条
        self.scrollBar = Scrollbar(self.frame)
        self.scrollBar.pack(side=RIGHT, fill=Y)
        # Treeview 组件
        self.treeList = ttk.Treeview(self.frame, height=13, columns=('c1', 'c2', 'c3'), show="headings",
                                yscrollcommand=self.scrollBar.set)
        self.treeList.column('c1', width=170, anchor='center')
        self.treeList.column('c2', width=170, anchor='center')
        self.treeList.column('c3', width=170, anchor='center')
        self.treeList.heading('c1', text='卡号')
        self.treeList.heading('c2', text='操作时间')
        self.treeList.heading('c3', text='明细（元）')
        self.treeList.pack(side=LEFT, fill=BOTH)
        # Treeview 组件与垂直滚动条结合
        self.scrollBar.config(command=self.treeList.yview)

    def newWin(self):
        self.winNewWin = Toplevel(self.win)
        screenwidth = self.winNewWin.winfo_screenwidth()
        screenheight = self.winNewWin.winfo_screenheight()
        sizeWinNewWin = '%dx%d+%d+%d' % (500, 500, (screenwidth - 500) / 2, (screenheight - 500) / 2)
        self.winNewWin.geometry(sizeWinNewWin)
        self.winNewWin.title('用户操作')
        self.winNewWin.attributes("-toolwindow", 1)  # 新窗口在最上面
        self.winNewWin.config(background=self.da_red)
        # 定义外层 Frame 并设置边框样式和距离
        self.outer_frame_newWin = tk.Frame(self.winNewWin, bg="white", borderwidth=5, relief="sunken")
        # 留出一定的距离，此处假设距离为 20 像素
        self.outer_frame_newWin.place(x=20, y=20, width=460, height=460)

        lab1NewWin = Label(self.outer_frame_newWin, text='欢迎使用一卡通管理系统', font='楷体 15', bg="white")
        lab1NewWin.place(x=120, y=30)

        self.frameNewWin = Frame(self.outer_frame_newWin, height=450, width=395, bd=1, relief='sunken', bg="white")
        self.frameNewWin.place(x=30, y=110)

        lab2NewWin = Label(self.frameNewWin, text='卡号：', font='楷体 12', bg="white").place(x=90, y=50)
        self.entryNewWinID = Entry(self.frameNewWin, width=20)
        self.entryNewWinID.place(x=150, y=54)

        self.btn1NewWin = ttk.Button(self.frameNewWin, text='修改密码', width=18)
        self.btn1NewWin.place(x=130, y=120)

        self.btn2NewWin = ttk.Button(self.frameNewWin, text='充     值', width=18)
        self.btn2NewWin.place(x=130, y=150)

        self.btn6NewWin = ttk.Button(self.frameNewWin, text='消     费', width=18)
        self.btn6NewWin.place(x=130, y=180)

        self.btn3NewWin = ttk.Button(self.frameNewWin, text='详细信息', width=18)
        self.btn3NewWin.place(x=130, y=210)

        self.btn4NewWin = ttk.Button(self.frameNewWin, text='挂     失', width=18)
        self.btn4NewWin.place(x=130, y=240)

        self.btn5NewWin = ttk.Button(self.frameNewWin, text='流水查询', width=18)
        self.btn5NewWin.place(x=130, y=270)

        lab3NewWin = Label(self.frameNewWin, text='余额：', font='楷体 12', bg="white").place(x=105, y=320)
        lab4NewWin = Label(self.frameNewWin, width=5, textvariable=self.varmoney, font='楷体 12', bg="white").place(x=165, y=320)
        lab5NewWin = Label(self.frameNewWin, text='(元)', font='楷体 12', bg="white").place(x=235, y=320)
        self.sql.connectSql()
        cursor = self.sql.conn.execute('select money from CDINFO where ID = "' + self.entry_username.get() + '"')
        temp = cursor.fetchall()
        money2 = temp[0][0]

        self.entryNewWinID.insert(0, self.entry_username.get())
        self.varmoney.set(money2)

        self.btn1NewWin.bind('<Button-1>', self.alterPasswd)
        self.btn2NewWin.bind('<Button-1>', self.addmoney)
        self.btn3NewWin.bind('<Button-1>', self.information)
        self.btn4NewWin.bind('<Button-1>', self.lost)
        self.btn5NewWin.bind('<Button-1>', self.look)
        self.btn6NewWin.bind('<Button-1>', self.jianmoney)

    def alterPasswd(self, event):
        '''修改密码'''
        self.winAlterPasswd = Toplevel(self.winNewWin)
        screenwidth = self.winAlterPasswd.winfo_screenwidth()
        screenheight = self.winAlterPasswd.winfo_screenheight()
        sizeWinAlterPasswd = '%dx%d+%d+%d' % (400, 250, (screenwidth - 400) / 2, (screenheight - 250) / 2)
        self.winAlterPasswd.geometry(sizeWinAlterPasswd)
        self.winAlterPasswd.title('修改密码')
        self.winAlterPasswd.attributes("-toolwindow", 1)  # 新窗口在最上面
        self.winAlterPasswd.config(background=self.da_red)
        # 定义外层 Frame 并设置边框样式和距离
        self.outer_frame_alterPasswd = tk.Frame(self.winAlterPasswd, bg="white", borderwidth=5, relief="sunken")
        # 留出一定的距离，此处假设距离为 20 像素
        self.outer_frame_alterPasswd.place(x=20, y=20, width=360, height=210)

        self.frameAlterPasswd = Frame(self.outer_frame_alterPasswd, height=200, width=340, bd=1, relief='sunken',
                                 bg="white")
        self.frameAlterPasswd.place(x=10, y=10)  # 相对于外层 Frame 的位置
        lab1AlterPasswd = Label(self.frameAlterPasswd, text='原密码：', font='楷体 12', bg="white")
        lab1AlterPasswd.place(x=50, y=30)
        self.entry1AlterPasswd = Entry(self.frameAlterPasswd, show='*', width=20)
        self.entry1AlterPasswd.place(x=130, y=32)
        lab1AlterPasswd = Label(self.frameAlterPasswd, text='新密码：', font='楷体 12', bg="white").place(x=50, y=60)
        self.entry2AlterPasswd = Entry(self.frameAlterPasswd, show='*', width=20)
        self.entry2AlterPasswd.place(x=130, y=62)
        lab1AlterPasswd = Label(self.frameAlterPasswd, text='确认密码：', font='楷体 12', bg="white").place(x=50, y=90)
        self.entry3AlterPasswd = Entry(self.frameAlterPasswd, show='*', width=20)
        self.entry3AlterPasswd.place(x=130, y=92)
        self.btn1AlterPasswd = ttk.Button(self.frameAlterPasswd, text='确认')
        self.btn1AlterPasswd.place(x=40, y=150)
        self.btn2AlterPasswd = ttk.Button(self.frameAlterPasswd, text='清除')
        self.btn2AlterPasswd.place(x=200, y=150)

        self.btn1AlterPasswd.bind('<Button-1>', self.checkPasswd)
        self.btn2AlterPasswd.bind('<Button-1>', self.clearPasswd)

    def clearPasswd(self, event):
        self.entry1AlterPasswd.delete(0, END)
        self.entry2AlterPasswd.delete(0, END)
        self.entry3AlterPasswd.delete(0, END)

    def checkPasswd(self, event):
        passwd = self.entry_passwd.get()
        passwd1 = self.entry1AlterPasswd.get()
        passwd2 = self.entry2AlterPasswd.get()
        passwd3 = self.entry3AlterPasswd.get()
        if Utils.checkPasswd(self.sql, passwd, passwd1, passwd2, passwd3):
            self.winAlterPasswd.destroy()
            self.winNewWin.destroy()
            self.entry_passwd.delete(0, END)
            messagebox.showwarning('提示', '请重新登录')

    def addmoney(self, event):
        self.ID = self.entryNewWinID.get()
        self.addMoneyWin()

    def jianmoney(self, event):
        '''消费'''
        self.ID = self.entryNewWinID.get()
        self.jianMoneyWin()

    def information(self, event):
        '''详细信息'''
        self.infoID.set(self.entryNewWinID.get())
        self.infoWin()

    def lost(self, event):
        '''挂失'''
        ask = messagebox.askyesno('提示', '将要进行挂失，挂失后将不能自助解锁\n\t是否继续？')
        if ask == True:
            if self.sql.check_lock(self.entryNewWinID.get()):
                sql = 'update CDINFO set lock = "1" where ID = "' + self.entryNewWinID.get() + '"'
                self.sql.doSql(sql)
                self.winNewWin.destroy()
        else:
            return

    def look(self, event):
        '''查看历史'''
        self.lookWin()
        self.showall(self.entryNewWinID.get())

    # 登录**函数定义
    def login(self, event):
        # 学生/教职工登录
        if self.combo4.get() == '学生' or self.combo4.get() == '教职工':
            self.sql.connectSql()
            cursor = self.sql.conn.execute('SELECT * from USER where ID= "' + self.entry_username.get() + '"')
            temp = cursor.fetchall()
            if len(temp) == 0:
                messagebox.showerror('错误', '用户不存在')
                return
            elif temp[0][2] != self.combo4.get():
                messagebox.showerror('错误', '用户类别不正确')
                return
            elif self.sql.check_lock(self.entry_username.get()):
                passwd = temp[0][1]
                if self.entry_passwd.get() != passwd:
                    messagebox.showerror('错误', '用户名或密码不正确')
                    return
                else:
                    self.newWin()
        # 管理员登录
        elif self.combo4.get() == '管理员':
            if self.entry_username.get() == 'admin' and self.entry_passwd.get() == '123456':
                self.win_root = Toplevel(self.win)
                self.screenwidth = self.win_root.winfo_screenwidth()
                self.screenheight = self.win_root.winfo_screenheight()
                size_root = '%dx%d+%d+%d' % (700, 400, (self.screenwidth - 700) / 2, (self.screenheight - 400) / 2)
                self.win_root.geometry(size_root)
                self.win_root.title('管理员操作')
                self.win_root.attributes("-toolwindow", 1)
                self.win_root.config(background=self.da_red)
                # 定义外层 Frame 并设置边框样式和距离
                self.outer_frame_root = tk.Frame(self.win_root, bg="white", borderwidth=5, relief="sunken")
                # 留出一定的距离，此处假设距离为 20 像素
                self.outer_frame_root.place(x=20, y=20, width=660, height=360)  # 根据实际需要调整宽度和高度

                # 管理员页面布局
                lab1_root = Label(self.outer_frame_root, text='欢迎进入管理员界面', font='楷体 15', bg="white")
                lab1_root.place(x=250, y=30)

                self.frame1_root = Frame(self.outer_frame_root, height=200, width=600, bd=1, relief='sunken', bg="white")
                self.frame1_root.place(x=28, y=110)  # 相对于外层 Frame 的位置
                lab2_root = Label(self.frame1_root, text='卡号：', font='楷体 12', bg="white")
                lab2_root.place(x=30, y=80)
                self.entry_ser_num = Entry(self.frame1_root, width=20)
                self.entry_ser_num.place(x=80, y=84)

                self.btn1_root = ttk.Button(self.frame1_root, text='新建持卡者', width=18)
                self.btn1_root.place(x=280, y=30)

                self.btn2_root = ttk.Button(self.frame1_root, text='充值', width=18)
                self.btn2_root.place(x=280, y=85)

                self.btn3_root = ttk.Button(self.frame1_root, text='注销一卡通', width=18)
                self.btn3_root.place(x=280, y=140)

                self.btn4_root = ttk.Button(self.frame1_root, text='更改持卡者详细信息', width=18)
                self.btn4_root.place(x=450, y=30)

                self.btn5_root = ttk.Button(self.frame1_root, text='挂失/解锁', width=18)
                self.btn5_root.place(x=450, y=85)

                self.btn6_root = ttk.Button(self.frame1_root, text='查询消费历史', width=18)
                self.btn6_root.place(x=450, y=140)

                self.btn1_root.bind('<Button-1>', self.addUser)
                self.btn2_root.bind('<Button-1>', self.addmoneyRoot)
                self.btn3_root.bind('<Button-1>', self.logout)
                self.btn4_root.bind('<Button-1>', self.informationRoot)
                self.btn5_root.bind('<Button-1>', self.lostUnlock)
                self.btn6_root.bind('<Button-1>', self.lookRoot)
            else:
                messagebox.showerror('错误', '用户名或密码错误！')

    # 管理员***函数定义
    def addUser(self, event):
        '''新建用户'''
        self.win_root_new = Toplevel(self.win_root)
        screenwidth = self.win_root_new.winfo_screenwidth()
        screenheight = self.win_root_new.winfo_screenheight()
        size_root_new = '%dx%d+%d+%d' % (500, 500, (screenwidth - 500) / 2, (screenheight - 500) / 2)
        self.win_root_new.geometry(size_root_new)
        self.win_root_new.title('新建用户')
        self.win_root_new.config(background=self.da_red)
        # 定义外层 Frame 并设置边框样式和距离
        self.outer_frame_new = tk.Frame(self.win_root_new, bg="white", borderwidth=5, relief="sunken")
        # 留出一定的距离，此处假设距离为 20 像素
        self.outer_frame_new.place(x=20, y=20, width=460, height=460)  # 根据实际需要调整宽度和高度

        lab11_root_new = Label(self.win_root_new, text='卡号', font='楷体 12', bg="white").place(x=140, y=60)
        lab12_root_new = Label(self.win_root_new, text='*', fg='red', bg="white").place(x=180, y=60)
        self.entry_new_ID = Entry(self.win_root_new, width=20)
        self.entry_new_ID.place(x=220, y=62)

        lab21_root_new = Label(self.win_root_new, text='姓名', font='楷体 12', bg="white").place(x=140, y=100)
        lab22_root_new = Label(self.win_root_new, text='*', fg='red', bg="white").place(x=180, y=100)
        self.entry_new_name = Entry(self.win_root_new, width=20)
        self.entry_new_name.place(x=220, y=102)

        lab3_root_new = Label(self.win_root_new, text='性别', font='楷体 12', bg="white").place(x=140, y=140)
        self.combo_new_sex = ttk.Combobox(self.win_root_new, width=5, height=20, values=('男', '女'), state="readonly")
        self.combo_new_sex.place(x=220, y=142)
        self.combo_new_sex.current(0)

        lab4_root_new = Label(self.win_root_new, text='班级', font='楷体 12', bg="white").place(x=140, y=200)
        self.entry_new_phone = Entry(self.win_root_new, width=20)
        self.entry_new_phone.place(x=220, y=202)

        lab5_root_new = Label(self.win_root_new, text='专业', font='楷体 12', bg="white").place(x=140, y=240)
        self.entry_new_major = Entry(self.win_root_new, width=20)
        self.entry_new_major.place(x=220, y=242)

        lab6_root_new = Label(self.win_root_new, text='类别', font='楷体 12', bg="white").place(x=140, y=280)
        self.comboInfoPeople = ttk.Combobox(self.win_root_new, width=5, height=20, textvariable=self.peopleSelect,
                                       values=('学生', '教职工'), state="readonly")
        self.comboInfoPeople.place(x=220, y=282)
        self.peopleSelect.set('')

        self.btn1_root_new = ttk.Button(self.win_root_new, text='确定', width=15)
        self.btn1_root_new.place(x=100, y=400)

        self.btn2_root_new = ttk.Button(self.win_root_new, text='清除', width=15)
        self.btn2_root_new.place(x=300, y=400)

        self.btn1_root_new.bind('<Button-1>', self.checkAddUser)
        self.btn2_root_new.bind('<Button-1>', self.clearAddUser)

    def checkAddUser(self, event):
        self.ID = self.entry_new_ID.get()
        name = self.entry_new_name.get()
        sex = self.combo_new_sex.get()
        banji = self.entry_new_phone.get()
        major = self.entry_new_major.get()
        passwd = '123456'
        people = self.comboInfoPeople.get()
        if Utils.checkAddUser(self.sql, self.ID, name, sex, banji, major, passwd, people, self.time1):
            self.win_root_new.destroy()

    def clearAddUser(self, event):
        # entry_new_num.delete(0, END)
        self.entry_new_name.delete(0, END)
        self.entry_new_phone.delete(0, END)
        self.entry_new_major.delete(0, END)

    def addmoneyRoot(self, event):
        '''充值'''
        self.ID = self.entry_ser_num.get()
        if Utils.addmoneyRoot(self.sql, self.ID):
            self.addMoneyWin()

    def logout(self, event):
        '''注销'''
        self.ID = self.entry_ser_num.get()
        Utils.logout(self.sql, self.ID)

    def informationRoot(self, event):
        '''详细信息'''
        self.ID = self.entry_ser_num.get()
        if Utils.informationRoot(self.sql, self.ID):
            self.infoID.set(self.entry_ser_num.get())
            self.infoWin()

    def lostUnlock(self, event):
        '''挂失解锁'''
        if self.entry_ser_num.get() == '':
            messagebox.showerror('错误', '请输入要挂失/解锁的卡号')
            return
        else:
            self.sql.connectSql()
            cursor = self.sql.conn.execute('SELECT * from USER where ID= "' + self.entry_ser_num.get() + '"')
            temp = cursor.fetchall()
            if len(temp) == 0:
                messagebox.showerror('错误', '用户不存在')
                return

        self.winLostUnlock = Toplevel(self.win_root)
        sizeLostUnlock = '%dx%d+%d+%d' % (400, 250, (self.screenwidth - 400) / 2, (self.screenheight - 250) / 2)
        self.winLostUnlock.geometry(sizeLostUnlock)
        self.winLostUnlock.title('挂失/解锁')

        self.btn1LostUnlock = ttk.Button(self.winLostUnlock, text='挂失', width=15)
        self.btn1LostUnlock.place(x=150, y=80)

        self.btn2LostUnlock = ttk.Button(self.winLostUnlock, text='解锁', width=15)
        self.btn2LostUnlock.place(x=150, y=150)

        self.btn1LostUnlock.bind('<Button-1>', self.lock)
        self.btn2LostUnlock.bind('<Button-1>', self.unLock)

    def lock(self, event):
        if self.sql.check_lock(self.entry_ser_num.get()):
            sql = 'update CDINFO set lock = "1" where ID = "' + self.entry_ser_num.get() + '"'
            self.sql.doSql(sql)
            self.winLostUnlock.destroy()
            messagebox.showinfo('提示', '已挂失')

    def unLock(self, event):
        self.sql.connectSql()
        cursor = self.sql.conn.execute('SELECT lock from CDINFO where ID= "' + self.entry_ser_num.get() + '"')
        temp = cursor.fetchall()
        if temp[0][0] == 0:
            messagebox.showerror('错误', '不可重复解锁')
            return
        sql = 'update CDINFO set lock = "0" where ID = "' + self.entry_ser_num.get() + '"'
        self.sql.doSql(sql)
        self.winLostUnlock.destroy()
        messagebox.showinfo('提示', '已解锁')

    def lookRoot(self, event):
        '''查看历史'''
        if self.entry_ser_num.get() == '':
            messagebox.showerror('错误', '请输入要查看的卡号')
            return
        else:
            self.sql.connectSql()
            cursor = self.sql.conn.execute('SELECT * from USER where ID= "' + self.entry_ser_num.get() + '"')
            temp = cursor.fetchall()
            if len(temp) == 0:
                messagebox.showerror('错误', '用户不存在')
                return
            else:
                self.lookWin()
                self.showall(self.entry_ser_num.get())

    # 显示所有信息
    def showall(self, ID):
        for row in self.treeList.get_children():
            self.treeList.delete(row)
        self.sql.connectSql()
        cursor = self.sql.conn.execute('select * from HISTORY where ID ="' + ID + '"')
        temp = cursor.fetchall()
        for i in temp:
            self.treeList.insert('', 'end', values=i)

if __name__ == '__main__':
    win = Ui_main()
    win.loop()