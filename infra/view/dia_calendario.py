# coding: utf-8
from datetime import date

from kivy.app import App
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex


from infra.controller.data import Data


class DiaCalendario(Button):
    """Classe que cria os botões de cada dia do calentario"""

    def on_press(self):
        self.aplicacao.dataSelecionada.define_dia(int(self.dia))
        prop = self.aplicacao.property('dataSelecionada')
        prop.dispatch(self.aplicacao)

    def __init__(self, fim_de_semana, **kwargs):

        super(DiaCalendario, self).__init__(**kwargs)
        self.aplicacao = App.get_running_app()
        self.dia = "0"
        self.fim_de_semana = fim_de_semana
        self.define_dia

    def pinta_dia_selecionado(self):
        diaSelecionado = self.aplicacao.dataSelecionada.dia_numero_mes
        if self.dia == diaSelecionado:
            self.bold = True
            self.color = get_color_from_hex("#3385ff")
            self.background_color = get_color_from_hex("#FFFFFF")

    def define_cor(self):
        self.color = get_color_from_hex("#000000")
        self.bold = False

        hoje = self.aplicacao.dataAtual.dia_numero_mes
        mesAtual = self.aplicacao.dataAtual.mes_nome
        mesSelecionado = self.aplicacao.dataSelecionada.mes_nome
        anoSelecionado = int(self.aplicacao.dataSelecionada.ano)
        anoAtual = int(self.aplicacao.dataAtual.ano)

        if ((self.dia == hoje) and
           (mesSelecionado == mesAtual) and
           (anoAtual == anoSelecionado)):
            self.underline = True

        if self.dia in ['1', '8', '15', '22']:
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

        if self.fim_de_semana is True:
            self.markup = True
            self.text = self.dia + "[sup] F[/sup]"

        self.pinta_dia_selecionado()

    def define_dia(self, dia):
        self.text = str(dia)
        self.dia = str(dia)
        self.define_cor()

__author__ = "Lário dos Santos Diniz"
