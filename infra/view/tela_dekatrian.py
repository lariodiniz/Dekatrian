# coding: utf-8
__author__ = "Lário dos Santos Diniz"


from infra.view.tela import Tela


class TelaDekatrian(Tela):


    def __init__(self, **kwargs):
        self.nome = 'TelaDekatrian'
        self.title='Informações Dekatrian'
        self.texto = Texto()
        super(TelaDekatrian, self).__init__(**kwargs)


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
