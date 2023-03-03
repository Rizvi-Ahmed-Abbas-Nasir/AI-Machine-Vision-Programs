import tkinter
import tkinter.messagebox
import PIL
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = customtkinter.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.toplevel_window = None
        self.title("AI Machine Vision")
        self.geometry(f"{1100}x{580}")
        #Icon for TopLevel Window
        # self.after(201, lambda: self.iconbitmap("logo2.png"))

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # images
        ImageHome = customtkinter.CTkImage(dark_image=PIL.Image.open("AIExapmple.png"), size=(200, 200))  # Images

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Developers",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.open_toplevel,
                                                        text="Rizvi Ahmed Abbas")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event,
                                                        text="Saad Shaikh Mujab")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event,
                                                        text="Ubaid Mukadam")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # TabsView

        Pages = customtkinter.CTkTabview(self, width=895, height=565,
                                         fg_color=("#bdbdc1", "#29292a"), corner_radius=15)  # 262628 alternate Color
        Pages.add(" Home ")
        Pages.add(" Desktop Controller ")
        Pages.add(" Trainer ")
        Pages.add(" VirtualKeyboard ")
        Pages.add(" Presentation Controller ")
        Pages.place(x=190, y=3)
        Pages._segmented_button.grid(sticky="W")

        HomeLabel0 = customtkinter.CTkLabel(Pages.tab(" Home "), text="AI ",
                                            font=customtkinter.CTkFont(family="IBM Plex Sans", size=90),
                                            fg_color="white", text_color="black", corner_radius=10)
        HomeLabel0.place(x=50, y=46)

        HomeLabel1 = customtkinter.CTkLabel(Pages.tab(" Home "), text=" Machine Vision",
                                            font=customtkinter.CTkFont(family="IBM Plex Sans", size=30),
                                            corner_radius=10)
        HomeLabel1.place(x=155, y=78)


        HomeLabel2 = customtkinter.CTkLabel(Pages.tab(" Home "), text=" Diploma Final Year Project",
                                            font=customtkinter.CTkFont(family="IBM Plex Sans", size=40),
                                            corner_radius=0)
        HomeLabel2.place(x=5, y=280)

        HomeLabel3 = customtkinter.CTkLabel(Pages.tab(" Home "),
                                            text="An Artificial Intelligence (AI) All Computer Vision program "
                                                 "are Intergrated in one Appliaction ",
                                            font=customtkinter.CTkFont(family="IBM Plex Sans", size=19),
                                            corner_radius=0)
        HomeLabel3.place(x=15, y=350)

        # App Images
        # button_1 = customtkinter.CTkButton(Pages.tab(" Home "),
        #                                    corner_radius=100,
        #                                    image=ImageHome,
        #                                    text=" ",
        #                                    fg_color="#29292a",
        #                                    hover_color="#29292a")
        # button_1.place(x=0, y=300)

        # TextBox
        self.textbox = customtkinter.CTkTextbox(Pages.tab(" Home "), width=350,height=240)
        self.textbox.grid(row=0, column=1, padx=(500, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0","About This Project\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, "
                                                     "sed diam nonumy eirmod tempor invidunt ut labore et dolore "
                                                     "magna aliquyam erat, sed diam voluptua.\n\n")
        self.textbox.configure(state="disabled")  # configure textbox to be read-only



    # Methods
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
            self.toplevel_window.grab_set()



if __name__ == "__main__":
    app = App()
    app.mainloop()
