#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# coding: utf-8
"""
"""
import unittest

from tic_tac_toe import TicTacToe


class TestTicTacToe(unittest.TestCase):

    def test_incomplete(self):
        t = TicTacToe(0)
        t.board = [
            ["X", "X", None],
            [None, None, None],
            [None, None, None],
        ]
        complete = t.complete()
        self.assertFalse(complete)

    def test_complete_top(self):
        t = TicTacToe(0)
        t.board = [
            ["X", "X", "X"],
            [None, None, None],
            [None, None, None],
        ]
        complete = t.complete()
        self.assertTrue(complete)

    def test_complete_bottom(self):
        t = TicTacToe(0)
        t.board = [
            [None, None, None],
            [None, None, None],
            ["X", "X", "X"],
        ]
        complete = t.complete()
        self.assertTrue(complete)

    def test_complete_middle(self):
        t = TicTacToe(0)
        t.board = [
            [None, None, None],
            ["X", "X", "X"],
            [None, None, None],
        ]
        complete = t.complete()
        self.assertTrue(complete)

    def test_complete_up_one(self):
        t = TicTacToe(0)
        t.board = [
            ["X", None, None],
            ["X", None, None],
            ["X", None, None],
        ]
        complete = t.complete()
        self.assertTrue(complete)

    def test_complete_two(self):
        t = TicTacToe(0)
        t.board = [
            [None, "X", None],
            [None, "X", None],
            [None, "X", None],
        ]
        complete = t.complete()
        self.assertTrue(complete)

    def test_complete_three(self):
        t = TicTacToe(0)
        t.board = [
            [None, None, "X"],
            [None, None, "X"],
            [None, None, "X"],
        ]
        complete = t.complete()
        self.assertTrue(complete)

    def test_complete_down(self):
        t = TicTacToe(0)
        t.board = [
            ["X", None, None],
            [None, "X", None],
            [None, None, "X"],
        ]
        complete = t.complete()
        self.assertTrue(complete)

    def test_complete_up(self):
        t = TicTacToe(0)
        t.board = [
            [None, None, "X"],
            [None, "X", None],
            ["X", None, None],
        ]
        complete = t.complete()
        self.assertTrue(complete)
