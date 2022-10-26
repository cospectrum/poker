from poker import CardValue, Suit


def test_card() -> None:
    assert len(CardValue) == 13
    assert len(Suit) == 4
