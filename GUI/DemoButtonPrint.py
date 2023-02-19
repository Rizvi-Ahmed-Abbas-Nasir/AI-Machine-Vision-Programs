from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from subprocess import call



class WidgetsEample(GridLayout):
    counter=0
    press_property=StringProperty("Default")

    def on_press_button(self):
        self.open_py_file()
        print("Button is Pressed")
        self.counter+=1
        self.press_property = str(self.counter)

    def open_py_file(self):
        call(["python", "HandTrackingModule.py"])



class DemoApp(App):
    pass


DemoApp().run()
