from cards import Card
import cards
import pytest
from packaging.version import parse
@pytest.mark.skipif(
                    parse(cards.__version__).major < 2,
                    reason='Less than operation not supported in ver. below 2.0')
def test_less_than():
    c1 = Card('a task')
    c2 = Card('b task')

    print(f'Version is {cards.__version__}, and parsed version is {parse("11.45.32").major}')
    assert c1 < c2