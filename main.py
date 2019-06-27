# coding: utf-8

__version__ = '1.0.0'
__author__ = "Lário dos Santos Diniz"

import os
import kivy
from os.path import abspath, dirname
import platform as plataforma


from datetime import date

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.lang import Builder
from kivy.utils import platform
from kivy.uix.button import Button

from infra.view.tela_inicial import TelaInicial
from infra.view.tela_desenvolvimento import TelaDesenvolvimento
from infra.view.tela_dekatrian import TelaDekatrian

from infra.controller.data import Data

from infra.view.area_menu import AreaMenu

kivy.require('1.9.1')

def defineBarra():
    if plataforma.system() == 'Windows':
        return '\\'
    else:
        return '/'

barra = defineBarra()
os.environ['KIVY_DATA_DIR'] = abspath(dirname(__file__)) + barra+'img'
print(os.environ['KIVY_DATA_DIR'])


class DekatrianApp(App):
    """Classe Principal da Aplicação"""

    dataAtual = ObjectProperty(Data(date.today()))
    dataSelecionada = ObjectProperty(Data(date.today()))
    tela = ObjectProperty(str())

    def __init__(self, version, **kwargs):
        self.version = version
        self._configuracaoInicial()
        self._carregaKv()
        super(DekatrianApp, self).__init__(**kwargs)
        self._telas = [TelaInicial(), TelaDekatrian(), TelaDesenvolvimento()]

    def _configuracaoInicial(self):

        self.barra = defineBarra()
        self.pasta_projeto = os.path.dirname(os.path.abspath(__file__))
        self.pasta_imagens = self.pasta_projeto+self.barra+'img'+self.barra

        Config.set('graphics', 'resizable', 0)
        Config.set('kivy', 'window_icon', self.pasta_imagens + 'icon.png')
        #Window.clearcolor = get_color_from_hex("#B0C4DE")
        if platform != 'android':
            Window.size = (360, 640)


    def _carregaKv(self):

        kv_path = self.pasta_projeto+self.barra+'infra'+self.barra+'view'
        kvs = self._listarArquivos(".kv", kv_path)

        for kv in kvs:
            Builder.load_file(kv_path+self.barra+kv)

    def _listarArquivos(self, ext, path):
        """Lista todos os arquivos que estão em um diretório
        com a extencao definida"""

        caminhos = [os.path.join(path, nome) for nome in os.listdir(path)]
        arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
        arqFiltrados = [arq for arq in arquivos if arq.lower().endswith(ext)]
        return [arq.split(self.barra)[-1] for arq in arqFiltrados]

    def build(self):

        self.icon = 'img/icon.png'
        self.title = 'Calendario Dekatrian'
        self.tela = TelaInicial()
        self.telaSecundaria = Button()
        self.gerenciador = ScreenManager()
        self.gerenciador.switch_to(self._telas[0])
        return self.gerenciador

    def mudarTela(self, tela):
        if self.gerenciador.current_screen != self._telas[tela]:
            if tela == 0:
                self.gerenciador.transition.direction = 'right'
            else:
                self.gerenciador.transition.direction = 'left'
            self.gerenciador.switch_to(self._telas[tela])       

    def mudarTelaSecundaria(self, tela):
        self.gerenciador.current_screen.ids.tela_secundaria.remove_widget(self.telaSecundaria)
        self.telaSecundaria = tela()
        self.gerenciador.current_screen.ids.tela_secundaria.add_widget(self.telaSecundaria)

    @property
    def tela_inicial(self):
        return 0

    @property
    def tela_dekatrian(self):
        return 1

    @property
    def tela_desenvolvimento(self):
        return 2

if __name__ in ('__android__', '__main__'):

    janela = DekatrianApp(__version__)
    janela.run()
