from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_tuple
        index=listMain.curselection()[0]
        selected_tuple = listMain.get(index)
        pNameText.delete(0, END)
        pNameText.insert(END, selected_tuple[1])
        pExpVal.delete(0, END)
        pExpVal.insert(END, selected_tuple[2])
        pHPVal.delete(0, END)
        pHPVal.insert(END, selected_tuple[3])
        pGoldVal.delete(0, END)
        pGoldVal.insert(END, selected_tuple[4])
    except IndexError:
        pass

def viewCommand():
    listMain.delete(0,END)
    for row in backend.view():
        listMain.insert(END, row)

def searchPatrons():
    listMain.delete(0,END)
    for row in backend.search(patronName.get(),patronExp.get(),patronHP.get(),patronGold.get()):
        listMain.insert(END, row)

def addPatron():
    backend.insert(patronName.get(),patronExp.get(),patronHP.get(),patronGold.get())
    listMain.delete(0, END)
    listMain.insert(END,(patronName.get(),patronExp.get(),patronHP.get(),patronGold.get()))

def updatePatron():
    backend.update(selected_tuple[0],patronName.get(),patronExp.get(),patronHP.get(),patronGold.get())

def deletePatron():
    backend.delete(selected_tuple[0])

window = Tk()
window.title("Database")

pName = Label(window, text="Name")
pName.grid(row = 0, column = 0)

pExp = Label(window, text="Exp")
pExp.grid(row = 0, column = 2)

pHP = Label(window, text="HP")
pHP.grid(row = 1, column = 0)

pGold = Label(window, text="Gold")
pGold.grid(row = 1, column = 2)

patronName = StringVar()
pNameText = Entry(window, textvariable=patronName)
pNameText.grid(row=0, column=1)

patronExp = IntVar()
pExpVal = Entry(window, textvariable=patronExp)
pExpVal.grid(row=0, column=3)

patronHP = IntVar()
pHPVal = Entry(window, textvariable=patronHP)
pHPVal.grid(row=1, column=1)

patronGold = IntVar()
pGoldVal = Entry(window, textvariable=patronGold)
pGoldVal.grid(row=1, column=3)

listMain = Listbox(window, height=10, width=35)
listMain.grid(row=2, column=0, rowspan=8, columnspan=2)

yScroll = Scrollbar(window)
yScroll.grid(row=2, column=2, rowspan=4)

listMain.configure(yscrollcommand=yScroll.set)
yScroll.configure(command=listMain.yview)

bViewAll = Button(window, text="View All", width=12, command=viewCommand)
bViewAll.grid(row=2, column= 3)

bSearch = Button(window, text="Search", width=12, command=searchPatrons)
bSearch.grid(row=3, column= 3)

bNew = Button(window, text="New", width=12, command=addPatron)
bNew.grid(row=4, column= 3)

bUpdate = Button(window, text="Update", width=12, command=updatePatron)
bUpdate.grid(row=5, column= 3)

bDelete = Button(window, text="Delete", width=12)
bDelete.grid(row=6, column= 3)

bClose = Button(window, text="Close", width=12)
bClose.grid(row=7, column= 3)

window.mainloop()