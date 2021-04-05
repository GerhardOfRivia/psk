#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# coding: utf-8
"""
Solve a tic-tac-toe problem
https://jrms-random-blog.blogspot.com/2021/03/a-google-interview-question.html
"""

import logging

from tic_tac_toe import TicTacToe, Player

logger = logging.getLogger()


def main():
    t = TicTacToe(0)
    t.play()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        logger.exception(err)
