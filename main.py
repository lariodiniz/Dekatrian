#coding: utf-8
#author: Lário dos Santos Diniz
__author__ = "Lário dos Santos Diniz"

import kivy
#define a versão minima da aplicação kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
Window.clearcolor = get_color_from_hex("#B0C4DE")


from infra.view.tela_inicial import TelaInicial

class DekatrianApp(App):    
    pass
   #def build(self):
   #    return TelaInicial()
    

if __name__ == '__main__':
    janela = DekatrianApp()
    janela.run()