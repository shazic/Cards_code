from cards import Card

def pytest_generate_tests(metafunc):
    if 'start_state' in metafunc.fixturenames:
        metafunc.parametrize('start_state', ['todo', 'in prog', 'done'])

def test_start(cards_db, start_state):
    c = Card(summary='this is a test', state='in prog')
    index = cards_db.add_card(c)
    cards_db.start(index)
    card = cards_db.get_card(index)
    assert card.state == 'in prog'