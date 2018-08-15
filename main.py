#coding: utf-8
#author: Lário dos Santos Diniz
__author__ = "Lário dos Santos Diniz"
__version__ = "0.1.0"

import kivy
#define a versão minima da aplicação kivy
kivy.require('1.9.1')

from kivy.app import App

from kivy.core.window import Window

from kivy.utils import get_color_from_hex
Window.clearcolor = get_color_from_hex("#B0C4DE")

from infra.view.tela_inicial import TelaInicial

from kivy.properties import ObjectProperty
from kivy.lang import Builder


kv_path = ''
kv = 'Dekatrian.kv'

class DekatrianApp(App):    

    def build(self):        
        self.icon = 'img/logo.png' 
        self.title = 'Calendario Dekatrian'         
        self.tela = TelaInicial()
        return self.tela     

if __name__ == '__main__':
    janela = DekatrianApp()    
    janela.run()