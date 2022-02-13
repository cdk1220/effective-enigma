""" This file implements classes for stacks and queues """
from copy import deepcopy


class Stack:
    def __init__(self):
        self.__array = []

    def push(self, value: int):
        self.__array.append(value)

    def pop(self):
        if len(self.__array) > 0:
            return self.__array.pop()
        else:
            raise LookupError("Trying to pop empty stack !!!")

    def peak(self):
        if len(self.__array) > 0:
            return deepcopy(self.__array[-1])
        else:
            raise LookupError("Trying to peak empty stack !!!")


class Queue:
    def __init__(self):
        self.__array = []

    def enqueue(self, value: int):
        self.__array.append(value)

    def dequeue(self):
        if len(self.__array) > 0:
            return self.__array.pop(0)
        else:
            raise LookupError("Trying to dequeue empty queue !!!")

    def peak(self):
        if len(self.__array) > 0:
            return deepcopy(self.__array[0])
        else:
            raise LookupError("Trying to peak empty queue !!!")