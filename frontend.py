from tkinter import *
import db_backend as db_backend

def get_selected_row(event):
    try:
        index=listMain.curselection()[0]
        selected_tuple = listMain.get(index)
        pNameText.delete(0, END)
        pNameText.insert(END, selected_tuple[1])
        pXpVal.delete(0, END)
        pXpVal.insert(END, selected_tuple[2])
        pHPVal.delete(0, END)
        pHPVal.insert(END, selected_tuple[3])
        pGoldVal.delete(0, END)
        pGoldVal.insert(END, selected_tuple[4])
        pDmgVal.delete(0, END)
        pDmgVal.insert(END, selected_tuple[5])
    except IndexError:
        pass

def viewCommand():
    listMain.delete(0,END)
    for row in db_backend.view():
        listMain.insert(END, row)

def searchPatrons():
    listMain.delete(0,END)
    for row in db_backend.search(patronName.get(),patronXp.get(),patronHP.get(),patronGold.get(),patronDmg.get()):
        listMain.insert(END, row)

def addPatron():
    db_backend.insert(patronName.get(),patronXp.get(),patronHP.get(),patronGold.get(),patronDmg.get())
    listMain.delete(0, END)
    listMain.insert(END,(patronName.get(),patronXp.get(),patronHP.get(),patronGold.get()),patronDmg.get())

def updatePatron():
    index=listMain.curselection()[0]
    selected_tuple = listMain.get(index)
    db_backend.update(selected_tuple[0],patronName.get(),patronXp.get(),patronHP.get(),patronGold.get(),patronDmg.get())

def deletePatron():
    index=listMain.curselection()[0]
    selected_tuple = listMain.get(index)
    db_backend.delete(selected_tuple[0])

window = Tk()
window.title("Database")

pName = Label(window, text="Name")
pName.grid(row = 0, column = 0)

pXp = Label(window, text="Xp")
pXp.grid(row = 1, column = 0)

pHP = Label(window, text="HP")
pHP.grid(row = 1, column = 2)

pGold = Label(window, text="Gold")
pGold.grid(row = 2, column = 0)

pDmg = Label(window, text="Damage")
pDmg.grid(row=2, column=2)

patronName = StringVar()
pNameText = Entry(window, textvariable=patronName)
pNameText.grid(row=0, column=1, columnspan=3)

patronXp = IntVar()
pXpVal = Entry(window, textvariable=patronXp)
pXpVal.grid(row=1, column=1)

patronHP = IntVar()
pHPVal = Entry(window, textvariable=patronHP)
pHPVal.grid(row=1, column=3)

patronGold = IntVar()
pGoldVal = Entry(window, textvariable=patronGold)
pGoldVal.grid(row=2, column=1)

patronDmg = IntVar()
pDmgVal = Entry(window, textvariable=patronDmg)
pDmgVal.grid(row=2, column=3)

listMain = Listbox(window, height=10, width=35)
listMain.grid(row=3, column=0, rowspan=8, columnspan=2)
listMain.delete(0,END)
for row in db_backend.view():
    listMain.insert(END, row)

yScroll = Scrollbar(window)
yScroll.grid(row=3, column=2, rowspan=6)

listMain.configure(yscrollcommand=yScroll.set)
yScroll.configure(command=listMain.yview)

listMain.bind('<<ListboxSelect>>', get_selected_row)

bViewAll = Button(window, text="View All", width=12, command=viewCommand)
bViewAll.grid(row=3, column= 3)

bSearch = Button(window, text="Search", width=12, command=searchPatrons)
bSearch.grid(row=4, column= 3)

bNew = Button(window, text="New", width=12, command=addPatron)
bNew.grid(row=5, column= 3)

bUpdate = Button(window, text="Update", width=12, command=updatePatron)
bUpdate.grid(row=6, column= 3)

bDelete = Button(window, text="Delete", width=12, command=deletePatron)
bDelete.grid(row=7, column= 3)

bClose = Button(window, text="Close", width=12, command=window.destroy)
bClose.grid(row=8, column= 3)

window.mainloop()