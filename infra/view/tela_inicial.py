#coding: utf-8
#author: Lário dos Santos Diniz
__author__ = "Lário dos Santos Diniz"

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from .uix.area_titulo import AreaTitulo
from .uix.area_data import AreaData
from .uix.area_calendario import AreaCalendario


kv_path = 'infra/view/'
kv = 'telainicial.kv'



class TelaInicial(BoxLayout):
    display = ObjectProperty()
    
    def __init__(self, **kwargs):
        super(TelaInicial, self).__init__(**kwargs)
        Builder.load_file(kv_path+kv)
    


