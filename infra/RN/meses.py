#coding: utf-8

__author__ = "Lário dos Santos Diniz"

"""
Data de Criação: 23/07/2018
"""
#from .entidade_de_tempo import EntidadeDeTempo


class Mes():

    @staticmethod
    def nomes():
        return ("Auran","Borean","Coronian","Driadan","Electran","Faian", "Gaian","Hermetian","Irisian","Kaosian","Lunan","Maian","Nixian")
		
    def __init__(self, numero):
	    
        self._numero = numero

        if numero == 0:
            self._nome = "Sem Mes"
        else:
            self._nome = Mes.nomes()[self.numero - 1]

    @property
    def numero(self):
        return self._numero

    @property
    def nome(self):
        return self._nome

if __name__ == "__main__":

    def testa_nomes_dos_meses():
        nomes = Mes.nomes()
        nomes_corretos = ("Auran","Borean", "Coronian", "Driadan", "Electran", "Faian", "Gaian", "Hermetian", "Irisian", "Kaosian","Lunan", "Maian","Nixian")

        for n in range(len(nomes_corretos)):
            if (nomes[n] != nomes_corretos[n]):
                print("Erro no nome da semana o dia",n+1," da semana deveria ser",nomes_corretos[n])
                print("Nome atual: ", nomes[n])
                break
            elif (n == 6):
                print("Sucesso ao testar os nomes da semana.")
    
    def testa_meses():
        for n in [1,2,3,4,5,6, 7,8,9,10,11,12,13]:
            mes = Mes(n)
            nome = Mes.nomes()[n-1]
            if (mes.nome != nome):
                print("Erro na classe mes, ao receber o parametro ",n," o nome do mes deve ser", nome)
                print("Nome atual: ", mes.nome)
                break
            elif (mes.numero == str(n)):
                print("Erro na classe mes, ao receber o parametro ",n," o numero do dia deve ser", n)
                print("numero atual: ", mes.numero)
                break
            else:
                print("Sucesso ao testar mes", nome)

    testa_nomes_dos_meses()
    testa_meses()
