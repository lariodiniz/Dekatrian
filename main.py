# coding: utf-8
import os
import kivy


from datetime import date

from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.logger import Logger

from infra.view.tela_inicial import TelaInicial
from infra.regras.data import Data
from infra.regras.carrega_kv import CarregaKV

from infra.view.area_menu import AreaMenu

kivy.require('1.9.1')
Config.set('graphics', 'resizable', 0)
Config.set('kivy', 'window_icon', 'img/icon.png')
Window.clearcolor = get_color_from_hex("#B0C4DE")
Window.size = (360, 640)

class DekatrianApp(App):
    """Classe Principal da Aplicação"""

    dataAtual = ObjectProperty(Data(date.today()))
    dataSelecionada = ObjectProperty(Data(date.today()))
    tela = ObjectProperty(str())

    def __init__(self, **kwargs):
        super(DekatrianApp, self).__init__(**kwargs)

    def build(self):

        CarregaKV()
        self.icon = 'img/icon.png'
        self.title = 'Calendario Dekatrian'
        self.tela = 'Calendario'
        return TelaInicial()

    def on_start(self):
        Logger.info('App: Aplicação Iniciada!')

    def on_stop(self):
        Logger.info('App:  Aplicação Finalizada')


if __name__ in ('__android__', '__main__'):

    janela = DekatrianApp()
    janela.run()

__version__ = "0.0.1"
__author__ = "Lário dos Santos Diniz"
