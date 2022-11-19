from cards import Card
import pytest

@pytest.mark.parametrize(
    "start_summary, start_state",
    [
        ('write a book', 'done'),
        ('second edition', 'in prog'),
        ('create a course', 'todo')
    ],
)
def test_finish(cards_db, start_summary, start_state):
    initial_card = Card(summary=start_summary, state=start_state)
    index = cards_db.add_card(initial_card)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == 'done'

@pytest.mark.parametrize('start_state', ['done', 'in prog', 'todo'])
def test_finish_simple(cards_db, start_state):
    initial_card = Card(summary='write a book', state=start_state)
    index = cards_db.add_card(initial_card)
    cards_db.finish(index)
    card = cards_db.get_card(index)
    assert card.state == 'done'

@pytest.mark.parametrize(
    "test_input,expected",
    [("3+5", 8), ("2+4", 6), pytest.param("6*9", 42, marks=pytest.mark.xfail)],
)
def test_eval(test_input, expected):
    assert eval(test_input) == expected