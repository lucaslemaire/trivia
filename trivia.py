#!/usr/bin/env python3

class Game:
    def __init__(self):
        self.min_players = 2
        self.max_players = 6
        self.too_much_players = False
        self.players = []
        self.earn_coin = {}
        self.players_used_joker = []
        self.places = [0] * self.max_players
        self.purses = [0] * self.max_players
        self.in_penalty_box = [0] * self.max_players
        self.pop_questions = []
        self.science_questions = []
        self.sports_questions = []
        self.rock_questions = []
        self.techno_questions = []
        self.current_player = 0
        self.choosen_category = False
        self.is_getting_out_of_penalty_box = False
        self.number_of_gold_to_win = self.ask_number_of_gold_to_win()
        choice = input("Do you want to replaced the rock questions by Techno ? Press Y or N : ")
        self.questionTechno = True if choice.upper() == 'Y' else False
        self.fill_question(self.questionTechno)

    def ask_number_of_gold_to_win(self):
        gold_to_win = int(input("Type the number of gold required to win : "))
        if gold_to_win < 6 :
            print("Value is too low ! Number of gold required set to 6.")
            gold_to_win = 6
        return gold_to_win

    def fill_question(self, question_techno):
        for i in range(50):
            self.pop_questions.append("Pop Question %s" % i)
            self.science_questions.append("Science Question %s" % i)
            self.sports_questions.append("Sports Question %s" % i)
            if not question_techno:
                self.rock_questions.append("Rock Question %s" % i)
            else:
                self.techno_questions.append("Techno Question %s" % i)

    def is_playable(self):
        return self.min_players <= self.how_many_players <= self.max_players

    def add_to_earn_coin(self, player_name):
        self.earn_coin[player_name] = -1

    def add(self, player_name):
        if self.how_many_players < self.max_players:
            self.players.append(player_name)
            self.add_to_earn_coin(player_name)
            self.places[self.how_many_players-1] = 0
            self.purses[self.how_many_players-1] = 0
            self.in_penalty_box[self.how_many_players - 1] = False
            print("%s was added\nThey are player number %s" % (player_name, len(self.players)))
            return True
        self.too_much_players = True
        return False

    @property
    def how_many_players(self):
        return len(self.players)

    def roll(self, roll):
        print("%s is the current player \n They have rolled a %s" % (self.players[self.current_player], roll))

        if self.in_penalty_box[self.current_player]:
            if roll % 2 != 0:
                self.is_getting_out_of_penalty_box = True

                print("%s is getting out of the penalty box" % self.players[self.current_player])
                self.places[self.current_player] = self.places[self.current_player] + roll
                if self.places[self.current_player] > 11:
                    self.places[self.current_player] = self.places[self.current_player] - 12

                print(self.players[self.current_player] + \
                            '\'s new location is ' + \
                            str(self.places[self.current_player]))
                print_categ = self._current_category if self._current_category else self.choosen_category
                print("The category is %s" % print_categ)
                self._ask_question()
            else:
                print("%s is not getting out of the penalty box" % self.players[self.current_player])
                self.is_getting_out_of_penalty_box = False
        else:
            self.places[self.current_player] = self.places[self.current_player] + roll
            if self.places[self.current_player] > 11:
                self.places[self.current_player] = self.places[self.current_player] - 12

            print("%s's new location is %s" % (self.players[self.current_player], self.places[self.current_player]))
            print_categ = self._current_category if self._current_category else self.choosen_category
            print("The category is %s" % print_categ)
            self._ask_question()

    def _ask_question(self):
        if self._current_category == 'Pop': print(self.pop_questions.pop(0))
        if self._current_category == 'Science': print(self.science_questions.pop(0))
        if self._current_category == 'Sports': print(self.sports_questions.pop(0))
        if self._current_category == 'Rock': print(self.rock_questions.pop(0))
        if self._current_category == 'Techno': print(self.techno_questions.pop(0))

    @property
    def _current_category(self):
        place = self.places[self.current_player]
        if self.choosen_category: 
            self.choosen_category = False
            return self.choosen_category
        if place % 4 == 0 and place <= 8: return 'Pop'
        if place % 4 == 1 and place <= 9: return 'Science'
        if place % 4 == 2 and place <= 10: return 'Sports'
        if self.questionTechno:
            return 'Techno'
        return 'Rock'

    def was_correctly_answered(self, is_joker):
        self.earn_coin[self.players[self.current_player]] += 1
        self.purses[self.current_player] += self.earn_coin[self.players[self.current_player]]
        if self.in_penalty_box[self.current_player]:
            if self.is_getting_out_of_penalty_box:
                print('Answer was correct!!!!')
                if not is_joker:
                    self.purses[self.current_player] += 1
                    print("%s now has %s Gold Coins." % (self.players[self.current_player], self.purses[self.current_player]))
                else:
                    print("%s did not earned gold." % self.players[self.current_player])
                winner = self._did_player_win()
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0

                return winner
            else:
                self.current_player += 1
                if self.current_player == len(self.players): self.current_player = 0
                return True
        else:
            print("Answer was corrent!!!!")
            if not is_joker:
                self.purses[self.current_player] += 1
                print("%s now has %s Gold Coins." % (self.players[self.current_player], self.purses[self.current_player]))
            else:
                print("%s did not earned gold." % self.players[self.current_player])
            winner = self._did_player_win()
            self.current_player += 1
            if self.current_player == len(self.players): self.current_player = 0

            return winner

    def get_random_category(self):
        random_category = randrange(3)
        if random_category == 0: return 'Pop'
        if random_category == 1: return 'Science'
        if random_category == 2: return 'Sports'
        if random_category == 3:
            if not self.questionTechno:
                return 'Rock'
            else:
                return ''
        else: return 'Techno'

    def wrong_answer(self):
        print('Question was incorrectly answered')
        self.choosen_category = self.get_random_category()
        print("%s was sent to the penalty box" % self.players[self.current_player])
        self.earn_coin[self.players[self.current_player]] = -1

        self.in_penalty_box[self.current_player] = True
        self.current_player += 1
        if self.current_player == len(self.players): self.current_player = 0
        return True

    def _did_player_win(self):
        return not (self.purses[self.current_player] >= self.number_of_gold_to_win)

    def use_joker(self):
        is_joker = True
        player = self.players[self.current_player]
        if player not in self.players_used_joker:
            self.players_used_joker.append(player)
            print('%s USE Joker !' % player)
            self.was_correctly_answered(is_joker)
        return True

    def leave_game(self):
        player = self.players[self.current_player]
        if player in self.players:
            self.players.remove(player)
            self.places.pop(self.how_many_players-1)
            self.purses.pop(self.how_many_players-1)
            self.in_penalty_box.pop(self.how_many_players - 1)
            if self.current_player >= len(self.players): self.current_player = 0
            print("Le joueur %s quitte le jeu." % player)
            return True

from random import randrange

if __name__ == '__main__':
    not_a_winner = False

    game = Game()

    game.add('Chet1')
    game.add('Chet2')
    game.add('Chet3')
    game.add('Chet1')
    game.add('Chet2')
    game.add('Chet3')

    if not game.too_much_players:
        while True:
            if not game.is_playable():
                print("Il n'y a pas ou plus assez de joueurs.")
                break
            game.roll(randrange(5) + 1)
            random = randrange(9)
            if random == 1:
                not_a_winner = game.leave_game()
            elif random == 6:
                not_a_winner = game.use_joker()
            elif random == 7:
                not_a_winner = game.wrong_answer()
            else:
                is_joker = False
                not_a_winner = game.was_correctly_answered(is_joker)

            if not game.players or not not_a_winner: break
    else:
        print("Il y a trop de joueurs ! Impossible de lancer la partie")
