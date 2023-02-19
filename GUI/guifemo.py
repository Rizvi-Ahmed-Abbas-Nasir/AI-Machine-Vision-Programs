import pyttsx3
from tkinter import *
import subprocess, time
import threading
import HandTrackingModule




window = Tk()

def click():
   gc = HandTrackingModule.main()
   t = threading.Thread(target=gc.start)
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



window.geometry("400x400")
button = Button(window, text="Click ME",command=threading.Thread(target=click).start)
button.pack()
window.mainloop()