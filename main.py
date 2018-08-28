# coding: utf-8
import os
import kivy
import platform as plataforma


from datetime import date

from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.lang import Builder
from kivy.utils import platform
from kivy.uix.button import Button

from infra.view.tela_inicial import TelaInicial
from infra.regras.data import Data

from infra.view.area_menu import AreaMenu

kivy.require('1.9.1')


class DekatrianApp(App):
    """Classe Principal da Aplicação"""

    dataAtual = ObjectProperty(Data(date.today()))
    dataSelecionada = ObjectProperty(Data(date.today()))
    tela = ObjectProperty(str())

    def __init__(self, **kwargs):
        self._configuracaoInicial()
        super(DekatrianApp, self).__init__(**kwargs)        
        self._carregaKv()

    def _configuracaoInicial(self):
        Config.set('graphics', 'resizable', 0)
        Config.set('kivy', 'window_icon', 'img/icon.png')
        Window.clearcolor = get_color_from_hex("#B0C4DE")
        if platform != 'android':
            Window.size = (360, 640)

    def _defineBarra(self):
        if plataforma.system() == 'Windows':
            return '\\'
        else:
            return '/'

    def _carregaKv(self):

        b = self._defineBarra()
        path = os.path.dirname(os.path.abspath(__file__))
        kv_path = path+b+'infra'+b+'view'+b+'kv'
        kvs = self._listarArquivos(".kv", kv_path)

        for kv in kvs:
            Builder.load_file(kv_path+b+kv)

    def _listarArquivos(self, ext, path):
        """Lista todos os arquivos que estão em um diretório com a extencao 
        definida"""

        b = self._defineBarra()
        caminhos = [os.path.join(path, nome) for nome in os.listdir(path)]
        arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
        arqFiltrados = [arq for arq in arquivos if arq.lower().endswith(ext)]
        return [arq.split(b)[-1] for arq in arqFiltrados]

    def build(self):

        self.icon = 'img/icon.png'
        self.title = 'Calendario Dekatrian'
        self.tela = TelaInicial()
        self.telaSecundaria = Button()
        return self.tela

    def mudarTela(self, tela):
        self.root_window.remove_widget(self.tela)
        self.tela = tela()
        self.root_window.add_widget(self.tela)

    def mudarTelaSecundaria(self, tela):
        self.tela.ids.tela_secundaria.remove_widget(self.telaSecundaria)
        self.telaSecundaria = tela()     
        self.tela.ids.tela_secundaria.add_widget(self.telaSecundaria)


if __name__ in ('__android__', '__main__'):

    janela = DekatrianApp()
    janela.run()

__version__ = '0.0.1'
__author__ = "Lário dos Santos Diniz"
