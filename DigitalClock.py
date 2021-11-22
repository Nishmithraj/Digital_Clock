from tkinter import *
#from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Digital Clock")

def time():
    current_time = strftime("%I:%M:%S %p")
    lbl.config(text= current_time)
    lbl.after(200, time)


lbl = Label(root, font = ('calibri', 40, 'bold'), bg="black", fg="white")
lbl.grid(row=0, column =0,sticky=W+E)
Button(root, text ="Click here to Exit", bg="black",fg="grey", command=root.destroy, border=2).grid(row=3, column=0, sticky=W+E)

lbl2 = Label(root, text =strftime('%A %d %B %Y'), font = ('calibri', 15, 'bold'), bg="black", fg="white")
lbl2.grid(row=2, column =0,sticky=W+E)

time()

mainloop()