# coding: utf-8
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color
from kivy.graphics import Rectangle


from kivy.utils import get_color_from_hex


from infra.view.area_titulo import AreaTitulo
from infra.view.area_data import AreaData
from infra.view.area_calendario import AreaCalendario


class TelaInicial(BoxLayout):
    def __init__(self, **kwargs):
        super(TelaInicial, self).__init__(**kwargs)

__author__ = "Lário dos Santos Diniz"
