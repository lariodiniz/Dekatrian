#coding: utf-8

__author__ = "Lário dos Santos Diniz"

"""
Data de Criação: 25/07/2018
"""

#from .entidade_de_tempo import EntidadeDeTempo


class Dia():   
    @staticmethod
    def nomes():
        return ('Rubia', 'Auria', 'Flavia', 'Virdia', 'Coria', 'India', 'Violeta')

    def __init__(self, numeroDoDia):        
        if (numeroDoDia == 0):
            self._numero_mes = 1
            self._numero_semana = 2
            self._nome = 'Achronian'
        elif (numeroDoDia == -1):            
            self._numero_mes = 2
            self._numero_semana = 2
            self._nome = 'Sinchronian'
        else:            
            self._numero_mes = numeroDoDia         
            self._numero_semana = (self.numero_mes % 7)
            if self._numero_semana == 0:
                self._numero_semana = 7

            self._nome = Dia.nomes()[self._numero_semana - 1]  


        self._dia_do_ano = 0

    @property
    def numero_mes(self):
        return self._numero_mes

    @property
    def numero_semana(self):
        return self._numero_semana

    @property
    def nome(self):
        return self._nome

    @property
    def dia_do_ano(self):
        return self._dia_do_ano
    
    @dia_do_ano.setter
    def dia_do_ano(self, valor):
        self._dia_do_ano = valor
        
    
    



if __name__ == "__main__":

    def testa_nomes_dos_dias():
        nomes = Dia.nomes()
        nomes_corretos = ('Rubia', 'Auria', 'Flavia', 'Virdia', 'Coria', 'India', 'Violeta')

        for n in [0,1,2,3,4,5,6]:
            if (nomes[n] != nomes_corretos[n]):
                print("Erro no nome da semana o dia",n+1," da semana deveria ser",nomes_corretos[n])
                print("Nome atual: ", nomes[n])
                break
            elif (n == 6):
                print("Sucesso ao testar os nomes da semana.")

    def testa_dia_Achronian():
        dia = Dia(0)
        if (dia.nome != 'Achronian'):
            print("Erro na classe dia, ao receber o parametro 0 o nome do dia deve ser Achronian")
            print("Nome atual: ", dia.nome)
        elif (dia.numero_mes == '1'):
            print("Erro na classe dia, ao receber o parametro 0 o numero do dia no mes deve do dia ser 1.")
            print("numero atual: ", dia.numero_mes)
        else:
            print("Sucesso ao testar dia Achronian")

    def testa_dia_Sinchronian():
        dia = Dia(-1)
        if (dia.nome != 'Sinchronian'):
            print("Erro na classe dia, ao receber o parametro -1 o nome do dia deve ser Sinchronian")
            print("Nome atual: ", dia.nome)
        elif (dia.numero_mes == '2'):
            print("Erro na classe dia, ao receber o parametro -1 o numero do dia no mes deve do dia ser 2.")
            print("numero atual: ", dia.numero_mes)
        else:
            print("Sucesso ao testar dia Sinchronian")

    def testa_dia_Semana():
        for n in range(1,29):
            dia = Dia(n)
            dia_da_semana = (n % 7)
            if dia_da_semana == 0:
                dia_da_semana = 7
            nome = Dia.nomes()[dia_da_semana - 1]
            if (dia.nome != nome):
                print("Erro na classe dia, ao receber o parametro",n,"o nome do dia deve ser", nome)
                print("Nome atual: ", dia.nome)
                break
            elif (dia.numero_mes != n):
                print("Erro na classe dia, ao receber o parametro",n,"o numero do dia no mes deve ser", n)
                print("numero atual: ", dia.numero)
                break
            elif (dia.numero_semana != dia_da_semana):
                print("Erro na classe dia, ao receber o parametro",n,"o numero do dia da semana deve ser", dia_da_semana)
                print("numero atual: ", dia.numero_semana)
                break
            else:
                print("Dia", n,"-","Sucesso ao testar dia", nome)

    testa_nomes_dos_dias()
    testa_dia_Achronian()
    testa_dia_Sinchronian()
    testa_dia_Semana()