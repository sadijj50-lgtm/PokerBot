from treys import Evaluator, Card, Deck
import random

evaluator = Evaluator()

# Ranges pré-flop simplificados (pode expandir depois)
RANGES = {
    "UTG": ["AA","KK","QQ","JJ","AKs","AQs","TT","AKo"],
    "MP": ["AA","KK","QQ","JJ","TT","99","AQs","AJs","KQs","AKo","AQo"],
    "CO": ["AA","KK","QQ","JJ","TT","99","88","77","ATs+","KJs+","QJs","AKo","AQo","AJo"],
    "BTN": ["Qualquer par","A2s+","K9s+","QTs+","JTs","T9s","A9o+","KTo+","QJo"],
    "SB": ["Pares 55+","A2s+","KTs+","QTs+","JTs","ATo+","KJo+"],
    "BB": ["Defende muito","qualquer broadway","qualquer par","suited connectors"]
}

def simular_equidade(cartas, comunitarias, jogadores=2, n=2000):
    wins = 0
    for _ in range(n):
        deck = Deck()
        for c in cartas + comunitarias:
            if c in deck.cards:
                deck.cards.remove(c)

        mesa = comunitarias[:]
        while len(mesa) < 5:
            mesa.append(deck.draw(1))

        vilao = [deck.draw(1), deck.draw(1)]
        rank_heroi = evaluator.evaluate(cartas, mesa)
        rank_vilao = evaluator.evaluate(vilao, mesa)

        if rank_heroi < rank_vilao:
            wins += 1
    return (wins / n) * 100


def calcular_acao(cartas, comunitarias, posicao, jogadores):
    equidade = simular_equidade(cartas, comunitarias, jogadores)

    if equidade > 65:
        return "RAISE forte (2.5x pote)", equidade
    elif equidade > 40:
        return "CALL / CHECK", equidade
    elif equidade > 25 and posicao in ["BTN","CO"]:
        return "BLUFF ocasional", equidade
    else:
        return "FOLD", equidade
