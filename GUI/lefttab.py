import customtkinter

app = customtkinter.CTk()
app._set_appearance_mode("dark")

app.columnconfigure(0, weight=1)
app.geometry("800x600")
notebook = customtkinter.CTkTabview(app, width=800, height=580)
notebook.add("Tab1")
notebook.add("Tab2")
notebook.grid(padx=10, pady=10)
notebook._segmented_button.grid(sticky="W")

app.mainloop()