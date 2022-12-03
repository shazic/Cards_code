import pytest
from cards import Card

@pytest.fixture(scope='function')
def cards_db_three_cards(db):
    db_ = db
    db_.delete_all()
    db_.add_card(Card('Learn something'))
    db_.add_card(Card('Build useful tools'))
    db_.add_card(Card('Teach others'))

    return db_

def test_zero_cards(cards_db):
    assert cards_db.count() == 0

def test_three_card(cards_db_three_cards):
    assert cards_db_three_cards.count() == 3