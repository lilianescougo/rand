import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import random

class NumeroAleatorio(App):
    def build(self):
        rand = random.randint(1, 100)
        label = Label(text=str(rand), font_size=50)

        layout = BoxLayout(orientatio="vertical")
        layout.add_widget(label)

        return layout

if _name_ == '_main_':
    NumeroAleatorioApp().run()