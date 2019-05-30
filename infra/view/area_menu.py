# coding: utf-8
from datetime import date

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class AreaMenu(BoxLayout):
    """Classe que define a area que mostra o menu."""

    def __init__(self, **kwargs):
        self.aplicacao = App.get_running_app()
        self.img_dekatrian = self.aplicacao.pasta_imagens+'report.png'
        self.img_calendario = self.aplicacao.pasta_imagens+'calendar.png'
        self.img_desenvolvimento = self.aplicacao.pasta_imagens+'resume.png'
        super(AreaMenu, self).__init__(**kwargs)

    def on_press_dekatrian(self):
        self.aplicacao.mudarTela(self.aplicacao.tela_dekatrian)

    def on_press_calendario(self):
        self.aplicacao.mudarTela(self.aplicacao.tela_inicial)

    def on_press_desenvolvimento(self):
        self.aplicacao.mudarTela(self.aplicacao.tela_desenvolvimento)


__author__ = "Lário dos Santos Diniz"
