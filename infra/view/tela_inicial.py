# coding: utf-8

import os

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.properties import ObjectProperty

from kivy.app import App

from kivy.utils import get_color_from_hex

from infra.view.area_titulo import AreaTitulo
from infra.view.area_data import AreaData
from infra.view.area_calendario import AreaCalendario


class TelaInicial(Screen):
    telaSecundaria = ObjectProperty(None)
    nome = 'TelaInicial'

    def __init__(self, **kwargs):
        self.aplicacao = App.get_running_app()
        
        #self.background = self.aplicacao.pasta_imagens+'background.png'
        super(TelaInicial, self).__init__(**kwargs)


__author__ = "Lário dos Santos Diniz"
