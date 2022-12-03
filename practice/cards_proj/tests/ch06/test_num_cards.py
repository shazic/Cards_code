import pytest
from cards import Card

pytestmark = [pytest.mark.num_cards(4)] # this will be superceded by the closest marker

@pytest.mark.num_cards(3)
def test_three_cards(cards_db):
    assert cards_db.count() == 3