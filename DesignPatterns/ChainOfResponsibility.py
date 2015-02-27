#!/usr/bin/env python

__author__ = 'avimehenwal'
__date__ = '27-Feb-2015'
__purpose__ = 'Chain Of Responsibility Design Pattern'

"""
1. The Chain of Responsibility pattern is used when we want to give a chance to multiple objects to satisfy a single request, or when we don't know which object (from a chain of objects) should process a specific request in advance. The principle is the same as the following:

There is a chain (linked list, tree, or any other convenient data structure) of objects.
We start by sending a request to the first object in the chain.
The object decides whether it should satisfy the request or not.
The object forwards the request to the next object.
This procedure is repeated until we reach the end of the chain.

2. The motivation behind Chain of Responsibility pattern is to create a system that can serve different requests in a hierarchical manner. In other words if an object that is a part of the system does not know how to respond to the given request it passes it along the object tree. As the name implies, each object along the route of the request can take the responsibility and serve the request.

3.
"""

class Event:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Widget:
    def __init__(self, parent=None):
        self.parent = parent

    def handle(self, event):
        handler = 'handle_{}'.format(event)
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        elif self.parent:
            self.parent.handle(event)
        elif hasattr(self, 'handle_default'):
            self.handle_default(event)


class MainWindow(Widget):
    def handle_close(self, event):
        print('MainWindow: {}'.format(event))

    def handle_default(self, event):
        print('MainWindow Default: {}'.format(event))


class SendDialog(Widget):
    def handle_paint(self, event):
        print('SendDialog: {}'.format(event))


class MsgText(Widget):
    def handle_down(self, event):
        print('MsgText: {}'.format(event))


def main():
    mw = MainWindow()
    sd = SendDialog(mw)
    msg = MsgText(sd)

    for e in ('down', 'paint', 'unhandled', 'close'):
        evt = Event(e)
        print('\nSending event -{}- to MainWindow'.format(evt))
        mw.handle(evt)
        print('Sending event -{}- to SendDialog'.format(evt))
        sd.handle(evt)
        print('Sending event -{}- to MsgText'.format(evt))
        msg.handle(evt)


if __name__ == '__main__':
    main()