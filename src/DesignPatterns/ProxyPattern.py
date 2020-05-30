#!/usr/bin/env python

__author__ = 'avimehenwal'
__date__ = '27-Feb-2015'
__purpose__ = 'Proxy Design Pattern'

"""
1. In some applications, we want to execute one or more important action before accessing an object. An example is accessing sensitive information. Before allowing any user to access sensitive information, we want to make sure that the user has sufficient privileges

2. A remote proxy,
 which acts as the local representation of an object that really exists in a different address space (for example, a network server).
A virtual proxy,
 which uses lazy initialization to defer the creation of a computationally expensive object until the moment it is actually needed.
A protection/protective proxy,
 which controls access to a sensitive object.
A smart (reference) proxy,
 which performs extra actions when an object is accessed. Examples of such actions are reference counting and thread-safety checks.

3. There are two basic, different kinds of lazy initialization in OOP. They are as follows:
At the instance level: This means that an object's property is initialized lazily, but the property has an object scope. Each instance (object) of the same class has its own (different) copy of the property.
At the class or module level: In this case, we do not want a different copy per instance, but all the instances share the same property, which is lazily initialized. This case is not covered in this chapter. If you find it interesting, consider it as an exercise.

4. Example : This means that you cannot make any transactions without physically presenting the card and knowing the PIN
An Object-Relational Mapping (ORM) API is also an example of how to use a remote proxy

5. A proxy, in its most general form, is a class functioning as an interface to something else. The proxy could interface to anything: a network connection, a large object in memory, a file, or some other resource that is expensive or impossible to duplicate.

6.

"""

class SensitiveInfo:
    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    def read(self):
        print('There are {} users: {}'.format(len(self.users), ' '.join(self.users)))

    def add(self, user):
        self.users.append(user)
        print('Added user {}'.format(user))


class Info:
    '''protection proxy to SensitiveInfo'''

    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = '0xdeadbeef'

    def read(self):
        self.protected.read()

    def add(self, user):
        sec = input('what is the secret? ')
        self.protected.add(user) if sec == self.secret else print("That's wrong!")


def main():
    info = Info()

    while True:
        print('1. read list |==| 2. add user |==| 3. quit')
        key = input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            exit()
        else:
            print('unknown option: {}'.format(key))

if __name__ == '__main__':
    main()