from trivia import Game

def test_number_of_players_more_than_one():
    game = Game()
    game.add('P1')
    
    assert game.is_playable() == False

    game.add('P2')   
    
    assert game.is_playable() == True


def test_number_of_players_less_than_seven():
    game = Game()
    game.add('P1')
    game.add('P2')
    game.add('P3')
    game.add('P4')
    game.add('P5')
    assert game.add('P6') == True
    assert game.add('P7') == False

def add_player():
    game = Game()
    game.add('P1')
    game.current_player == 1
    game.add('P2')
    game.current_player == 2
    
def leave_game():
    game = Game()
    game.add('P1')
    game.add('P2')
    game.add('P3')
    game.players.remove(game.player)
    game.current_player == 2

