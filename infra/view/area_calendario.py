# coding: utf-8
from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label

from infra.view.dia_calendario import DiaCalendario
from infra.regras.dia import Dia


class AreaCalendario(StackLayout):
    """Classe que monta o calendario da Aplicação"""

    def __init__(self, **kwargs):
        super(AreaCalendario, self).__init__(**kwargs)
        self.diasDoCalendario = []
        self.aplicacao = App.get_running_app()
        self.aplicacao.bind(dataSelecionada=self.mudouDataSelecionada)
        self.monta_calendario()

    def monta_calendario(self):

        if self.aplicacao.dataSelecionada.mes_nome != 'Sem Mes':
            for nomeDaSemana in Dia.nomes():
                nomeSemana = Label()
                nomeSemana.text = nomeDaSemana
                nomeSemana.size_hint = (.1428, .2)
                self.add_widget(nomeSemana)

            for dia in range(1, 29):
                diaC = DiaCalendario()
                diaC.define_dia(dia)
                self.diasDoCalendario.append(diaC)
                self.add_widget(diaC)
        else:
            diaForaDoCalendario = Label()
            diaForaDoCalendario.text = self.aplicacao.dataSelecionada.dia_nome
            diaForaDoCalendario.size_hint = (1, 1)
            self.add_widget(diaForaDoCalendario)

        self.defineCores()

    def mudouDataSelecionada(self, app, classMudou):
        self.defineCores()

    def defineCores(self):

        for dia in self.diasDoCalendario:
            dia.define_cor()

__author__ = "Lário dos Santos Diniz"
