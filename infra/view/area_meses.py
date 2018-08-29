# coding: utf-8
from datetime import date, datetime

from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

from infra.view.mes_calendario import MesCalendario
from infra.regras.meses import Mes
from infra.regras.data import Data


class AreaMeses(StackLayout):
    """Classe que monta a tela de Meses"""

    def __init__(self, **kwargs):
        super(AreaMeses, self).__init__(**kwargs)
        self.aplicacao = App.get_running_app()
        self.monta_meses()

    def monta_meses(self):
        mesAtual = self.aplicacao.dataAtual.mes_nome

        for nomeDoMes in Mes.nomes():
            mes = MesCalendario(nomeDoMes)
            if (nomeDoMes == mesAtual):
                mes.background_color = get_color_from_hex("#ADD8E6")

            self.add_widget(mes)

        mes = MesCalendario('Achronian')
        mes.background_color = get_color_from_hex("#FFD700")
        self.add_widget(mes)

        proximoAno = self.aplicacao.dataSelecionada.to_date.year+1
        if self._ehBissexto(proximoAno):
            mes = MesCalendario('Sinchronian')
            mes.background_color = get_color_from_hex("#DCDCDC")
            self.add_widget(mes)

    def _ehBissexto(self, ano):
        return (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0)

__author__ = "Lário dos Santos Diniz"
