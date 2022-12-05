import pytest

pytestmark = pytest.mark.all

@pytest.mark.odd
def test_one():
    pass


def test_two():
    pass

@pytest.mark.odd
def test_three():
    pass

@pytest.mark.testclass
class TestClass:
    def test_four(self):
        pass

    @pytest.mark.odd
    def test_five(self):
        pass


@pytest.mark.parametrize("x", 
                         [
                             6, 
                             pytest.param(7, marks=pytest.mark.odd)
                        ])
def test_param(x):
    pass

#############################################################
# commands                                                  #
#############################################################
# 5. Run all the tests using the all marker.                #
# - pytest -v -m all                                        #
# 6. Run the odd tests.                                     #
# - pytest -v -m odd                                        #
# 7. Run the odd tests that are not marked with testclass.  #
# - pytest -v -m "odd and not testclass"                    #
# 8. Run the odd tests that are parametrized.               #
#    (Hint: Use both marker and keyword flags.)             #
# - pytest -v -m odd -k param                               #
#############################################################
