#!/usr/bin/env python

__author__ = 'avimehenwal'
__date__ = '19-Feb-2015'
__purpose__ = 'Factory Method Design Pattern'

"""
1. Factory method pattern is a creational pattern. Enables Polymorphism

2. deal with the problem of creating objects without specifying the exact class of object that will be created. This is done by creating objects via calling a factory method—either specified in an interface and implemented by child classes, or implemented in a base class and optionally overridden by derived classes—rather than by calling a constructor.

3.The factory method pattern should not be confused with the more general notion of factories and factory methods. The factory method pattern is the best-known use of factories and factory methods, but not all uses of factory methods are examples of the factory method pattern

4. Intent : Define an interface for creating an object, but let subclasses decide which class to instantiate. Factory Method lets a class defer instantiation to subclasses.
Defining a "virtual" constructor.

5. Standard Interface for creating objects from classes.

6.  (a) track an object creation
    (b) decouple an object creation from an object usage, or even
    (c) improve the performance and resource usage of an application.
"""

import xml.etree.ElementTree as etree
import json

class JSONConnector:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)


def connect_to(filepath):
    factory = None
    try:
       factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory


def main():
    sqlite_factory = connect_to('data/person.sq3')
    print()

    xml_factory = connect_to('data/person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Liar'))
    print('found: {} persons'.format(len(liars)))
    for liar in liars:
        print('first name: {}'.format(liar.find('firstName').text))
        print('last name: {}'.format(liar.find('lastName').text))
        [print('phone number ({}):'.format(p.attrib['type']), p.text) for p in liar.find('phoneNumbers')]
    print()

    json_factory = connect_to('data/donut.json')
    json_data = json_factory.parsed_data
    print('found: {} donuts'.format(len(json_data)))
    for donut in json_data:
    print('name: {}'.format(donut['name']))
    print('price: ${}'.format(donut['ppu']))
    [print('topping: {} {}'.format(t['id'], t['type'])) for t in donut['topping']]

if __name__ == '__main__':
    main()