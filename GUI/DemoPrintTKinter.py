from tkinter import *
from subprocess import call

def click():
    open_py_file()


def open_py_file():
    call(["python", "guifemo.py"])
   

window = Tk()
window.geometry("400x400")
button = Button(window, text="Click ME")
button.config(command=click)
button.pack()
window.mainloop()