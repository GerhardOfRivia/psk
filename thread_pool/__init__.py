#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# coding: utf-8
"""
My super simple and clean thread pool
"""

import time
import logging
from threading import Thread, Event
from queue import Queue, Empty
from contextlib import ContextDecorator

logger = logging.getLogger()
THREAD_COUNT = 20


class TaskWorker(Thread):
    """ Thread executing tasks from a given tasks queue """
    def __init__(self, name, task_queue, **kwargs):
        super().__init__(name=name, kwargs=kwargs)
        self.task_queue = task_queue
        self.daemon = True
        self.event = Event()
        self.start()

    def run(self):
        logger.info(f'{self.name} running')
        while True:
            try:
                if self.event.is_set():
                    break
                func, args, kwargs = self.task_queue.get(timeout=5)
                start_time = time.time()
                logger.debug('started task {} [{}]'.format(func.__name__, args))
                func(*args, **kwargs)
            except Empty:
                self.event.wait(1)
            except Exception as e:
                # An exception happened in this thread
                logger.exception(e)
                logger.info('failed %f', 0.0)
            else:  # executed if the try clause does not raise an exception
                self.task_queue.task_done()
                end_time = time.time()
                logger.info('complete %f', round(end_time - start_time, 6))
        logger.info(f'{self.name} shutting down')


class ThreadPool(ContextDecorator):
    """ Pool of threads consuming tasks from a queue """
    def __init__(self, num_threads):
        logger.info(f'Creating {self.__class__.__name__} with {num_threads} threads')
        self.num_threads = num_threads
        self.task_queue = Queue()
        self._thread_pool = []

    def count(self):
        """ Get approximate number of tasks on queue queue """
        return self.task_queue.qsize()

    def add_task(self, func, *args, **kwargs):
        """ Add a task to the queue """
        logger.debug('task being added to queue {}'.format(func))
        self.task_queue.put((func, args, kwargs))

    def map(self, func, args_list):
        """ Add a list of tasks to the queue """
        logger.debug('map agrs_list to queue {}'.format(func))
        for args in args_list:
            self.add_task(func, args)

    def __enter__(self):
        """ Start the threads and pass the task_queue """
        logger.info(f'Starting {self.num_threads} workers for ThreadPool')
        for i in range(self.num_threads):
            t = TaskWorker(f'{self.__class__.__name__}-{i}-{self.num_threads}', self.task_queue)
            self._thread_pool.append(t)
        return self

    def __exit__(self, exc_type, exc, exc_tb):
        """ Wait for threads to complete """
        logger.info(f'Waiting for {self.task_queue.qsize()} tasks on {self.__class__.__name__} to complete')
        try:
            if exc_type is None:
                self.task_queue.join()
                logger.info(f'Tasks on {self.__class__.__name__} complete')
            else:
                logger.error(f'Exception during thread execution: {exc}')
        finally:
            for thread in self._thread_pool:
                thread.event.set()
        return False


def main():
    task_args = [x for x in range(10)]
    task_count = len(task_args)
    logger.info(f'{task_count} to work')
    with ThreadPool(THREAD_COUNT) as pool:
        pool.map(time.sleep, task_args)
        logger.info(f'Task count {task_count} vs queue_count {pool.count()}')
    logger.info(f'Complete')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
