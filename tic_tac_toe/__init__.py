#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# coding: utf-8
"""
Solve a tic-tac-toe problem
"""
import sys
import random
import logging

logger = logging.getLogger()


class TicTacToe:

    def __init__(self, number_of_players):
        self.size = 3
        self.board = [[None for _ in range(self.size)] for _ in range(self.size)]
        self._players = self._generate_players(number_of_players)

    def __str__(self):
        return "\n".join([str(row) for row in self.board])

    @staticmethod
    def _generate_players(number_of_players):
        if number_of_players == 0:
            return [Player("X"), Player("O")]
        elif number_of_players == 1:
            return [Player("X", "input"), Player("O")]
        elif number_of_players == 2:
            return [Player("X", "input"), Player("O", "input")]
        else:
            raise ValueError("What game are you playing? (0-2)")

    def get_input(self, player):
        row, col = player.get_input(self)
        self.board[row][col] = player.symbol

    def complete(self):
        for i in range(self.size):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                print(f"{self.board[i][0]} {self.board[i][1]} {self.board[i][2]}")
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                print(f"{self.board[0][i]}\n{self.board[1][i]}\n{self.board[2][i]}")
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            print(f"{self.board[0][0]}\\{self.board[1][1]}\\{self.board[2][2]}")
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            print(f"{self.board[0][2]}/{self.board[1][1]}/{self.board[2][0]}")
            return True
        return False

    def play(self):
        turn = 0
        while True:
            if turn == 9:
                print(f"GameOver\n{self}")
            if self.complete():
                return
            player = self._players[turn % 2]
            self.get_input(player)
            print(f"{turn}\n{self}")
            turn += 1


class Player:

    def __init__(self, symbol, logic: str = "random"):
        self.symbol = symbol
        if logic == "random":
            self.logic = self.from_random
        elif logic == "input":
            self.logic = self.from_user
        elif logic == "brain":
            self.logic = self.from_brain
        else:
            raise ValueError("Invalid ")

    def __str__(self):
        return self.symbol

    def get_input(self, tic_tac_toe: TicTacToe) -> tuple:
        while True:
            try:
                row, col = self.logic(tic_tac_toe)
                if row >= len(tic_tac_toe.board) or col >= len(tic_tac_toe.board):
                    raise ValueError()
                if tic_tac_toe.board[row][col] is not None:
                    raise RuntimeError()
                return row, col
            except ValueError:
                print("invalid input only numbers smaller than three", file=sys.stderr)
            except RuntimeError:
                print("invalid input spot taken", file=sys.stderr)

    @staticmethod
    def _get_options(tic_tac_toe: TicTacToe):
        options = list()
        for row in range(0, 3):
            for col in range(0, 3):
                if tic_tac_toe.board[row][col] is None:
                    options.append((row, col))
        return options

    def from_user(self, tic_tac_toe: TicTacToe):
        options = self._get_options(tic_tac_toe)
        print(f"Options: {options}")
        row = int(input(f"({self.symbol}) Enter row (0-2): "))
        col = int(input(f"({self.symbol}) Enter column (0-2): "))
        return row, col

    def from_random(self, tic_tac_toe: TicTacToe):
        options = self._get_options(tic_tac_toe)
        index = random.randint(0, len(options)-1)
        row, col = options[index]
        print(f"({self.symbol}) Selected row (0-2): {row}")
        print(f"({self.symbol}) Selected col (0-2): {col}")
        return row, col

    def from_brain(self, tic_tac_toe: TicTacToe):
        pass
