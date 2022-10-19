from cards import Card

import pytest

def assert_identical(c1: Card, c2: Card):
    __tracebackhide__ = True
    assert c1 == c2
    # if c1.id != c2.id:
    #     pytest.fail(f'Ids do not match. {c1.id} != {c2.id}')
    assert c1.id == c2.id, f'Ids do not match. {c1.id} != {c2.id}'

def test_identical():
    c1 = Card('foo', id=123)
    c2 = Card('foo', id=123)
    assert_identical(c1, c2)