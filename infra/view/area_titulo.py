#coding: utf-8
#author: Lário dos Santos Diniz
__author__ = "Lário dos Santos Diniz"

from kivy.uix.floatlayout import FloatLayout

from kivy.properties import ObjectProperty
from kivy.lang import Builder


class AreaTitulo(FloatLayout):   

    titulo = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(AreaTitulo, self).__init__(**kwargs)
        self.titulo = "Dekatrian"
        
      