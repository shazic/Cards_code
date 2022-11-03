# Python testing with `pytest`
Follow along examples with the book __Python testing with Pytest__ by _Brian Okken_ (2nd edition).

## Chapter 1 review (Getting started)
- `pytest` can be run in several different ways:
    - `pytest`: With n- arguments, `pytest` searches the local directory and subdirectories for tests.
    - `pytest <filename>`: Runs the tests in one file
    - `pytest <filename> <filename> ...`: Runs the tests in multiple named files
    - `pytest <dirname>`: Starts in a particular directory (or more than one) and recursively searches for tests
- Test discovery refers t- how `pytest` finds your test code and depends on naming:
    - Test files should be named `test_<something>.py` or `<something>_test.py`.
    - Test methods and functions should be named `test_<something>`.
    - Test classes should be named `Test<Something>`.
- The possible outcomes of a test function include: `PASSED (.)`, `FAILED (F)`, `SKIPPED (s)`, `XFAIL (x)`, `XPASS (X)`, and `ERROR (E)`.
- The `-v` or `--verbose` command-line flag is used to reveal more verbose output.
- The `--tb=no` command-line flag is used to to turn off tracebacks.

## Chapter 2 review (Writing tests)
- `pytest` uses assert rewriting, which allows us to use standard Python assert expressions.
- Tests can fail from assertion failures, from calls to `fail()`, or from any uncaught exception.
- `pytest.raises()` is used to test for expected exceptions.
- The `-vv` command-line flag shows even more information during test failures.

## Chapter 3 review (Fixtures)
- Fixtures are `@pytest.fixture()` decorated functions.
- Fixtures can return data using `return` or `yield`.
- Code before the `yield` is the __setup__ code. Code after the `yield` is the __teardown__ code.
- Fixtures can be set to one of the following scope:
  - _function_
  - _class_
  - _module_
  - _package_
  - _session_ 
- The __default__ scope is _function_ scope. You can even define the scope dynamically.
- Multiple test modules can use the same fixture if it’s in a `conftest.py` file.
- `autouse` fixtures don’t have to be named by the test function.
- You can have the name of a fixture be different than the fixture function name.
- Some command-line flags:
  - `pytest --setup-show` is used to see the order of execution.
  - `pytest --fixtures` is used to list available fixtures and where the fixture is located.
  - `-s` and `--capture=no` allow print statements to be seen even in passing tests.

