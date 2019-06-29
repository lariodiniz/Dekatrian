#coding: utf-8
__author__ = "Lário dos Santos Diniz"


from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

class Tela(Screen):
    telaSecundaria = ObjectProperty(None)
    nome  = ObjectProperty(str())
    title = ObjectProperty(str())

    def __init__(self, **kwargs):
        self.aplicacao = App.get_running_app()
        super(Tela, self).__init__(**kwargs)
    
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            self.aplicacao.mudarTela(self.aplicacao.tela_menu)
            return True

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.voltar)
