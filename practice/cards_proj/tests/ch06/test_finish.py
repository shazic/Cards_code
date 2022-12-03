import pytest
from cards import Card, InvalidCardId

################################################################
# If pytest sees a pytestmark attribute in a test module,      #
# it will apply the marker(s) to all the tests in that module  #
################################################################
pytestmark = [pytest.mark.finish]


@pytest.fixture(params=
                [
                    'todo',
                    pytest.param('in prog', marks=pytest.mark.smoke),
                    'done'
                ])
def start_state_fixture(request):
    return request.param

# @pytest.mark.smoke
class TestFinish:
    def test_finish_from_todo(self, cards_db):
        i = cards_db.add_card(Card('a sample card', state='todo'))
        cards_db.finish(i)
        c = cards_db.get_card(i)
        assert c.state == 'done'

    def test_finish_from_in_prog(self, cards_db):
        i = cards_db.add_card(Card('a sample card', state='in prog'))
        cards_db.finish(i)
        c = cards_db.get_card(i)
        assert c.state == 'done'

    def test_finish_from_done(self, cards_db):
        i = cards_db.add_card(Card('a sample card', state='done'))
        cards_db.finish(i)
        c = cards_db.get_card(i)
        assert c.state == 'done'

    @pytest.mark.parametrize(
        'start_state',
        [
            'todo',
            pytest.param('in prog', marks=pytest.mark.smoke),
            'done',
        ],
    )
    def test_finish_from(self, cards_db, start_state):
        i = cards_db.add_card(Card('a sample card', state=start_state))
        cards_db.finish(i)
        c = cards_db.get_card(i)
        assert c.state == 'done'

    def test_finish_fix_from(self, cards_db, start_state_fixture):
        i = cards_db.add_card(Card('a sample card', state=start_state_fixture))
        cards_db.finish(i)
        c = cards_db.get_card(i)
        assert c.state == 'done'

    @pytest.mark.smoke
    @pytest.mark.exception
    def test_finish_non_existent(self, cards_db):
        i = 123
        with pytest.raises(InvalidCardId):
            cards_db.finish(i)
