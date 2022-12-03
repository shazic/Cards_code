import pytest
from cards import Card, InvalidCardId


def test_start(cards_db):
    """
    start changes state from "todo" to "in prog"
    """

    index = cards_db.add_card(Card('foo', state='todo'))
    cards_db.start(index)
    c = cards_db.get_card(index)
    assert c.state == 'in prog'

def test_start_non_existent(cards_db):
    """
    Shouldn't be able to start a non existent card
    """

    index = 123
    with pytest.raises(InvalidCardId):
        cards_db.start(index)