from tkinter import *
import bootand

from pyrogram import Client
from pyrogram import filters
# import requests


#-----------------------------------
# api_id =
# api_hash = ''
# # phon=''


root = Tk()
root.title('BOT.BAD')
root.resizable(width=False, height=False)
root.geometry('570x790')
root.configure(bg='Sky blue')
# --------LABEL------------------
l1 = Label(root, text='APP-ID',bg='Sky blue')
l1.place(x=80, y=625)

l2 = Label(root, text='APP-HASH',bg='Sky blue')
l2.place(x=330, y=625)

l3 = Label(root, text='user name',bg='Sky blue')
l3.place(x=150, y=485)

l4 = Label(root, text='user name',bg='Sky blue')
l4.place(x=430, y=485)

l5 = Label(root, text='user name',bg='Sky blue')
l5.place(x=150, y=530)

l6 = Label(root, text='user name',bg='Sky blue')
l6.place(x=430, y=530)

l7 = Label(root, text='Phon Number',bg='Sky blue')
l7.place(x=30, y=680)

# -----------------------------------------------
# def log():
#     api_id.get()
#     api_hash.get()
    # phon.get()
# -----------------------------------------------

# ---------Entries---------

join_taxt = StringVar()
e5 = Entry(root, textvariable=join_taxt)
e5.place(x=120, y=510)


leave_taxt = StringVar()
e6 = Entry(root, textvariable=leave_taxt)
e6.place(x=400, y=510)


dialog_taxt = StringVar()
e7 = Entry(root, textvariable=dialog_taxt)
e7.place(x=400, y=550)


search_taxt = StringVar()
e8 = Entry(root, textvariable=search_taxt)
e8.place(x=120, y=550)


appid_text= IntVar()
api_id = Entry(root,textvariable=appid_text,width=30)
api_id.place(x=10, y=650)


apphash_text = StringVar()
api_hash = Entry(root, textvariable=apphash_text,width=50)
api_hash.place(x=210, y=650)


phon_text = IntVar()
phon = Entry(root, textvariable=phon_text,width=30)
phon.place(x=10, y=700)

# ------------------listbox-----------------------

list1 = Listbox(root, width=90, height=30)
list1.grid(row=0, column=0, rowspan=5, columnspan=3)

sb1 = Scrollbar(root)
sb1.place(x=546, y=185)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# ----------------function---------------
def clear_list():
    list1.delete(0, END)


def fill_list(books):
    for book in books:
        list1.insert(END, book)


# -------------function--------------
def view_command():
    clear_list()
    books = bootand.view()
    fill_list(books)

def search_command():
    clear_list()
    books = bootand.search(e8.get())
    fill_list(books)


# --------------------bot--------------------------

app = Client('botbadboy', api_id.get(), api_hash.get())

# -----------------------------------------------

with app:
       def end ():
             x1=e7.get()
             x="@"+x1
             for message in app.iter_history(x):
                  # print(message)
                if message.text or message.sticker or message.command:
                     global h
                     h=message.text or message.sticker  or message.command
                     list1.insert(h)

             # print(message.text or message.sticker or message.command)

             global hh
             hh=message.chat.username or message.chat.first_name or message.chat.title
             list1.insert(hh)

             # print(message.chat.username or message.chat.first_name or message.chat.title)


       end()


def add_command():
    bootand.insert(h,hh)
    view_command()

# ----------جهت اضافه شدن و لفت---------------
with app:
    def join():
        x2 = e5.get()
        xx = "@" + x2
        app.join_chat(xx)
    join()

with app:
    def leave():
        x3= e6.get()
        xxx = "@" + x3
        app.leave_chat(xxx)
    leave()

# ---------------------Button--------------------------

b1 = Button(root, text='View All', width=12, command=view_command)
b1.place(x=10, y=590)

b2 = Button(root, text='CLOSE', width=12, command=root.destroy , bg='red')
b2.place(x=455, y=720)

b3 = Button(root, text='JOIN', width=12, command=join)
b3.place(x=10, y=505)

b4 = Button(root, text='LEAVE', width=12,command=leave)
b4.place(x=290, y=505)

b6 = Button(root, text='dialog', width=12 , command=end)
b6.place(x=290, y=550)

b7 = Button(root, text='search', width=12,command=search_command)
b7.place(x=10, y=550)

b8 = Button(root, text='add', width=12 , command=add_command)
b8.place(x=120, y=590)

# b5 = Button(root, text='log in', width=12,command=log)
# b5.place(x=10, y=60)


view_command()
root.mainloop()