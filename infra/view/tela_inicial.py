#coding: utf-8
#author: Lário dos Santos Diniz
__author__ = "Lário dos Santos Diniz"

import os

from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color
from kivy.graphics import Rectangle

from kivy.lang import Builder
from kivy.utils import get_color_from_hex

from infra.regras.lista_arquivos import listarArquivos

from infra.view.area_titulo import AreaTitulo
from infra.view.area_data import AreaData
from infra.view.area_calendario import AreaCalendario


class TelaInicial(BoxLayout):  
    def __init__(self, **kwargs):
        super(TelaInicial, self).__init__(**kwargs) 
            

path = os.getcwd()

kv_path = path+'\\infra\\view\\kv'
kvs = listarArquivos(".kv", kv_path)

for kv in kvs:    
    Builder.load_file(kv_path+"\\"+kv)  
      
       