"""
============================================
Utilities Library
============================================
"""
import difflib
import pprint
import inspect
import pickle
import os


class DictDiffer(object):
    """
    Calculate the difference between two dictionaries as:

    1) items added
    2) items removed
    3) keys same in both but changed values\n
    4) keys same in both and unchanged values
    5) dicts match
    5) partial match
    """
    
    def __init__(self, current_dict, past_dict):
        if not isinstance(current_dict, dict):
            raise TypeError('current_dict must be a dict')
        if not isinstance(past_dict, dict):
            raise TypeError('past_dict must be a dict')
        self.current_dict, self.past_dict = current_dict, past_dict
        self.set_current, self.set_past = set(current_dict.keys()), set(past_dict.keys())
        self.intersect = self.set_current.intersection(self.set_past)
        self.union = self.set_current.union(self.set_past)

    def added(self):
        '''returns items added in current dict'''
        return self.set_current - self.intersect 

    def removed(self):
        '''returns items removed in current dict'''
        return self.set_past - self.intersect 

    def changed(self):
        '''returns items changed in current dict'''
        return set(o for o in self.intersect if self.past_dict[o] != self.current_dict[o])

    def unchanged(self):
        '''returns items unchanged in current dict'''
        return set(o for o in self.intersect if self.past_dict[o] == self.current_dict[o])

    def diff(self):
        '''returns diff between current and past dict'''
        return self.union - self.intersect

    def ismatch(self):
        '''returns true if diference is empty. else returns false'''
        try:
            if len(self.current_dict) != len(self.past_dict):
                raise Exception('length of dicts not equal')
            for key in self.current_dict.iterkeys():
                if self.current_dict[key] != self.past_dict[key]:
                    raise Exception('values dont match')
        except Exception, err:
            return False
        return True




    
    

