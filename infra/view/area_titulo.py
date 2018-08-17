#coding: utf-8
#author: Lário dos Santos Diniz
__author__ = "Lário dos Santos Diniz"

from kivy.uix.floatlayout import FloatLayout

class AreaTitulo(FloatLayout):       
    
    def __init__(self, **kwargs):
        super(AreaTitulo, self).__init__(**kwargs)
        self.titulo = "Dekatrian"
        
      