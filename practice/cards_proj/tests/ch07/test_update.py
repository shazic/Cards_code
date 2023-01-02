import pytest
from cards import Card


def test_should_update_owner_of_card(cards_db):
    original_card = Card(summary='This is a test', owner='Owner 1')
    index = cards_db.add_card(original_card)
    updated_card = Card(summary='This is a test', owner='Owner 2')
    cards_db.update_card(index, updated_card)

    c = cards_db.get_card(index)
    assert c == updated_card

def test_should_update_summary_of_card(cards_db):
    original_card = Card(summary='This is a test', owner='Owner 1')
    index = cards_db.add_card(original_card)
    updated_card = Card(summary='This is a test 2', owner='Owner 1')
    cards_db.update_card(index, updated_card)

    c = cards_db.get_card(index)
    assert c == updated_card

def test_should_update_owner_and_summary_of_card(cards_db):
    original_card = Card(summary='This is a test', owner='Owner 1')
    index = cards_db.add_card(original_card)
    updated_card = Card(summary='This is a test 2', owner='Owner 2')
    cards_db.update_card(index, updated_card)

    c = cards_db.get_card(index)
    assert c == updated_card

def test_should_not_be_able_to_update_non_existent_card(cards_db):
    with pytest.raises(Exception):
        cards_db.update_card(999, Card(summary='This is a test', owner='Owner 1'))