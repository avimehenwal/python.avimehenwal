#!/usr/bin/env python

__author__ = 'avimehenwal'
__date__ = '20-Feb-2015'
__purpose__ = 'Adapter Design Pattern'

"""
1. In software engineering, the adapter pattern is a software design pattern that allows the interface of an existing class to be used from another interface.[1] It is often used to make existing classes work with others without modifying their source code.

2. Structural design patterns deal with the relationships between the entities (such as classes and objects) of a system. A structural design pattern focuses on providing a simple way of composing objects for creating new functionality

3. Two types Object Adapter Pattern and Class Adapter Pattern

4. Grok is a Python framework that runs on top of Zope 3 and focuses on agile development. The Grok framework uses Adapters for making it possible for existing objects to conform to specific APIs without the need to modify them [j.mp/grokada].

5.
"""

class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def paint(self, factory):
        point = factory.getPoint()
        corner = factory.getCorner()

        show = corner.leftUp()
        show += point.line(self.width - 2)
        show += corner.rightUp()
        print(show)

        for i in range(self.height -2):
            show = point.line(self.width)
            print(show)

        show = corner.leftDown()
        show += point.line(self.width - 2)
        show += corner.rightDown()
        print(show)


class Dot:
    def line(self, width):
        point = ""
        for i in range(width):
            point +="-"
        return point


class Sharp:
    def leftUp(self):
        return "#"
    def rightUp(self):
        return "#"
    def leftDown(self):
        return "#"
    def rightDown(self):
        return "#"


class DotSharpFactory:
    def getPoint(self):
        return Dot()
    def getCorner(self):
        return Sharp()


def main():
    rect = Rectangle(20, 10)
    rect.paint(DotSharpFactory())


if __name__ == '__main__':
    main()
