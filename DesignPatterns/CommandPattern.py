#!/usr/bin/env python

__author__ = 'avimehenwal'
__date__ = '27-Feb-2015'
__purpose__ = 'Command Design Pattern'


"""
1. the command pattern is a behavioral design pattern in which an object is used to represent and encapsulate all the information needed to call a method at a later time. This information includes the method name, the object that owns the method and values for the method parameters.

2. Four terms always associated with the command pattern are command, receiver, invoker and client. A command object has a receiver object and invokes a method of the receiver in a way that is specific to that receiver's class. The receiver then does the work. A command object is separately passed to an invoker object, which invokes the command, and optionally does bookkeeping about the command execution. Any command object can be passed to the same invoker object. Both an invoker object and several command objects are held by a client object. The client contains the decision making about which commands to execute at which points. To execute a command, it passes the command object to the invoker object

3.
"""

from abc import ABCMeta
from abc import abstractmethod
import inspect
import os

class Command(object):
    """
    Abstract / Interface base class for commands.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class CreateCommand(Command):
    """
    Create command implementation.
    """
    def __init__(self, name):
        self.file_name = name

    def execute(self, name):
        open(self.file_name, 'w')
        print str(self) + ':::Method:::' + inspect.stack()[0][3]

    def undo(self):
        os.remove(self.file_name)
        print str(self) + ':::Method:::' + inspect.stack()[0][3]


class MoveCommand(Command):
    """
    Move command implementation.
    """
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self, src, dest):
        os.rename(self.src, self.dest)
        print str(self) + ':::Method:::' + inspect.stack()[0][3]

    def undo(self):
        os.rename(self.dest, self.src)
        print str(self) + ':::Method:::' + inspect.stack()[0][3]


class Invoker(object):

    def __init__(self, command):
        self.command = command

    def do(self):
        self.command.execute()

    def undo(self):
        self.command.undo()


# Client for the command pattern
if __name__ == '__main__':
    create_cmd = CreateCommand('/tmp/foo.txt')
    move_cmd = MoveCommand('/tmp/foo.txt', '/tmp/bar.txt')
    create_invoker = Invoker(create_cmd)
    move_invoker = Invoker(move_cmd)
    create_invoker.do()
    move_invoker.do()
    move_invoker.undo()
    create_invoker.undo()