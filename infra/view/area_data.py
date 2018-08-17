# coding: utf-8
from datetime import date

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from infra.regras.data import Data


class AreaData(BoxLayout):
    """Classe que define a area que mostra as datas na aplicação."""

    def __init__(self, **kwargs):

        super(AreaData, self).__init__(**kwargs)

        aplicacao = App.get_running_app()
        dataSelecionada = aplicacao.dataSelecionada

        self.dia = dataSelecionada.dia_numero_mes
        self.mes = dataSelecionada.mes_nome+" ("+dataSelecionada.mes_numero+")"
        self.ano = dataSelecionada.ano
        self.data = dataSelecionada.data

__author__ = "Lário dos Santos Diniz"
