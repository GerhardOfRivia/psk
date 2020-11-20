#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# coding: utf-8
"""
My super simple and clean thread pool
"""

import time
import logging
from datetime import datetime, timedelta
from threading import Thread, Event
from queue import Queue, Empty
from contextlib import ContextDecorator

logger = logging.getLogger()
TIMEOUT = 60


class Manager(Thread):
    """ Thread manages queue """

    def __init__(self, name: str, task_queue: Queue, **kwargs):
        super().__init__(name=name, kwargs=kwargs)
        self.task_queue = task_queue
        self.daemon = True
        self.event = Event()
        self.start()

    def run(self):
        logger.debug(f'{self.name} running')
        self.task_queue.join()
        self.event.set()
        logger.debug(f'{self.name} shutting down')


class TaskWorker(Thread):
    """ Thread executing tasks from a given tasks queue """
    def __init__(self, name: str, task_queue: Queue, **kwargs):
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
        logger.info(f'creating {self.__class__.__name__} with {num_threads} threads')
        if num_threads < 1:
            raise ValueError('invalid number of threads')
        self.num_threads = num_threads
        self._task_queue = Queue()
        self._thread_pool = []
        self._manager = None

    def count(self):
        """ Get approximate number of tasks on queue queue """
        return self._task_queue.qsize()

    def add_task(self, func, *args, **kwargs):
        """ Add a task to the queue """
        logger.debug('task being added to queue {}'.format(func))
        self._task_queue.put((func, args, kwargs))

    def map(self, func, args_list):
        """ Add a list of tasks to the queue """
        logger.debug('map agrs_list to queue {}'.format(func))
        for args in args_list:
            self.add_task(func, args)

    def _status_manager(self):
        timeout_dt = datetime.utcnow() + timedelta(seconds=TIMEOUT)
        while True:
            try:
                current_time = datetime.utcnow()
                if self._manager.event.is_set():
                    logger.info(f'manager complete event {self._manager.event.is_set()}')
                    break
                if current_time > timeout_dt:
                    logger.info(f'timeout complete current {current_time} timeout {timeout_dt}')
                    break
                time.sleep(1)
            except Exception as e:
                # An exception happened in the main execution thread
                logger.exception(e)

    def __enter__(self):
        """ Start the threads and pass the task_queue """
        logger.info(f'Starting {self.num_threads} workers for ThreadPool')
        for i in range(self.num_threads):
            t = TaskWorker(f'{self.__class__.__name__}-{i}-{self.num_threads}', self._task_queue)
            self._thread_pool.append(t)
        return self

    def __exit__(self, exc_type, exc, exc_tb):
        """ Wait for threads to complete """
        logger.info(f'Waiting for tasks on {self.__class__.__name__} to complete')
        self._manager = Manager(f'{self.__class__.__name__}-manager', self._task_queue)
        try:
            if exc_type is None:
                self._status_manager()
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
    with ThreadPool(20) as pool:
        pool.map(time.sleep, task_args)
        logger.info(f'Task count {task_count} vs queue_count {pool.count()}')
    logger.info(f'Complete')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
