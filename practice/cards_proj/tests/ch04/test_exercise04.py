from exercise04 import hello
import os

FILENAME = 'hello.txt'

def test_writes_correct_content_to_file_without_fixtures():
    if os.path.exists(FILENAME):
        os.remove(FILENAME)

    hello()

    with open(FILENAME, 'r') as file:
        assert file.read() == 'Hello World!\n'

    os.remove(FILENAME)

def test_writes_correct_content_to_file_with_monkeypatch_and_tmp_path(monkeypatch, tmp_path, capsys):
    filepath = tmp_path
    monkeypatch.chdir(str(filepath))
    with capsys.disabled():
        print(f'temporary path = {filepath}')

    hello()

    full_filepath = f'{filepath}\\{FILENAME}'
    with open(full_filepath, 'r') as file:
        assert file.read() == 'Hello World!\n'
