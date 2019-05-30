# coding: utf-8
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex

def Texto():
    
    return '''
Dekatrian e um calendario idealizado 
pelo integrante da equipe do podcast 
Scicast:

Roberto Spinelli.

Visite a pagina da Deviante ou o grupo 
do facebook do Calendario Dekatrian 
para saber mais.

[ref=http:////www.deviante.com.br//podcasts//scicast//]www.deviante.com.br//podcasts//scicast//[/ref]
'''

class TelaDekatrian(BoxLayout):

    def __init__(self, **kwargs):
        self.texto = Texto()
        super(TelaDekatrian, self).__init__(**kwargs)


__author__ = "Lário dos Santos Diniz"
