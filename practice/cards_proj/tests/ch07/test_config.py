import cards.cli as c
def test_should_return_correct_db_path_from_config(cards_db, capsys):
    c.config()
    output = capsys.readouterr().out.rstrip()
    assert output == 'C:\\Users\\schattopadhyaya\\cards_db'