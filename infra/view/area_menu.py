# coding: utf-8
from kivy.app import App
from kivy.uix.actionbar import ActionBar
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.utils import get_color_from_hex
from kivy.animation import Animation

class AreaMenu(ActionBar):
    """Classe que define a area que mostra o menu."""

    def __init__(self, **kwargs):
        self.aplicacao = App.get_running_app()
        self.img_logo = self.aplicacao.pasta_imagens+'icon.png'

        super(AreaMenu, self).__init__(**kwargs)

    def on_press_menu(self):
        self.aplicacao.mudarTela(self.aplicacao.tela_menu)

    def sair(self, *args):
        self.aplicacao.stop()

    def confirmacao(self, *args):
        box = BoxLayout(orientation='vertical', padding=10, spacing=10)
        botoes = BoxLayout(padding=10, spacing=10)

        pop = Popup(title='Deseja mesmo sair?', content=box, 
                size_hint=(None, None),
                size=(150, 150),
                background= self.aplicacao.pasta_imagens+'background.png',
                )

        sim = Button(text='Sim', on_release=self.sair)
        nao = Button(text='Não', on_release=pop.dismiss)
        botoes.add_widget(sim)

        botoes.add_widget(nao)
        atencao = Image(source=self.aplicacao.pasta_imagens+'warning.png')
        box.add_widget(atencao)
        box.add_widget(botoes)
        anim = Animation(size=(300, 180), duration=0.2, t='out_back')
        anim.start(pop)
        pop.open()



__author__ = "Lário dos Santos Diniz"
