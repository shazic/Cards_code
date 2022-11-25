import pytest
from cards import Card

@pytest.mark.parametrize('start_state', ['todo', 'in prog', 'done'])
def test_start(cards_db, start_state):
    c = Card(summary='This is a test card', state=start_state)
    index = cards_db.add_card(c)
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == 'in prog'
