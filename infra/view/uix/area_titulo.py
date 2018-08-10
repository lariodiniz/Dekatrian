#coding: utf-8
#author: Lário dos Santos Diniz
__author__ = "Lário dos Santos Diniz"

from kivy.uix.floatlayout import FloatLayout

from kivy.properties import ObjectProperty
from kivy.lang import Builder

kv_path = 'infra/view/uix/'
kv = 'areatitulo.kv'


class AreaTitulo(FloatLayout):
    display = ObjectProperty()
    def __init__(self, **kwargs):
        super(AreaTitulo, self).__init__(**kwargs)
        self.titulo = "[b]Dekatrian[/b]"
        Builder.load_file(kv_path+kv)