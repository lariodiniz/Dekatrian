# coding: utf-8
__author__ = "Lário dos Santos Diniz"


from infra.view.area_titulo import AreaTitulo
from infra.view.area_data import AreaData
from infra.view.area_calendario import AreaCalendario
from infra.view.tela import Tela


class TelaInicial(Tela):

    def __init__(self, **kwargs):
        self.nome = 'TelaInicial'
        self.title = 'Calendário'
        super(TelaInicial, self).__init__(**kwargs)
