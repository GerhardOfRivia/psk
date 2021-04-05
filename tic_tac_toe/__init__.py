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

    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self._players = [Player("O"), Player("X")]

    def __str__(self):
        return "\n".join([str(row) for row in self.board])

    def get_input(self, player_index):
        input_try = 0
        while True:
            if input_try > 3:
                exit(1)
            try:
                player = self._players[player_index]
                row, col = player.get_input()
                if row >= len(self.board) or col >= len(self.board):
                    raise ValueError()
                if self.board[row][col] is not None:
                    raise RuntimeError()
                self.board[row][col] = player.symbol
                break
            except ValueError:
                print("invalid input only numbers smaller than three", file=sys.stderr)
            except RuntimeError:
                print("invalid input spot taken", file=sys.stderr)
            input_try += 1

    def complete(self):
        for i in range(3):
            if self.board[i][0] is None:
                continue
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                print(f"{self.board[i][0]} {self.board[i][1]} {self.board[i][2]}")
                return True
            if self.board[0][i] is None:
                continue
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                print(f"{self.board[0][i]}\n{self.board[1][i]}\n{self.board[2][i]}")
                return True
        if self.board[1][1] is None:
            return False
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
            self.get_input(turn % 2)
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

    def get_input(self) -> tuple:
        return self.logic()

    def from_user(self):
        row = int(input(f"({self.symbol}) Enter row (0-2): "))
        col = int(input(f"({self.symbol}) Enter column (0-2): "))
        return row, col

    def from_random(self):
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        print(f"({self.symbol}) Selected row (0-2): {row}")
        print(f"({self.symbol}) Selected col (0-2): {col}")
        return row, col

    def from_brain(self):
        pass
