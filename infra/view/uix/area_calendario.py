#coding: utf-8
#author: Lário dos Santos Diniz
__author__ = "Lário dos Santos Diniz"

from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

from kivy.properties import ObjectProperty
from kivy.lang import Builder

kv_path = 'infra/view/uix/'
kv = 'areacalendario.kv'


class AreaCalendario(StackLayout):
    display = ObjectProperty()

    def on_press(self):
        self.add_widget(Button(text="Testando"))

    def __init__(self, **kwargs):
        super(AreaCalendario, self).__init__(**kwargs)        
        Builder.load_file(kv_path+kv)

        


