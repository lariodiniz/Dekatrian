# coding: utf-8
from datetime import date, datetime

from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

from infra.view.ano_calendario import AnoCalendario
from infra.controller.data import Data


class AreaAnos(StackLayout):
    """Classe que monta a tela de Anos"""

    def __init__(self, **kwargs):
        super(AreaAnos, self).__init__(**kwargs)
        self.aplicacao = App.get_running_app()
        self.monta_anos()

    def monta_anos(self):
        anoAtual = int(self.aplicacao.dataAtual.ano)
        anoSelecionado = int(self.aplicacao.dataSelecionada.ano)
        for numeroAno in range(anoSelecionado-4, anoSelecionado+8):
            ano = AnoCalendario(str(numeroAno))
            if numeroAno == anoAtual:
                ano.background_color = get_color_from_hex("#DDDDDD")
            self.add_widget(ano)

__author__ = "Lário dos Santos Diniz"
