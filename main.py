# coding: utf-8
import os
import kivy

from datetime import date


from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty

from infra.view.tela_inicial import TelaInicial
from infra.regras.data import Data
from infra.regras.carrega_kv import CarregaKV


kivy.require('1.9.1')
Window.clearcolor = get_color_from_hex("#B0C4DE")


class DekatrianApp(App):
    """Classe Principal da Aplicação"""

    dataAtual = ObjectProperty(Data(date.today()))
    dataSelecionada = ObjectProperty(Data(date.today()))

    def build(self):

        CarregaKV()
        self.icon = 'img/logo.png'
        self.title = 'Calendario Dekatrian'
        self.tela = TelaInicial()
        return self.tela


if __name__ == '__main__':

    janela = DekatrianApp()
    janela.run()

__version__ = "0.0.1"
__author__ = "Lário dos Santos Diniz"
