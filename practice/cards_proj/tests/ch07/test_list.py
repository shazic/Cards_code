import pytest
from cards import Card


def test_should_return_empty_list_from_empty_database(cards_db):
    card_list = cards_db.list_cards()
    assert card_list == []

@pytest.mark.num_cards(3)
def test_should_return_non_empty_list_from_non_empty_database(cards_db):
    card_list = cards_db.list_cards()
    assert len(card_list) == 3
