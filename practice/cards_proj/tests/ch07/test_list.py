import pytest
from cards import Card


def test_should_return_empty_list_from_empty_database(cards_db):
    card_list = cards_db.list_cards()
    assert card_list == []

@pytest.mark.num_cards(3)
def test_should_return_non_empty_list_from_non_empty_database(cards_db):
    card_list = cards_db.list_cards()
    assert len(card_list) == 3

def test_should_filter_with_owner_if_list_with_owner(non_empty_db):
    card_list = non_empty_db.list_cards(owner="Brian")
    assert len(card_list) == 2

def test_should_filter_by_state_if_list_with_state(non_empty_db):
    card_list = non_empty_db.list_cards(state="done")
    assert len(card_list) == 2

def test_should_filter_by_both_owner_and_state_if_list_with_owner_and_state(non_empty_db):
    card_list = non_empty_db.list_cards(owner="Brian", state="done")
    assert len(card_list) == 1

