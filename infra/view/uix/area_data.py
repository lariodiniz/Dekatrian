#coding: utf-8
#author: Lário dos Santos Diniz
__author__ = "Lário dos Santos Diniz"

from kivy.uix.boxlayout import BoxLayout

from ...RN.data import Data
from datetime import date

class AreaData(BoxLayout):
    def __init__(self, **kwargs):
        super(AreaData, self).__init__(**kwargs)
        data = Data(date.today())
        self.dia = data.dia_numero_mes 
        self.mes = data.mes_nome+" ("+data.mes_numero+")"
        self.ano = data.ano
        self.data = "[i]"+data.data+"[/i]"