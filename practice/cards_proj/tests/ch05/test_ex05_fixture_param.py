from cards import Card
import pytest


@pytest.fixture(params=['todo', 'in prog', 'done'])
def start_state(request):
    return request.param

def test_start(cards_db, start_state):
    c = Card(summary='this is a test', state=start_state)
    index = cards_db.add_card(c)
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == 'in prog'