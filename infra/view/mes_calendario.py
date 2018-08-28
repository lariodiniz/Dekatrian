# coding: utf-8
from datetime import date, datetime, timedelta


from kivy.app import App
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.uix.boxlayout import BoxLayout

from infra.regras.data import Data


class MesCalendario(Button):
    """Classe que cria os botões de cada mes do calentario"""

    def on_press(self):
        if self.text == 'Achronian':
            dataAtual = self.aplicacao.dataSelecionada.to_date

            d1 = datetime.strptime('{}-01-01'.format(dataAtual.year+1),
                                   '%Y-%m-%d')
            self.aplicacao.dataSelecionada = Data(d1)
        elif self.text == 'Sinchronian':
            dataAtual = self.aplicacao.dataSelecionada.to_date

            d1 = datetime.strptime('{}-01-02'.format(dataAtual.year+1),
                                   '%Y-%m-%d')
            self.aplicacao.dataSelecionada = Data(d1)
        else:
            self.aplicacao.dataSelecionada.define_mes(self.text)

        prop = self.aplicacao.property('dataSelecionada')
        prop.dispatch(self.aplicacao)
        self.aplicacao.mudarTelaSecundaria(BoxLayout)

    def __init__(self, nomeMes, **kwargs):

        super(MesCalendario, self).__init__(**kwargs)
        self.aplicacao = App.get_running_app()
        self.text = nomeMes
        self.size_hint = (.25, .25)
        self.define_cor()

    def define_cor(self):
        self.color = get_color_from_hex("#000000")
        self.bold = False

__author__ = "Lário dos Santos Diniz"
