import cards

def test_two(cards_db):
    cards_db.add_card(cards.Card('first'))
    cards_db.add_card(cards.Card('second'))
    assert cards_db.count() == 2

def test_empty(cards_db):
    assert cards_db.count() == 0

