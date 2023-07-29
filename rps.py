#!/usr/bin/env python3
import random

moves = ['rock', 'paper', 'scissors']

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    score = 0

    def __init__(self):
        self.my_move = None
        self.their_move = None

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        while True:
            action = input("Rock, paper, or scissors?\n").lower()
            for move in moves:
                if move in action:
                    return move
            print("Invalid input. Please choose rock, paper, or scissors.")

    def learn(self, my_move, their_move):
        pass


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        index = (moves.index(self.my_move) + 1) % len(moves)
        return moves[index]


def beats(one, two):
    return (
        (one.lower() == 'rock' and two.lower() == 'scissors') or
        (one.lower() == 'scissors' and two.lower() == 'paper') or
        (one.lower() == 'paper' and two.lower() == 'rock')
    )


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.rounds = None

    def set_rounds(self):
        while True:
            try:
                self.rounds = int(input("Enter the number of rounds: "))
                if self.rounds > 0:
                    break
                else:
                    print("Invalid input. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def final_results(self):
        if self.p1.score > self.p2.score:
            print("CONGRATULATION, PLAYER 1 WINS THE GAME!!\n")
        elif self.p2.score > self.p1.score:
            print("CONGRATULATION, PLAYER 2 WINS THE GAME!!\n")
        else:
            print("THE GAME IS A TIE!")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            print("WOW! PLAYER 1 WINS!")
            self.p1.score += 1
        elif beats(move2, move1):
            print("WOW! PLAYER 2 WINS!")
            self.p2.score += 1
        else:
            print("IT'S A TIE!")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"\n----Scores----\n Player 1: {self.p1.score}"
              f" \n Player 2: {self.p2.score}\n")

    def play_game(self):
        print("GAME START!")
        for round in range(self.rounds):
            print(f"Round {round+1}:")
            self.play_round()
        print("GAME OVER!")
        print(f"\n----Final Scores----\n\n Player 1: {self.p1.score}"
              f" \n Player 2: {self.p2.score} \n")
        self.final_results()
        self.reset_scores()

    def reset_scores(self):
        self.p1.score = 0
        self.p2.score = 0


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.set_rounds()
    game.play_game()
