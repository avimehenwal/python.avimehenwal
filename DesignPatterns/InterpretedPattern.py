#!/usr/bin/env python

__author__ = 'avimehenwal'
__date__ = '10-March-2015'
__purpose__ = 'Interpreted Design Pattern'


"""
1. specifies how to evaluate sentences in a language. The basic idea is to have a class for each symbol (terminal or nonterminal) in a specialized computer language. The syntax tree of a sentence in the language is an instance of the composite pattern and is used to evaluate (interpret) the sentence for a client.[1]:243 See also Composite pattern.

2. Uses for the Interpreter pattern
    - Specialized database query languages such as SQL.
    - Specialized computer languages which are often used to describe communication protocols.
    - Most general-purpose computer languages actually incorporate several specialized languages.

3. The following Backus-Naur Form example illustrates the interpreter pattern
        expression ::= plus | minus | variable | number
        plus ::= expression expression '+'
        minus ::= expression expression '-'
        variable  ::= 'a' | 'b' | 'c' | ... | 'z'
        digit = '0' | '1' | ... | '9'
        number ::= digit | digit number

4. In computer programming with object-oriented programming languages, duck typing is a style of typing in which an object's methods and properties determine the valid semantics, rather than its inheritance from a particular class or implementation of an explicit interface.
For example, in a non-duck-typed language, one would create a function that requires that the object passed into it be of type Duck, in order to ensure that that function can then use the object's walk and quack methods. In a duck-typed language, the function would take an object of any type and simply call its walk and quack methods, producing a run-time error if they are not defined. Instead of specifying types formally, duck typing practices rely on documentation, clear code, and testing to ensure correct use.

"""

class Duck:
    def quack(self):
        print("Quaaaaaack!")
    def feathers(self):
        print("The duck has white and gray feathers.")

class Person:
    def quack(self):
        print("The person imitates a duck.")
    def feathers(self):
        print("The person takes a feather from the ground and shows it.")
    def name(self):
        print("John Smith")

def in_the_forest(duck):
    duck.quack()
    duck.feathers()

def game():
    donald = Duck()
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)

game()