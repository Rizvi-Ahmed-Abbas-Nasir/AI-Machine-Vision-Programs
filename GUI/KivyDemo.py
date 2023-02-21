import threading

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.clock import Clock

import HandTrackingModule


class Sprite(Widget):
    pass


class RootWidget(Widget):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.submit = Button(text="Abbas")
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
        self.submit2 = Button(text="Exit")
        self.submit2.bind(on_press=self.terminatedPRO)
        self.add_widget(self.submit2)

    def press(self):
        print("Abbas")
        g = HandTrackingModule.main()
        t = threading.Thread(target=g.start)
        t.start()
    def terminatedPRO(self):
        g = HandTrackingModule.main()
        g.stop()

    def build(self):
        butt = Button(text="Click")
        butt.bind(on_press=self.press)  # dont use brackets while calling function
        return butt


class MyApp(App):
    def build(self):
        app = RootWidget()
        return app

if __name__=="__main__":
    MyApp().run()