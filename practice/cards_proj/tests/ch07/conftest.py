import pytest
import cards
from pathlib import Path
from tempfile import TemporaryDirectory

# def pytest_addoption(parser):
#     parser.addoption(
#         '--func-db',
#         action='store_true',
#         default=False,
#         help='new db for each test',
#     )

def db_scope(fixture_name, config):
    if config.getoption("--func-db", None):
        return "function"
    return "session"

@pytest.fixture(scope=db_scope)
def session_card_db(tmp_path_factory):
    """CardsDB object connected to a temporary database
    """
    db_path = tmp_path_factory.mktemp('cards_db')
    db_ = cards.CardsDB(db_path)
    yield db_
    db_.close()

@pytest.fixture(scope="session")
def some_cards():
    return [
        cards.Card("write book", "Brian", "done"),
        cards.Card("edit book", "Katie", "done"),
        cards.Card("write 2nd edition", "Brian", "todo"),
        cards.Card("edit 2nd edition", "Katie", "todo"),
    ]

@pytest.fixture(scope="function")
def non_empty_db(cards_db, some_cards):
    for c in some_cards:
        cards_db.add_card(c)
    return cards_db

@pytest.fixture(scope="function")
def cards_db(session_card_db, request, faker):
    db = session_card_db
    """CardsDB object that is empty"""
    db.delete_all()
    # support for `@pytest.mark.num_cards(<some number>)
    faker.seed_instance(101)
    m = request.node.get_closest_marker('num_cards')
    if m and len(m.args) > 0:
        num_cards = m.args[0]
        for _ in range(num_cards):
            db.add_card(
                cards.Card(
                    summary=faker.sentence(),
                    owner=faker.first_name()
                )
            )
    return db
