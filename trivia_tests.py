from trivia import Game
from unittest.mock import patch


@patch('builtins.input', return_value='3')
def test_number_of_players_more_than_one(input):
    game = Game()
    game.add('P1')
    assert game.is_playable() == False
    game.add('P2')
    assert game.is_playable() == True

@patch('builtins.input', return_value='3')
def test_number_of_players_less_than_seven(input):
    game = Game()
    game.add('P1')
    game.add('P2')
    game.add('P3')
    game.add('P4')
    game.add('P5')
    assert game.add('P6') == True
    assert game.add('P7') == False

@patch('builtins.input', return_value='3')
def test_nb_player(input):
    game = Game()
    game.add('P1')
    game.add('P2')
    assert len(game.players) == 2
    game.add('P3')
    game.add('P4')
    assert len(game.players) == 4

@patch('builtins.input', return_value='3')
def test_good_answer(input):
    game = Game()
    game.add('P1')
    game.add('P2')
    assert game.purses == [0, 0, 0, 0, 0, 0]
    game.was_correctly_answered(is_joker='')
    print(game.purses)
    assert game.purses == [1, 0, 0, 0, 0, 0]

@patch('builtins.input', return_value='3')
def test_bad_answer(input):
    game = Game()
    game.add('P1')
    game.add('P2')
    assert game.purses == [0, 0, 0, 0, 0, 0]
    game.wrong_answer()
    print(game.purses)
    assert game.purses == [0, 0, 0, 0, 0, 0]

@patch('builtins.input', return_value='3')
def test_add_player(input):
    game = Game()
    game.add('P1')
    game.add('P2')
    assert len(game.players) == 2;
    game.add('P2')
    assert len(game.players) == 3;

@patch('builtins.input', return_value='3')
def test_delete_player(input):
    game = Game()
    game.add('P1')
    game.add('P2')
    assert len(game.players) == 2;
    game.add('P3')
    assert len(game.players) == 3;
    game.leave_game()
    assert len(game.players) == 2;

@patch('builtins.input', return_value='3')
def test_joker(input):
    game = Game()
    game.add('P1')
    game.add('P2')
    assert len(game.players_used_joker) == 0
    game.use_joker()
    assert len(game.players_used_joker) == 1

