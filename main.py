from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

from ocr_reader import capturar_info
from poker_engine import calcular_acao


class PokerBotUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.add_widget(Image(source="assets/mesa.png"))

        self.label_resultado = Label(text="Iniciando bot...", font_size="20sp")
        self.add_widget(self.label_resultado)

        btn_scan = Button(text="📸 Ler tela e calcular ação", size_hint=(1, 0.2))
        btn_scan.bind(on_press=self.executar_bot)
        self.add_widget(btn_scan)

    def executar_bot(self, *args):
        try:
            cartas, comunitarias, posicao, jogadores = capturar_info()
            acao, equidade = calcular_acao(cartas, comunitarias, posicao, jogadores)
            self.label_resultado.text = f"[{posicao}] -> {acao}\nEquidade: {equidade:.1f}%"
        except Exception as e:
            self.label_resultado.text = f"Erro: {str(e)}"


class PokerBotApp(App):
    def build(self):
        return PokerBotUI()


if __name__ == "__main__":
    PokerBotApp().run()
