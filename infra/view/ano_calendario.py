# coding: utf-8
from datetime import date, datetime, timedelta


from kivy.app import App
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.uix.boxlayout import BoxLayout

from infra.controller.data import Data


class AnoCalendario(Button):
    """Classe que cria os botões de cada ano do calentario"""

    def on_press(self):
        self.aplicacao.dataSelecionada.define_ano(self.text)

        prop = self.aplicacao.property('dataSelecionada')
        prop.dispatch(self.aplicacao)
        self.aplicacao.mudarTela(self.aplicacao.tela_inicial)

    def __init__(self, numeroAno, **kwargs):

        super(AnoCalendario, self).__init__(**kwargs)
        self.aplicacao = App.get_running_app()
        self.text = numeroAno
        self.size_hint = (.25, .25)
        self.define_cor()

    def define_cor(self):
        self.color = get_color_from_hex("#000000")
        self.bold = False

__author__ = "Lário dos Santos Diniz"
