#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# coding: utf-8
"""
Solve a tic-tac-toe problem
"""
import sys
import logging

logger = logging.getLogger()


class TicTacToe:

    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.player = "X"

    def __str__(self):
        return "\n".join([str(row) for row in self.board])

    def get_input(self):
        while True:
            try:
                row = int(input(f"({self.player}) Enter row (0-2): "))
                col = int(input(f"({self.player}) Enter column (0-2): "))
                if row >= len(self.board) or col >= len(self.board):
                    raise ValueError()
                if self.board[row][col] is not None:
                    raise RuntimeError()
                self.board[row][col] = self.player
                break
            except ValueError:
                print("invalid input only numbers smaller than three", file=sys.stderr)
            except RuntimeError:
                print("invalid input spot taken", file=sys.stderr)
        self.player = "O" if self.player == "X" else "X"

    def complete(self):
        for row in range(3):
            for col in range(3):
                z = self.board[row][col]
                if z is None:
                    continue
        return False

    def play(self):
        while True:
            print(self)
            if self.complete():
                return
            self.get_input()
            print(self)
