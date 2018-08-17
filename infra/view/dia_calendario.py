# coding: utf-8
from datetime import date

from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.app import App

from infra.regras.data import Data


class DiaCalendario(Button):
    """Classe que cria os botões de cada dia do calentario"""

    def on_press(self):

        print(self.dia)

    def __init__(self, **kwargs):

        super(DiaCalendario, self).__init__(**kwargs)
        self.dia = "0"
        self.define_dia

    def _define_cor(self):

        aplicacao = App.get_running_app()

        hoje = aplicacao.dataAtual.dia_numero_mes
        diaSelecionado = aplicacao.dataSelecionada.dia_numero_mes

        if self.dia == hoje:
            self.bold = True
            self.underline = True

        if self.dia == diaSelecionado:
            self.color = get_color_from_hex("#3385ff")
            self.background_color = get_color_from_hex("#FFFFFF")
        elif self.dia in ['1', '8', '15', '22']:
            self.background_color = get_color_from_hex("#ff6666")
        elif self.dia in ['2', '9', '16', '23']:
            self.background_color = get_color_from_hex("#ffa366")
        elif self.dia in ['3', '10', '17', '24']:
            self.background_color = get_color_from_hex("#ffff66")
        elif self.dia in ['4', '11', '18', '25']:
            self.background_color = get_color_from_hex("#8cff66")
        elif self.dia in ['5', '12', '19', '26']:
            self.background_color = get_color_from_hex("#668cff")
        elif self.dia in ['6', '13', '20', '27']:
            self.background_color = get_color_from_hex("#ff66ff")
        elif self.dia in ['7', '14', '21', '28']:
            self.background_color = get_color_from_hex("#b366ff")

    def define_dia(self, dia):
        self.text = str(dia)
        self.dia = str(dia)
        self._define_cor()

__author__ = "Lário dos Santos Diniz"
