# coding: utf-8
from .dia import Dia
from .meses import Mes
from datetime import date, datetime, timedelta


class Data():
    """Classe que define Datas no formato Dekatrian"""

    @property
    def dia_nome(self):
        return self._dia.nome

    @property
    def dia_do_ano(self):
        return str(self._dia_do_ano)

    @property
    def dia_numero_mes(self):
        return str(self._dia.numero_mes)

    @property
    def dia_numero_semana(self):
        return str(self._dia.numero_semana)

    @property
    def mes_numero(self):
        return str(self._mes.numero)

    @property
    def mes_nome(self):
        return self._mes.nome

    def define_dia(self, dia):
        if type(dia) is not int:
            men = "A viariavel para o dia precisa ser do tipo inteiro."
            raise Exception(men)

        self._dia = Dia(dia)
        self.converte_gregoriano()

    def define_mes(self, mes):
        nomesMes = Mes.nomes()

        try:
            mesNum = nomesMes.index(mes)+1
            self._mes = Mes(mesNum)
            self.converte_gregoriano()
        except:
            men = "A viariavel para o nome do mes é inválida."
            raise Exception(men)

    def define_ano(self, ano):
        self.ano = ano
        self.converte_gregoriano()

    def _define_dias_passados(self, data):
        d2 = datetime.strptime(data.strftime("%Y-%m-%d"), '%Y-%m-%d')
        d1 = datetime.strptime('{}-01-01'.format(data.year), '%Y-%m-%d')
        return abs((d2 - d1).days)

    def imprimir(self):
        return "{:02d} \ {:02d} ({}) \ {}".format(
            int(self.dia_numero_mes),
            int(self.mes_numero),
            self.mes_nome, int(self.ano))

    def converte_gregoriano(self):

        d1 = datetime.strptime('{}-01-01'.format(int(self.ano) - 10000),
                               '%Y-%m-%d')
        diasSemMes = 0
        if self._ehBissexto(d1.year):
            diasSemMes = 2
        else:
            diasSemMes = 1

        diasPassados = ((self._mes.numero * 28) - 28)

        diasPassados += self._dia.numero_mes + diasSemMes
        d2 = d1 + timedelta(diasPassados - 1)
        self.data = d2.strftime("%d/%m/%Y")

    @property
    def to_date(self):
        ano = self.data[-4:]
        mes = self.data[3:5]
        dia = self.data[0:2]
        return datetime.strptime(ano+"-"+mes+"-"+dia, '%Y-%m-%d')

    def __init__(self, data):

        dias_passados = self._define_dias_passados(data)
        self.data = data.strftime("%d/%m/%Y")
        self._dia_do_ano = dias_passados + 1
        self.ano = str(data.year + 10000)

        if dias_passados == 0:
            dia_do_mes = 0
            mes = 0
        elif self._ehBissexto(data.year):
            if dias_passados == 1:
                dia_do_mes = -1
                mes = 0
            else:
                dia_do_mes = ((dias_passados - 1) % 28)
                mes = ((dias_passados - 1) // 28) + 1
                if dia_do_mes == 0:
                    dia_do_mes = 28
        else:
            dia_do_mes = (dias_passados % 28)
            mes = ((dias_passados) // 28) + 1
            if dia_do_mes == 0:
                dia_do_mes = 28

        if (mes > 13):
            mes = 13

        self._mes = Mes(mes)
        self.define_dia(dia_do_mes)

    def _ehBissexto(self, ano):
        return (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0)


if __name__ == "__main__":
    def testa_dia_Achronian():
        d = date.today()
        d = datetime.strptime('{}-01-01'.format(d.year), '%Y-%m-%d')
        data = Data(d)
        if (data.dia_nome == 'Achronian'):
            print("Erro na classe data, o nome do primeiro dia do ano deve",
                  "ser Achronian")
            print("Nome atual:", data.dia_nome)
        elif (data.dia_do_ano == 1):
            print("Erro na classe data, o numero do primeiro dia do ano",
                  "deve ser 1")
            print("numero atual:", data.dia_do_ano)
        elif (data.dia_numero_mes == '1'):
            print("Erro na classe data, o numero do dia da semana do primeiro",
                  "dia do ano deve ser 1")
            print("numero atual:", data.dia_numero_mes)
        elif (data.dia_numero_semana == '1'):
            print("Erro na classe data, o numero do dia da semana do primeiro",
                  "dia do ano deve ser 1")
            print("numero atual:", data.dia_numero_semana)
        elif (data.mes_nome == 'Sem Mes'):
            print("Erro na classe data, o nome do mes do primeiro dia do ano",
                  "deve ser Sem Mes")
            print("nome atual:", data.mes_nome)
        else:
            print("Sucesso ao testar a data",
                  data.imprimir(),
                  "-",
                  d.strftime("%d/%m/%Y"))

    def testa_dia_Sinchronian():
        d = date.today()
        d = datetime.strptime('2016-01-02', '%Y-%m-%d')
        data = Data(d)
        if (data.dia_nome == 'Sinchronian'):
            print("Erro na classe data, o nome do segundo dia de um ano",
                  "bissesto deve ser Sinchronian")
            print("Nome atual:", data.dia_nome)
        elif (data.dia_do_ano == 2):
            print("Erro na classe data, o numero do segundo dia de um ano",
                  "bissesto deve ser 2")
            print("numero atual:", data.dia_do_ano)
        elif (data.dia_numero_mes == '2'):
            print("Erro na classe data, o numero do dia da semana do segundo",
                  "dia de um ano bissesto deve ser 2")
            print("numero atual:", data.dia_numero_mes)
        elif (data.dia_numero_semana == '2'):
            print("Erro na classe data, o numero do dia da semana do primeiro",
                  "dia do ano deve ser 2")
            print("numero atual:", data.dia_numero_semana)
        elif (data.mes_nome == 'Sem Mes'):
            print("Erro na classe data, o nome do mes do segundo dia de ano",
                  "bissexto deve ser Sem Mes")
            print("nome atual:", data.mes_nome)
        else:
            print("Sucesso ao testar a data",
                  data.imprimir(),
                  "-",
                  d.strftime("%d/%m/%Y"))

    def testa_dia_Especifico():
        d = datetime.strptime('2018-01-03', '%Y-%m-%d')
        data = Data(d)
        print("Data:",
              data.imprimir(),
              "-",
              d.strftime("%d/%m/%Y"))
        if (data.dia_nome == 'Rubia'):
            print("Erro na classe data ao testar a data 31/07/2018. o nome do",
                  "dia deveria ser Rubia")
            print("Nome atual: ", data.dia_nome)
        elif (data.dia_do_ano == 212):
            print("Erro na classe data ao testar a data 31/07/2018. o numero",
                  "do dia no ano deveria ser 212")
            print("numero atual: ", data.dia_do_ano)
        elif (data.dia_numero_semana == '1'):
            print("Erro na classe data ao testar a data 31/07/2018. o nome do",
                  "dia deveria ser Rubia")
            print("numero atual: ", data.dia_numero_semana)
        elif (data.dia_numero_mes == '15'):
            print("Erro na classe data ao testar a data 31/07/2018. o nome do",
                  "dia deveria ser Rubia")
            print("numero atual: ", data.dia_numero_mes)
        elif (data.mes_nome == 'Hermetian'):
            print("Erro na classe data ao testar a data 31/07/2018. o nome do",
                  "mes deveria ser Hermetian")
            print("nome atual: ", data.mes_nome)
        else:
            print("Sucesso ao testar a data",
                  data.imprimir(),
                  "-",
                  d.strftime("%d/%m/%Y"))

    print()
    print(" ---- Iniciando Testes ---- ")
    print()
    testa_dia_Achronian()
    testa_dia_Sinchronian()
    testa_dia_Especifico()

__author__ = "Lário dos Santos Diniz"
