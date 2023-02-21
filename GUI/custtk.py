import threading
import tkinter

import PIL
import customtkinter as ctk
from PIL import ImageTk
from PIL.Image import Image
from PIL.ImageTk import PhotoImage
import HandTrackingModule

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
app = ctk.CTk(fg_color="#222222")  # create CTk window like you do with the Tk window
image = PIL.Image.open("logo2.png")
icon = ImageTk.PhotoImage(image)
app.columnconfigure(0, weight=1)
app.title("AI Machine Vision")
app.geometry("1000x600")

notebook = ctk.CTkTabview(app, width=1000, height=580, corner_radius=8 , fg_color="#29292a") # 262628 alternate Color
notebook.add(" Home ")
notebook.add(" Desktop Controller ")
notebook.add(" Tranier ")
notebook.add(" VirtualKeyboard ")
notebook.grid(padx=10, pady=10)
notebook._segmented_button.grid(sticky="W")

button_1 = ctk.CTkButton(notebook.tab(" Home "))
button_1.pack()

#
# def button_function():
#     g = HandTrackingModule.main()
#     t = threading.Thread(target=g.start)
#     t.start()


# Use CTkButton instead of tkinter Button
# button = ctk.CTkButton(master=app, text="Start", command=button_function)
# button2 = ctk.CTkButton(master=app, text="Closed", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
# button2.pack()

app.mainloop()
