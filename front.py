# Designed By @Aashish Auti
# Contact us www.techashu.com/contactus OR autiaashish@gmail.com
# Registration FORM
from tkinter import Button, Scrollbar, Listbox, Entry, OptionMenu, StringVar, END, Label, Tk, DISABLED, font

import back

event_price_dict = {
    "CS 1.6": 200,
    "PUBG Single": 30,
    "PUBG Squad": 100,
    "Clash Royal": 30,
    "Photography Mobile": 30,
    "Photography DSLR": 50,
    "Mini Militia": 30,
    "Braniac": 40,
    "tiktok": 20,
    "Bollywood Chaska": 40,
    "Nail art": 20,
    "1 minute game": 10,
    "Ludo King": 20,
    "Mehendi": 20,
    "Circuit Making": 20
}

def entry_changed(*args):
    entry7.delete(0, END)
    amount_text.set(str(event_price_dict[eventname_text.get()]))


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    entry1.delete(0, END)
    entry1.insert(END, selected_tuple[1])
    entry2.delete(0, END)
    entry2.insert(END, selected_tuple[2])
    entry3.delete(0, END)
    entry3.insert(END, selected_tuple[3])
    entry4.delete(0, END)
    entry4.insert(END, selected_tuple[4])
    entry5.delete(0, END)
    entry5.insert(END, selected_tuple[5])
    entry6.delete(0, END)
    entry6.insert(END, selected_tuple[6])
    entry7.delete(0, END)
    entry7.insert(END, selected_tuple[7])


def view_command():
    list1.delete(0, END)
    for row in back.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in back.search(name_text.get(), emailid_text.get(), phone_number_text.get(), collegename_text.get(),
                           eventname_text.get(), participationmode_text.get(), amount_text.get()):
        list1.insert(END, row)


def add_command():
    back.insert(name_text.get(), emailid_text.get(), phone_number_text.get(), collegename_text.get(),
                eventname_text.get(), participationmode_text.get(), amount_text.get())
    list1.delete(0, END)
    list1.insert(END, (
    name_text.get(), emailid_text.get(), phone_number_text.get(), collegename_text.get(), eventname_text.get(),
    participationmode_text.get(), amount_text.get()))


def delete_command():
    back.delete(selected_tuple[0])


def update_command():
    back.update(selected_tuple[0], name_text.get(), emailid_text.get(), phone_number_text.get(), collegename_text.get(),
                eventname_text.get(), participationmode_text.get(), amount_text.get())


window = Tk()
window.title("AlgoRhythm-2018")
window.option_add( "*font", "lucida 8 bold" )
window.config(background='#6ed3cf')
label1 = Label(window, text="AlgoRhythm-2018 CS Department", bg='light blue', font=('Times 20 bold'))

label1.grid(row=0, column=2)

label2 = Label(window, text="Name")
label2.grid(row=1, column=0)

label3 = Label(window, text="Email ID")
label3.grid(row=2, column=0)

label4 = Label(window, text="Phone number")
label4.grid(row=3, column=0)

label5 = Label(window, text="College Name")
label5.grid(row=4, column=0)

label6 = Label(window, text="Event Name:")
label6.grid(row=5, column=0)

label7 = Label(window, text="Participation Mode (Single OR GROUP)")
label7.grid(row=6, column=0)

label8 = Label(window, text="Amount")
label8.grid(row=7, column=0)

label9 = Label(window, text="")
label9.grid(row=8, column=0)

name_text = StringVar()
entry1 = Entry(window, textvariable=name_text)
entry1.grid(row=1, column=1)

emailid_text = StringVar()
entry2 = Entry(window, textvariable=emailid_text)
entry2.grid(row=2, column=1)

phone_number_text = StringVar()
entry3 = Entry(window, textvariable=phone_number_text)
entry3.grid(row=3, column=1)

collegename_text = StringVar()
entry4 = Entry(window, textvariable=collegename_text)
entry4.grid(row=4, column=1)

amount_text = StringVar()
entry7 = Entry(window, textvariable=amount_text, state=DISABLED)

entry7.grid(row=7, column=1)

eventname_text = StringVar()
entry5 = OptionMenu(window, eventname_text, *event_price_dict.keys())
entry5.grid(row=5, column=1)
eventname_text.trace('w', entry_changed)
participationmode_text = StringVar()
entry6 = Entry(window, textvariable=participationmode_text)
entry6.grid(row=6, column=1)

list1 = Listbox(window, height=20, width=100)
list1.grid(row=1, column=3, rowspan=6, columnspan=2)

scrl = Scrollbar(window)
scrl.grid(row=1, column=2, sticky='ns', rowspan=6)

list1.configure(yscrollcommand=scrl.set)
scrl.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=9, column=0)

b2 = Button(window, text="Submit", width=12, command=add_command)
b2.grid(row=9, column=1)

b3 = Button(window, text="Delete entry", width=12, command=delete_command)
b3.grid(row=9, column=2)

b4 = Button(window, text="Search", width=12, command=search_command)
b4.grid(row=9, column=3)

b5 = Button(window, text="Update", width=12, command=update_command)
b5.grid(row=9, column=4)

window.mainloop()
