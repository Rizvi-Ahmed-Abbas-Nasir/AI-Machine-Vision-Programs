import threading
import tkinter

import customtkinter

import HandTrackingModule

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("800x600")


def button_function():
    g = HandTrackingModule.main()
    t = threading.Thread(target=g.start)
    t.start()


# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Start", command=button_function)
button2 = customtkinter.CTkButton(master=app, text="Closed", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
# button2.place(relx=0.5, rely=0.5, anchor=tkinter.LEFT)

app.mainloop()
