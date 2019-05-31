# coding: utf-8
from kivy.uix.boxlayout import BoxLayout
from kivy.utils import get_color_from_hex


def Texto():

    return '''
Este programa está sendo desenvolvido 
por [ref=https://twitter.com/lariodiniz]Lario Diniz[/ref]. Para criticas, 
sugestoes e contatos envie um email para:

lariodiniz@gmail.com

Este programa é de codigo aberto e 
gratuito, ele utiliza a licenca MIT. 
Acesse o repositorio do codigo e 
contribua no desenvolvimento.

[ref=https://github.com/lariodiniz/Dekatrian]github.com/lariodiniz/Dekatrian[/ref]

Icones dos botões feitos por 
[ref=https://www.flaticon.com/authors/dinosoftlabs]DinosoftLabs[/ref] para [ref=https://www.flaticon.com/]www.flaticon.com[/ref] 
e usa a licença [ref=http://creativecommons.org/licenses/by/3.0/]CC 3.0[/ref] 


Tecnologias utilizadas no desenvolvimento:

Python 3.5
Kivy 1.9.1
'''

class TelaDesenvolvimento(BoxLayout):

    def __init__(self, **kwargs):
        self.texto = Texto()
        super(TelaDesenvolvimento, self).__init__(**kwargs)


__author__ = "Lário dos Santos Diniz"
