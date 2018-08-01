#coding: utf-8
#author: Lário dos Santos Diniz
__author__ = "Lário dos Santos Diniz"

from kivy.uix.boxlayout import BoxLayout


from ...RN.data import Data
from datetime import date

class LabelData(BoxLayout):
    def __init__(self, **kwargs):
        super(LabelData, self).__init__(**kwargs)
        data = Data(date.today())
        self.dia = data.dia_numero_mes 
        self.mes = data.mes_numero+" - "+data.mes_nome
        self.ano = data.ano
        self.data = data.data