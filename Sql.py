import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
import time
import tkinter as tk

class Sql():
    def __init__(self):
        self.conn = sqlite3.connect('ykt.db')
        self.initTable()


    def initTable(self):
        # 创建表
        try:
            self.conn.execute('''CREATE TABLE USER
                          (ID CHAR(13) PRIMARY KEY NOT NULL ,
                          PASSWD TEXT,
                          TYPE TEXT)''')
            self.conn.execute('''CREATE TABLE USERINFO
                          (ID CHAR(13) PRIMARY KEY NOT NULL ,
                          NAME TEXT,
                          SEX BOOLEAN,
                          banji  CHAR(11),
                          major CHAR(50))''')
            self.conn.execute('''CREATE TABLE CDINFO
                          (ID CHAR(13) PRIMARY KEY NOT NULL,
                          MONEY FLOAT ,
                          LOCK BOOLEAN)''')
            self.conn.execute('''CREATE TABLE HISTORY
                          (ID CHAR(13) ,
                          NAME text
                          TIME TEXT,
                          MONEY FLOAT,
                            BANJI text,
                           ZHUANYE text)''')
            messagebox.showinfo('欢迎使用', '初始化成功！')
            self.conn.close()
        except Exception as e:
            # 打印异常信息
            pass

    def check_lock(self, ID):
        self.conn = sqlite3.connect('ykt.db')
        cursor = self.conn.execute('SELECT lock from CDINFO where ID= "' + ID + '"')
        temp = cursor.fetchall()
        if temp[0][0] == 1:
            messagebox.showinfo('提示', '此一卡通已锁定')
            return False
        else:
            return True
    def connectSql(self):
        self.conn = sqlite3.connect('ykt.db')

    def doSql(self, sql):
        '''用来执行SQL语句，尤其是INSERT和DELETE语句'''
        self.conn = sqlite3.connect('ykt.db')
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()
