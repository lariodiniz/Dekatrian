#coding: utf-8

__author__ = "Lário dos Santos Diniz"

"""
Data de Criação: 25/07/2018
"""

from entidade_de_tempo import EntidadeDeTempo

class Dia(EntidadeDeTempo):   

    @staticmethod
    
    
    def __init__(self, numero, nome):
        self.nome = nome
        self.numero = numero
    
    



if __name__ == "__main__":
    dia = Dia(0,)
    print(dia.nome)
    