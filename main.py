# coding: utf-8
import os
import kivy


from datetime import date

from kivy.app import App
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty
from kivy.config import Config
from kivy.lang import Builder

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
        Window.size = (360, 640)

    def _carregaKv(self):
        path = os.path.dirname(os.path.abspath(__file__))

        kv_path = path+'\\infra\\view\\kv'
        kvs = self._listarArquivos(".kv", kv_path)

        for kv in kvs:
            Builder.load_file(kv_path+"\\"+kv)

    def _listarArquivos(self, ext, path):
        """Lista todos os arquivos que estão em um diretório com a extencao 
        definida"""

        caminhos = [os.path.join(path, nome) for nome in os.listdir(path)]
        arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
        arqFiltrados = [arq for arq in arquivos if arq.lower().endswith(ext)]
        return [arq.split('\\')[-1] for arq in arqFiltrados]   

    def build(self):

        self.icon = 'img/icon.png'
        self.title = 'Calendario Dekatrian'
        self.tela = 'Calendario'
        return TelaInicial()

if __name__ in ('__android__', '__main__'):

    janela = DekatrianApp()
    janela.run()

__version__ = "0.0.1"
__author__ = "Lário dos Santos Diniz"
