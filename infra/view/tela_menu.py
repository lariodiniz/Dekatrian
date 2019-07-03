# coding: utf-8
__author__ = "Lário dos Santos Diniz"

import os


from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.utils import get_color_from_hex
from kivy.properties import ObjectProperty


class TelaMenu(Screen):
    """Classe que define a area que mostra o menu."""
    
    nome = ObjectProperty('TelaMenu')
    title = ObjectProperty('Menu')

    def __init__(self, **kwargs):
        self.aplicacao = App.get_running_app()
        self.img_logo = self.aplicacao.pasta_imagens+'icon.png'
        self.img_dekatrian = self.aplicacao.pasta_imagens+'report.png'
        self.img_calendario = self.aplicacao.pasta_imagens+'calendar.png'
        self.img_desenvolvimento = self.aplicacao.pasta_imagens+'resume.png'
        super(TelaMenu, self).__init__(**kwargs)

    def on_press_dekatrian(self):
        self.aplicacao.mudarTela(self.aplicacao.tela_dekatrian)

    def on_press_calendario(self):
        self.aplicacao.mudarTela(self.aplicacao.tela_inicial)

    def on_press_desenvolvimento(self):
        self.aplicacao.mudarTela(self.aplicacao.tela_desenvolvimento)

    @property
    def text_dekatrian(self):
        return 'Informação Dekatrian'

    @property
    def text_desenvolvedor(self):
        return 'Informação Desenvolvedor'

    @property
    def text_label_calendario(self):
        return 'Calendário'

    @property
    def text_label_titulo(self):
        return 'Calendário Dekatrian'
