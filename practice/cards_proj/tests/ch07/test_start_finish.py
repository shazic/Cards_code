import pytest
from cards import Card


@pytest.fixture(params=['todo', 'in prog', 'done'])
def start_state(request):
    return request.param

def test_should_have_status_in_prog_when_card_is_started(cards_db, start_state):
    index = cards_db.add_card(Card(summary='This is a test', state=start_state))
    cards_db.start(index)
    c = cards_db.get_card(index)
    assert c.state == 'in prog'

def test_should_not_be_able_to_start_non_existent_card(cards_db):
    with pytest.raises(Exception):
        cards_db.start(1999)

def test_should_have_status_done_when_card_is_finished(cards_db, start_state):
    index = cards_db.add_card(Card(summary='This is a test', state=start_state))
    cards_db.finish(index)
    c = cards_db.get_card(index)
    assert c.state == 'done'

def test_should_not_be_able_to_finish_non_existent_card(cards_db):
    with pytest.raises(Exception):
        cards_db.finish(1999)

