from tkinter import *
import backend


def clear_list():
    list1.delete(0, END)


def fill_list(books):
    for book in books:
        list1.insert(END, book)


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

list1 = Listbox(window, width=35, height=6)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


def get_selected_row(event):
    global selected_book
    index = list1.curselection()[0]
    selected_book = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_book[1])
    e2.delete(0, END)
    e2.insert(END, selected_book[2])
    e3.delete(0, END)
    e3.insert(END, selected_book[3])
    e4.delete(0, END)
    e4.insert(END, selected_book[4])


list1.bind("<<listBoxSelect>>", get_selected_row)


def view_command():
    list1.delete(0, END)
    books = backend.view()
    fill_list(books)


bt1 = Button(window, text="View All", width=12, command=lambda: view_command())
bt1.grid(row=2, column=3)


def search_command():
    clear_list()
    books = backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    fill_list(books)


bt1 = Button(window, text="Search Entry", width=12, command=search_command)
bt1.grid(row=3, column=3)


def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()


bt1 = Button(window, text="Add Entry", width=12, command=lambda: add_command())
bt1.grid(row=4, column=3)

bt1 = Button(window, text="Update Selected", width=12)
bt1.grid(row=5, column=3)


# def delete_command():
#     print(selectedBook)
#     print(selectedBook[0])
#     backend.delete(selectedBook[0])
#     view_command()
def delete_row():
    selected_row = list1.curselection()
    selected_row = int(selected_row[0])
    list1.delete(selected_row)


bt1 = Button(window, text="Delete Selected", width=12, command=delete_row)
bt1.grid(row=6, column=3)

bt1 = Button(window, text="Close", width=12, command=window.destroy)
bt1.grid(row=7, column=3)
view_command()
window.mainloop()
