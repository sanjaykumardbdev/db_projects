# https://www.codermantra.com/tkinter-combobox/

from datetime import date
from pprint import pprint
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import cx_Oracle


class Application(object):
    def __init__(self, master):

        # top frame design:

        topFrame = Frame(master, height=150, bg='#cc5249')
        topFrame.pack(fill=X)

        db_level = Label(topFrame, text='Database Connectivity', bg='white', fg='blue', font='arial 15 bold')
        db_level.place(x=140, y=50)

        # date_level = Label(topFrame, text="Today's Date" +str(date), bg='white', fg='blue', font='arial 10 bold')
        # date_level.place(x=310, y=120)

        date_lbl = Label(topFrame, text="Today's Date:" , font='arial 12 bold', fg='#5d92e8', bg='white')
        date_lbl.place(x=280, y=110)

        # bottom frame design:

        bottomFrame = Frame(master, height=350, bg='#6cd3f0')
        bottomFrame.pack(fill=X)

        # Host Details
        host_lbl = Label(bottomFrame, text="Host:", width=10, font='arial 8 bold', fg='#5d92e8', bg='white')
        host_lbl.place(x=50, y=50)

        self.host_entry = Entry(bottomFrame, width=20, bd=2)
        self.host_entry.insert(0, 'localhost')
        self.host_entry.place(x=150, y=50)


        # Username Details
        user_lbl = Label(bottomFrame, text="User Name:", width=10, font='arial 8 bold', fg='#5d92e8', bg='white')
        user_lbl.place(x=50, y=90)

        self.user_entry = Entry(bottomFrame, width=20, bd=2)
        self.user_entry.insert(0, 'scott')
        self.user_entry.place(x=150, y=90)

        # self.user_combobox = Combobox(bottomFrame, width=20, values = 'list1')
        # self.user_combobox = Combobox(bottomFrame, width=20)
        # self.user_combobox.current(0)
        # self.user_combobox.place(x=320, y=90)

        # Password Details
        pass_lbl = Label(bottomFrame, text="Password:", width=10, font='arial 8 bold', fg='#5d92e8', bg='white')
        pass_lbl.place(x=50, y=130)

        self.pass_entry = Entry(bottomFrame, width=20, bd=2,show='*')
        self.pass_entry.insert(0, 'tiger')
        self.pass_entry.place(x=150, y=130)

        # Button Test Connnection:
        val_conn_btn = Button(bottomFrame, text='Test Connection', width=17, height=1, font='arial 8 bold', fg='#5d92e8', bg='white', command=self.testconn)
        val_conn_btn.place(x=150, y=170)

        # Button Connect database:
        val_conn_btn = Button(bottomFrame, text='Connect Database', width=17, height=1, font='arial 8 bold', fg='#5d92e8', bg='white', command=self.Connect_Db)
        val_conn_btn.place(x=150, y=200)

        self.lst_box = Listbox(bottomFrame)
        self.lst_box.place(x=320, y=140)

    def testconn(self):
        host = self.host_entry.get()
        username = self.user_entry.get()
        password = self.pass_entry.get()
        # print(host + ' ' + username + ' ' + password)

        host = host+':1521/XE'
        # db = cx_Oracle.connect('scott', 'tiger', 'localhost:1521/XE')
        # db_cur = db.cursor()
        # print(host + ' ' + username + ' ' + password)

        try:
            # self.lst_box.delete(0,END)
            db_connect = cx_Oracle.connect(username, password, host)
            db_cur = db_connect.cursor()
            print(db_cur)
            dt = db_cur.execute('select sysdate from dual').fetchone()
            # print(dt[0])

            # tab_name = db_cur.execute('select tname from tab')
            # # pprint(tab_name)
            # cnt = 1
            # for i in tab_name:
            #     # self.user_combobox.bind(str(i[0]))
            #     # self.lst_box.insert(str(cnt), str(i[0]))
            #     self.user_combobox.bind("<<ComboboxSelected>>")
            #     cnt += 1


        except Exception as e:
            print('db connection err' + str(e))



    def Connect_Db(self):
        pass


        # conn_success_lbl = Label(bottomFrame, text="Success", width=9, font='arial 8 bold')
        # conn_success_lbl.place(x=370, y=170)
        #
        # conn_success_lbl = Label(bottomFrame, text="Failed", width=9, font='arial 8 bold')
        # conn_success_lbl.place(x=370, y=170)
        #
        # conn_success_lbl = Label(bottomFrame, text="Please check user/password", width=25, font='arial 8 bold')
        # conn_success_lbl.place(x=150, y=200)


def main():
    root = Tk()
    Application(root)
    root.title('DB Connectivity')
    root.geometry('500x500+150+100')
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    main()
