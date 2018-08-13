#coding: utf-8
#author: Lário dos Santos Diniz
__author__ = "Lário dos Santos Diniz"

from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

from kivy.properties import ObjectProperty
from kivy.lang import Builder

kv_path = 'infra/view/uix/'
kv = 'diacalendario.kv'


class DiaCalendario(Button):
    display = ObjectProperty()

    def on_press(self):
        print(self.dia)

    def __init__(self, **kwargs):
        super(DiaCalendario, self).__init__(**kwargs) 
        self.dia = "0"
        Builder.load_file(kv_path+kv)
    
    def _define_cor(self):
        if self.dia in ['1','8','15','22']:
            self.background_color =get_color_from_hex("#FF0000")
        elif self.dia in ['2','9','16','23']:
            self.background_color = get_color_from_hex("#FFA500")
        elif self.dia in ['3','10','17','24']:
            self.background_color = get_color_from_hex("#FFFF00")
        elif self.dia in ['4','11','18','25']:
            self.background_color = get_color_from_hex("#00FA9A")
        elif self.dia in ['5','12','19','26']:
            self.background_color = get_color_from_hex("#87CEEB")
        elif self.dia in ['6','13','20','27']:
            self.background_color = get_color_from_hex("#7B68EE")
        elif self.dia in ['7','14','21','28']:
            self.background_color = get_color_from_hex("#FF1493")



    def define_dia(self, dia):
        self.text = str(dia)
        self.dia = str(dia)
        self._define_cor()

        


