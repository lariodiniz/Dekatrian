#coding: utf-8
#author: Lário dos Santos Diniz
__author__ = "Lário dos Santos Diniz"

import os

def listarArquivos(extencao, path = os.getcwd()):
    """Lista todos os arquivos que estão em um diretório com a extencao definida"""
    
    caminhos = [os.path.join(path, nome) for nome in os.listdir(path)]
    arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
    arquivosFiltrados = [arq for arq in arquivos if arq.lower().endswith(extencao)]
    return [arq.split('\\')[-1] for arq in arquivosFiltrados]

if __name__ == '__main__':
    print(listarArquivos(extencao = '.py'))