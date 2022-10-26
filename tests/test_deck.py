from poker import Deck


def test_deck() -> None:
    deck = Deck()
    assert len(deck) == 52

    cards = [card for card in deck.cards]
    deck.shuffle()
    assert cards != deck.cards
