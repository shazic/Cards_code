import pytest
from cards import Card, InvalidCardId


@pytest.mark.num_cards(3)
def test_should_remove_one_from_non_empty_database(cards_db):
    card_to_be_deleted = cards_db.list_cards()[0]
    cards_db.delete_card(card_to_be_deleted.id)
    list_of_cards_after_deletion = cards_db.list_cards()

    assert (card_to_be_deleted not in list_of_cards_after_deletion) \
           and \
           (cards_db.count() == 2)

@pytest.mark.num_cards(1)
def test_should_remove_last_card_from_database(cards_db):
    card_to_be_deleted = cards_db.list_cards()[0]
    cards_db.delete_card(card_to_be_deleted.id)

    assert cards_db.count() == 0

@pytest.mark.num_cards(3)
def test_should_not_be_able_to_delete_non_existent_card(cards_db):
    with pytest.raises(InvalidCardId):
        cards_db.delete_card(9999)

