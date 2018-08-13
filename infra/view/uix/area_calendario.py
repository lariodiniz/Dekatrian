#coding: utf-8
#author: Lário dos Santos Diniz
__author__ = "Lário dos Santos Diniz"

from kivy.uix.stacklayout import StackLayout

from infra.view.uix.dia_calendario import DiaCalendario


from kivy.properties import ObjectProperty
from kivy.lang import Builder


kv_path = 'infra/view/uix/'
kv = 'areacalendario.kv'


class AreaCalendario(StackLayout):
    display = ObjectProperty()
    
    def __init__(self, **kwargs):
        super(AreaCalendario, self).__init__(**kwargs)        
        
        self.monda_calendario()
        Builder.load_file(kv_path+kv)

    def monda_calendario(self):
        for dia in range(1,29):            
            diaC = DiaCalendario()
            diaC.define_dia(dia)            
            self.add_widget(diaC)
        


