from tkinter import *
import backend
window = Tk()
# ============================= Labels ==============================
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)
l1 = Label(window, text="Author")
l1.grid(row=0, column=2)
l1 = Label(window, text="Year")
l1.grid(row=1, column=0)
l1 = Label(window, text="ISBN")
l1.grid(row=1, column=2)
# ============================= Entries ==============================
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)
author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window,width=35,height=6)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

bt1 = Button(window,text="View All",width=12)
bt1.grid(row=2,column=3)

bt1 = Button(window,text="Search Entry",width=12)
bt1.grid(row=3,column=3)

bt1 = Button(window,text="Add Entry",width=12)
bt1.grid(row=4,column=3)

bt1 = Button(window,text="Update Selected",width=12)
bt1.grid(row=5,column=3)

bt1 = Button(window,text="Delete Selected",width=12)
bt1.grid(row=6,column=3)

bt1 = Button(window,text="Close",width=12)
bt1.grid(row=7,column=3)

window.mainloop()