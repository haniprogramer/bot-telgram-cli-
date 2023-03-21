from tkinter import *
import bootand
# from _thread import start_new_thread
import pandas


from pyrogram import Client
from pyrogram import filters


rot = Tk()
rot.title('BOT.BAD')
rot.resizable(width=False, height=False)
rot.geometry('350x270')
rot.configure(bg='Sky blue')
# -----------------------------
trackfram2 = LabelFrame(rot, bg='Sky blue', bd=5, fg='white',text='Log In',font=('Arial',11,'bold'))
trackfram2.place(x=0, y=2, width=350, height=200)
# --------LABEL----------
l1 = Label(trackfram2, text='Phone Number',bg='Sky blue')
l1.place(x=10, y=10)

l2 = Label(trackfram2, text='APP-ID',bg='Sky blue')
l2.place(x=10, y=60)

l3 = Label(trackfram2, text='APP-HASH',bg='Sky blue')
l3.place(x=10, y=105)

# ---------Entries---------
phon_text = IntVar()
phon = Entry(trackfram2, textvariable=phon_text,width=50)
phon.place(x=10, y=30)

appid_text= IntVar()
api_id = Entry(trackfram2,textvariable=appid_text,width=50)
api_id.place(x=10, y=80)

apphash_text = StringVar()
api_hash = Entry(trackfram2, textvariable=apphash_text,width=50)
api_hash.place(x=10, y=130)

# -----------------------------------------------
def log():
    api_id.get()
    api_hash.get()
    phon.get()
# -----------------------------------------------


app = Client('botbadboy', api_id.get(), api_hash.get(),phon.get())

# -----------------------------------------------
def tob2 ():

    root = Tk()
    root.title('BOT.BAD')
    root.resizable(width=False, height=False)
    root.geometry('570x630')
    root.configure(bg='Sky blue')
    # --------LABEL----------

    l3 = Label(root, text='user name',bg='Sky blue')
    l3.place(x=150, y=485)

    l4 = Label(root, text='user name',bg='Sky blue')
    l4.place(x=430, y=485)

    l5 = Label(root, text='user name',bg='Sky blue')
    l5.place(x=150, y=530)

    l6 = Label(root, text='user name',bg='Sky blue')
    l6.place(x=430, y=530)

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



    # ---------------------------------------------------------------

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


    # ----------------------------------------------


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

    # -------------------Excel-----------------------
    def excl ():
        product = {'message': 'h', 'chat': 'hh', 'join': 'join' ,'leave':'leave'}

        data = pandas.DataFrame.from_dict(product, orient='index')
        data = data.transpose()
        wirter = pandas.ExcelWriter('bot.xlsx')
        data.to_excel(wirter)
        wirter.save()

    # --------------------------------------------

    b1 = Button(root, text='View All', width=12, command=view_command)
    b1.place(x=10, y=590)

    b3 = Button(root, text='JOIN', width=12, command=join)
    #
    b3.place(x=10, y=505)

    b4 = Button(root, text='LEAVE', width=12,command=leave)
    #
    b4.place(x=290, y=505)

    b6 = Button(root, text='dialog', width=12 , command=end )
    #
    b6.place(x=290, y=550)

    b7 = Button(root, text='search', width=12,command=search_command)
    b7.place(x=10, y=550)

    b8 = Button(root, text='add', width=12, command=add_command)
    #
    b8.place(x=120, y=590)

    b9 = Button(root, text='Excel', width=12, command=excl, bg='green')
    b9.place(x=230, y=590)

    b10 = Button(root, text='CLOSE', width=12, command=root.destroy , bg='red')
    b10.place(x=340, y=590)

    view_command()


trackfram=LabelFrame(rot,bg='Sky blue',bd=5,fg='white')
trackfram.place(x=0,y=200,width=350,height=70)

b22 = Button(trackfram, text='CLOSE', width=12, command=rot.destroy )
b22.place(x=230, y=17)

b55 = Button(trackfram, text='log in', width=12,command=log)
b55.place(x=20, y=17)

b66 = Button(trackfram, text='next', width=12,command=tob2)
b66.place(x=125, y=17)




rot.mainloop()

# start_new_thread()