import gc

import pyttsx3
from tkinter import *
import subprocess, time
import threading
import HandTrackingModule
import Main

window = Tk()


def click():
   g = HandTrackingModule.main()
   t = threading.Thread(target=g.start)
   t.start()

def exitPro():
   g  = Main.main()
   t = threading.Thread(target=g.start)
   t.start()





def open_py_file():
   pass
   #call(["python", "HandTrackingModule.py"])
   # t1 = time.time()
   # p = subprocess.run(["python", "HandTrackingModule.py"])
   # p.terminate()
   # p.wait(500)
   # t2 = time.time()
   # print(t2 - t1)



window.geometry("900x600")
button = Button(window, text="Click ME",command=click)
#command=threading.Thread(target=click).start)
button2 = Button(window, text="Destory Me", command=exitPro)
button.pack()
button2.pack()
window.mainloop()