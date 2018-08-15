#coding: utf-8
#author: Lário dos Santos Diniz
__author__ = "Lário dos Santos Diniz"

from datetime import date

from kivy.uix.boxlayout import BoxLayout

from infra.regras.data import Data

class AreaData(BoxLayout):
    
    def __init__(self, **kwargs):
        super(AreaData, self).__init__(**kwargs)
        data = Data(date.today())
        self.dia = data.dia_numero_mes 
        self.mes = data.mes_nome+" ("+data.mes_numero+")"
        self.ano = data.ano
        self.data = data.data
        