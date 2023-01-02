from cards import Card


def test_should_return_zero_for_empty_database(cards_db):
    assert cards_db.count() == 0

def test_should_return_one_after_adding_a_card_to_database(cards_db):
    c = Card(summary='adding one card here')
    cards_db.add_card(c)
    assert cards_db.count() == 1

def test_should_return_three_after_adding_three_cards_to_database(cards_db):
    c1 = Card(summary='adding one card here')
    cards_db.add_card(c1)

    c2 = Card(summary='adding one card here')
    cards_db.add_card(c2)

    c3 = Card(summary='adding one card here')
    cards_db.add_card(c3)

    assert cards_db.count() == 3


