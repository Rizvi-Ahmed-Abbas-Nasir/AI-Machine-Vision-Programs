import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.title("GUI")



frame=[[],[],[]]
frame[0]= customtkinter.CTkFrame(app,width=200,height=200)
frame[0].grid(row=0, column=0,padx=5,pady=5,sticky="nsew")
frame[1]= customtkinter.CTkFrame(app,width=200,height=200)
frame[1].grid(row=0, column=1,padx=5,pady=5,sticky="nsew")
frame[2]= customtkinter.CTkFrame(app,width=200,height=200)
frame[2].grid(row=0, column=2,padx=5,pady=5,sticky="nsew")

hhh=[[],[]]

hhh[0]= customtkinter.CTkFrame(frame[1],fg_color="transparent")
hhh[0].grid(row=0, column=0,sticky=tkinter.W)
hhh[1]= customtkinter.CTkFrame(frame[1],fg_color="transparent")
hhh[1].grid(row=0, column=1)

logo = customtkinter.CTkLabel(hhh[0], font=customtkinter.CTkFont(family="Microsoft JhengHei",size=15, weight="bold"))#標題
logo.grid(row=0, column=0)

app.mainloop()