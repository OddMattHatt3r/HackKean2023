from tkinter import *
from tkinter import simpledialog
import tkinter as tk
from tkinter.ttk import *
import binascii

root = Tk()

btn = Button (root, text = 'Exit',
              command = root.destroy)
btn.pack( side = 'bottom')


def display_text():
   global entry
   string= entry.get()
   res = []
   for ele in string:
       res.extend(ord(num) for num in ele)
       label.configure(text=res)

def display_text2():
    global entry
    string= entry.get()
    res = []
    for ele in string:
       res.extend(ord(num) for num in ele)
       label.configure(text=res)

#Initialize a Label to display the User Input
label=Label(root, text="", font=("Courier 22 bold"))
label.pack()
entry= Entry(root, width= 40)
entry.focus_set()
entry.pack()

# This button will initialize
# the progress bar
button = Button(root, text = 'Send', command = lambda: [display_text(), display_text2()])
button.pack()
                                
menu = Menu(root)
w = Label(root, text ='Quantum Calculator', font = "50") 
w.pack()
  


root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='Window', menu=filemenu)
filemenu.add_command(label='Sent')
filemenu.add_command(label='Recieved...')
filemenu.add_separator()

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')




mainloop()
