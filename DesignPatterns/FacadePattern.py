#!/usr/bin/env python

__author__ = 'avimehenwal'
__date__ = '23-Feb-2015'
__purpose__ = 'Facade Design Pattern'

"""
1. Facade is an abstraction layer implemented over an existing complex system.The Facade (also known as Façade) design pattern helps us to hide the internal complexity of our systems and expose only what is necessary to the client through a simplified interface [Eckel08, page 209].

2. Provides a single, simple entry point to a complex system. By introducing Facade, the client code can use a system by simply calling a single method/function. At the same time, the internal system does not lose any functionality. It just encapsulates it

3. Facade is also useful if you have more than one layer in your system. You can introduce one Facade entry point per layer, and let all layers communicate with each other through their Facades. That promotes loose coupling and keeps the layers as independent as possible

4. Examples, customer service department of a bank, or a company, and the keys that we use to turn a vehicle on
"""

from enum import Enum
from abc import ABCMeta, abstractmethod

State = Enum('State', 'new running sleeping restart zombie')

class User:
    pass


class Process:
    pass


class File:
    pass


class Server(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass


class FileServer(Server):
    def __init__(self):
        '''actions required for initializing the file server'''
        self.name = 'FileServer'
        self.state = State.new

    def boot(self):
        print('booting the {}'.format(self))
        '''actions required for booting the file server'''
        self.state = State.running

    def kill(self, restart=True):
        print('Killing {}'.format(self))
        '''actions required for killing the file server'''
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name, permissions):
        '''check validity of permissions, user rights, etc.'''

        print("trying to create the file '{}' for user '{}' with permissions {}".format(name, user, permissions))


class ProcessServer(Server):
    def __init__(self):
        '''actions required for initializing the process server'''
        self.name = 'ProcessServer'
        self.state = State.new

    def boot(self):
        print('booting the {}'.format(self))
        '''actions required for booting the process server'''
        self.state = State.running

    def kill(self, restart=True):
        print('Killing {}'.format(self))
        '''actions required for killing the process server'''
        self.state = State.restart if restart else State.zombie

    def create_process(self, user, name):
        '''check user rights, generate PID, etc.'''

        print("trying to create the process '{}' for user '{}'".format(name, user))


class WindowServer:
    pass


class NetworkServer:
    pass


class OperatingSystem:
    '''The Facade'''
    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [i.boot() for i in (self.fs, self.ps)]

    def create_file(self, user, name, permissions):
        return self.fs.create_file(user, name, permissions)

    def create_process(self, user, name):
        return self.ps.create_process(user, name)


def main():
    os = OperatingSystem()
    os.start()
    os.create_file('foo', 'hello', '-rw-r-r')
    os.create_process('bar', 'ls /tmp')


if __name__ == '__main__':
    main()