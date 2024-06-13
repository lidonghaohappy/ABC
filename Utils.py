from tkinter import *
from tkinter import ttk, messagebox
import time
import tkinter as tk
import Sql
from Windows import Ui_windows

def add(sql, ID, money, time1):
    sql.connectSql()
    cursor = sql.conn.execute('select money from CDINFO where ID = "' + ID + '"')
    temp = cursor.fetchall()
    sql.connectSql()
    cursor1 = sql.conn.execute('SELECT banji, major FROM USERINFO WHERE ID = ?', (ID,))
    user_info = cursor1.fetchall()
    if not user_info:
        messagebox.showerror('错误', '未找到对应的用户信息')
        return
    banji, major = user_info[0]
    money1 = temp[0][0]
    sql1 = 'update CDINFO set money = "' + str(
        money1 + float(money)) + '" where ID = "' + ID + '"'
    temp = '充值' + money + '元'
    sql2 = 'insert into HISTORY values("' + ID + '","' + time1 + '","' + temp + '","' + banji + '","' + major + '")'
    sql.doSql(sql1)
    sql.doSql(sql2)
    sql.connectSql()
    cursor = sql.conn.execute('select money from CDINFO where ID = "' + ID + '"')
    temp = cursor.fetchall()
    money2 = temp[0][0]
    messagebox.showinfo('恭喜', '充值成功！当前余额为%0.2f' % money2 + ' 元')
    return money2

def checkAddUser(sql, ID, name, sex, banji, major, passwd, people, time1):
    if ID == '':
        messagebox.showerror('错误', '卡号不能为空')
        return False
    if len(ID) != 8:
        messagebox.showerror('错误', '卡号必须为8位')
        return False
    sql.connectSql()
    cursor = sql.conn.execute('SELECT * from USERINFO where ID= "' + ID + '"')
    temp = cursor.fetchall()
    if len(temp) != 0:
        messagebox.showerror('错误', '卡号已存在')
        return False
    if name == '':
        messagebox.showerror('错误', '姓名不能为空')
        return False
    if banji != '':
        if len(banji) != 1:
            messagebox.showerror('错误', '班级输入有误')
            return False
    if people == '':
        messagebox.showerror('错误', '请选择用户类别')
        return False

    sql1 = 'insert into USERINFO values("' + ID + '","' + name + '","' + sex + '","' + banji + '","' + major + '")'
    sql2 = 'insert into USER values("' + ID + '","' + passwd + '","' + people + '")'
    sql3 = 'insert into CDINFO values("' + ID + '","0","0")'
    sql4 = 'insert into HISTORY values("' + ID + '","' + time1 + '","0","0","0")'

    sql.doSql(sql1)
    sql.doSql(sql2)
    sql.doSql(sql3)
    sql.doSql(sql4)

    messagebox.showinfo('恭喜', '新建成功！')
    return True

def checkinfoWin(sql, ID, name, sex, banji, major):
    if name == '':
        messagebox.showerror('错误', '姓名不能为空')
        return False
    if banji != '':
        if len(banji) != 1:
            messagebox.showerror('错误', '请输入正确班级号')
            return False
    ask = messagebox.askyesnocancel('注意', '是否保存修改？')
    if ask == True:
        sql1 = 'update USERINFO set name = "' + name + '", sex = "'
        sql1 += sex + '", banji = "' + banji + '",major ="' + major + '"'
        sql.doSql(sql1)
        messagebox.showinfo('恭喜', '修改成功！')
        return True
    elif ask == False:
        return True
    else:
        return False

def jian(sql, ID, time1, money):
    sql.connectSql()
    cursor = sql.conn.execute('select money from CDINFO where ID = "' + ID + '"')
    temp = cursor.fetchall()
    money1 = temp[0][0]
    sql.connectSql()
    cursor1 = sql.conn.execute('SELECT banji, major FROM USERINFO WHERE ID = ?', (ID,))
    user_info = cursor1.fetchall()

    if not user_info:
        messagebox.showerror('错误', '未找到对应的用户信息')
        return False

    banji, major = user_info[0]
    sql1 = 'update CDINFO set money = "' + str(
        money1 - float(money)) + '" where ID = "' + ID + '"'
    temp = '消费' + money + '元'

    sql2 = 'insert into HISTORY values("' + ID + '","' + time1 + '","' + temp + '","' + banji + '","' + major + '")'
    sql.doSql(sql1)
    sql.doSql(sql2)
    sql.connectSql()
    cursor = sql.conn.execute('select money from CDINFO where ID = "' + ID + '"')
    temp = cursor.fetchall()
    money2 = temp[0][0]
    messagebox.showinfo('恭喜', '消费成功！当前余额为%0.2f' % money2 + ' 元')
    return money2

def checkPasswd(sql, passwd, passwd1, passwd2, passwd3):
    if passwd1 != passwd:
        messagebox.showerror('错误', '原密码输入错误')
    elif passwd2 != passwd3:
        messagebox.showerror('错误', '两次输入不一致')
    else:
        sql = 'update USER set passwd = "' + passwd3 + '"'
        sql.doSql(sql)
        messagebox.showinfo('恭喜', '修改成功！')
        return True
    return False

def logout(sql, ID):
    '''注销'''
    if ID == '':
        messagebox.showerror('错误', '请输入要注销的卡号')
        return False
    else:
        sql.connectSql()
        cursor = sql.conn.execute('SELECT * from USER where ID= "' + ID + '"')
        temp = cursor.fetchall()
        if len(temp) == 0:
            messagebox.showerror('错误', '用户不存在')
            return False
        else:
            ask = messagebox.askyesno('提示', '          将要进行注销\n             是否继续？')
            if ask == True:
                sql1 = 'delete from USER where ID = "' + ID + '"'
                sql2 = 'delete from USERINFO where ID = "' + ID + '"'
                sql3 = 'delete from CDINFO where ID = "' + ID + '"'
                sql4 = 'delete from HISTORY where ID = "' + ID + '"'
                sql.doSql(sql1)
                sql.doSql(sql2)
                sql.doSql(sql3)
                sql.doSql(sql4)
                messagebox.showinfo('恭喜', '删除成功！')
                return True
            else:
                return False

def addmoneyRoot(sql, ID):
    '''充值'''
    if ID == '':
        messagebox.showerror('错误', '请输入要充值的卡号')
        return False
    else:
        sql.connectSql()
        cursor = sql.conn.execute('SELECT * from USER where ID= "' + ID + '"')
        temp = cursor.fetchall()
        if len(temp) == 0:
            messagebox.showerror('错误', '用户不存在')
            return False
        else:
            return True

def informationRoot(sql, ID):
    '''详细信息'''
    if ID == '':
        messagebox.showerror('错误', '请输入要查看的卡号')
        return False
    else:
        sql.connectSql()
        cursor = sql.conn.execute('SELECT * from USER where ID= "' + ID + '"')
        temp = cursor.fetchall()
        if len(temp) == 0:
            messagebox.showerror('错误', '用户不存在')
            return False
        else:
            return True