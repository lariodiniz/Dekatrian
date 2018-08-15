#coding: utf-8
#author: Lário dos Santos Diniz
__author__ = "Lário dos Santos Diniz"

from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label

from infra.view.dia_calendario import DiaCalendario
from infra.regras.dia import Dia

class AreaCalendario(StackLayout):
    
    def __init__(self, **kwargs):
        super(AreaCalendario, self).__init__(**kwargs) 
        self.monda_calendario()       
        

    def monda_calendario(self):

        for nomeDaSemana in Dia.nomes():
            nomeSemana = Label()
            nomeSemana.text = nomeDaSemana
            nomeSemana.size_hint = (.1428, .2)
            self.add_widget(nomeSemana)

        for dia in range(1,29):            
            diaC = DiaCalendario()
            diaC.define_dia(dia)
               
            self.add_widget(diaC)
        


