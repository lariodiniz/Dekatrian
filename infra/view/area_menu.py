# coding: utf-8
from datetime import date

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex
from kivy.uix.label import Label

from infra.regras.data import Data

from infra.view.tela_dekatrian import TelaDekatrian
from infra.view.tela_inicial import TelaInicial
from infra.view.tela_desenvolvimento import TelaDesenvolvimento


class AreaMenu(BoxLayout):
    """Classe que define a area que mostra o menu."""

    def __init__(self, **kwargs):
        super(AreaMenu, self).__init__(**kwargs)
        self.aplicacao = App.get_running_app()

    def on_press_dekatrian(self):
        self.aplicacao.mudarTela(TelaDekatrian)

    def on_press_calendario(self):
        self.aplicacao.mudarTela(TelaInicial)        

    def on_press_desenvolvimento(self):
        self.aplicacao.mudarTela(TelaDesenvolvimento)
        

__author__ = "Lário dos Santos Diniz"
