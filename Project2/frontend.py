from tkinter import *

import backend


def view_command():
    for row in backend.view():
        list1.insert(END, row)


def delete_command():  # To delete all the data from database, you have to run again after clicking on Delete
    backend.delete_database()


def upload():
    statusvar.set("Busy..")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready")


root = Tk()
root.wm_title("Database Intrecting Project")
canvas = Canvas(root, height=400, width=800)
canvas.pack()

frame = Frame()
frame.place(relx=0.3, rely=0.1, relwidth=0.8, relheight=0.8)

list1 = Listbox(frame, height=20, width=60)
list1.grid(row=4, column=1, rowspan=5, columnspan=1)

sb1 = Scrollbar(frame)
sb1.grid(row=5, column=3, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# if you click on view all and not prints on listbox, please run connect function from backend to fetch data
try:
    b1 = Button(frame, text="VIEW ALL", width=7, bg='green', command=view_command)
    b1.grid(row=4, column=6)

    b3 = Button(frame, text="DELETE ", width=7, bg='red', command=delete_command)
    b3.grid(row=6, column=6)

    b4 = Button(frame, text="CLOSE", width=7, bg='blue', command=root.destroy)
    b4.grid(row=7, column=6)

except Exception as E:
    print("Error :", E)

statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)

root.mainloop()
