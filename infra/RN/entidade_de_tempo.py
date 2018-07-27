#coding: utf-8

__author__ = "Lário dos Santos Diniz"

"""
Data de Criação: 23/07/2018
"""

class EntidadeDeTempo():
	"""Classe abstrata que define uma entidade de tempo"""
	
	def __init__(self):
		self._nome = ""
		self._descricao = ""
		self._numero = ""
		
	@property
	def nome(self):
		return self._nome
	
	@property
	def descricao(self):
		return self._descricao
		
	@property
	def numero(self):
		return self._numero

if __name__ == "__main__":
	print("OK")