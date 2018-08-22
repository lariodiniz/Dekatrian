# coding: utf-8
import os

from kivy.lang import Builder


class CarregaKV():
    """Carrega no Sistema Todos os Arquivos KV"""

    def __init__(self):
        path = ""

        kv_path = path+'infra\\view\\kv'
        kvs = self.listarArquivos(".kv", kv_path)

        for kv in kvs:
            Builder.load_file(kv_path+"\\"+kv)

    def listarArquivos(self, ext, path):
        """Lista todos os arquivos que estão em um diretório com a extencao 
        definida"""

        caminhos = [os.path.join(path, nome) for nome in os.listdir(path)]
        arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
        arqFiltrados = [arq for arq in arquivos if arq.lower().endswith(ext)]
        return [arq.split('\\')[-1] for arq in arqFiltrados]

__author__ = "Lário dos Santos Diniz"
