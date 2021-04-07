#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# coding: utf-8
"""
"""
import unittest

from . import ThreadPool


def add_one(input_list: list):
    for index in range(len(input_list)):
        input_list[index] += 1


def exception():
    raise ValueError('test this')


class TestThreadPool(unittest.TestCase):

    def test_basic_queue_count(self):
        with ThreadPool(1) as thread_pool:
            count = thread_pool.count()
        self.assertEqual(0, count)

    def test_basic_thread(self):
        a = [0, 0, 0]
        with ThreadPool(1) as thread_pool:
            thread_pool.add_task(add_one, a)
        self.assertEqual(3, sum(a))

    def test_map_thread(self):
        a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        with ThreadPool(3) as thread_pool:
            thread_pool.map(add_one, a)
        for i in a:
            self.assertEqual(3, sum(i))

    def test_map_sleep(self):
        import time
        from datetime import datetime, timedelta
        task_args = [x for x in range(10)]
        task_count = len(task_args)
        start_time = datetime.utcnow()
        print(f'{task_count} to work')
        with ThreadPool(9) as pool:
            pool.map(time.sleep, task_args)
        duration = (datetime.utcnow() - start_time).total_seconds()
        self.assertGreater(duration, 10)
