import pytest
from cards import Card, MissingSummary

def test_should_add_a_card_with_summary_to_empty_db(cards_db):
    c = Card(summary='This is a card for the empty db')
    index = cards_db.add_card(c)
    added_card = cards_db.get_card(index)

    assert added_card == c
    assert cards_db.count() == 1

@pytest.mark.num_cards(3)
def test_should_add_a_card_with_summary_to_non_empty_db(cards_db):
    c = Card(summary='This is a card for the empty db')
    index = cards_db.add_card(c)
    added_card = cards_db.get_card(index)

    assert added_card == c
    assert cards_db.count() == 4

def test_should_add_a_card_with_summary_and_owner_to_empty_db(cards_db):
    c = Card(summary='This is a card for the empty db', owner='Fake Owner')
    index = cards_db.add_card(c)
    added_card = cards_db.get_card(index)

    assert added_card == c

def test_should_throw_error_when_adding_a_card_with_missing_summary(cards_db):
    c = Card(owner='This is a card for the empty db')
    with pytest.raises(MissingSummary):
        cards_db.add_card(c)

def test_should_add_two_cards_with_identical_summary_and_owners(cards_db):
    c1 = Card(summary='This is a card for the empty db')
    index1 = cards_db.add_card(c1)

    c2 = Card(summary='This is a card for the empty db')
    index2 = cards_db.add_card(c2)

    assert cards_db.count() == 2
    assert index1 != index2
    assert c1 == c2




