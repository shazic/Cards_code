def test_disabled(capsys):
    with capsys.disabled():
        print('\nalways print')