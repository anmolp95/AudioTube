from Tkinter import *
def search():
    print "Hello"
def OnDouble(self, event):
    widget = event.widget
    selection=widget.curselection()
    value = widget.get(selection[0])
    print "selection:", selection, ": '%s'" % value
def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print 'You selected item %d: "%s"' % (index, value)
master = Tk()
Label(master, text="Search").grid(row=0,column=0)
e1 = Entry(master,width=60)
e1.grid(row=0, column=1)
Button(master, text='Search', command=search).grid(row=1, column=2, sticky=E, pady=4)
lb=Listbox(master,height=30, width=60)
str="hello"+"\\n"+"gig"
lb.insert(END,str)
lb.insert(END,"Hi")
lb.insert(END,"This")
lb.bind('<Double-Button-1>', onselect)
lb.grid(row=1,column=0)
mainloop( )
