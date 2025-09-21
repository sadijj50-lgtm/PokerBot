import pytesseract
from PIL import ImageGrab
from treys import Card

# Configura o caminho do Tesseract (em Android pode mudar)
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

def texto_para_carta(txt):
    mapa = {
        "A": "A", "K": "K", "Q": "Q", "J": "J", "T": "T",
        "2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"
    }
    if len(txt) < 2:
        return None
    valor = mapa.get(txt[0].upper(), None)
    naipe = txt[1].lower()
    if not valor:
        return None
    return Card.new(valor + naipe)

def capturar_info():
    # Captura tela
    img = ImageGrab.grab()
    texto = pytesseract.image_to_string(img)

    # DEBUG: em produção você teria parsing mais detalhado
    # Aqui simplifico para demo
    cartas = [Card.new("As"), Card.new("Kh")]   # Exemplo fixo
    comunitarias = []
    posicao = "BTN"
    jogadores = 3

    return cartas, comunitarias, posicao, jogadores
