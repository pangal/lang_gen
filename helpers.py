from __future__ import division, unicode_literals
import random
from random import randint as roll

def weighted_random(choices):
    ''' Taken from http://stackoverflow.com/questions/2570690/python-algorithm-to-randomly-select-a-key-based-on-proportionality-weight
        Takes an OrderedDict of choice:weight pairs as input (Uses OrderedDict to preserve random seed, since apparently
        python will change the iteration order of regular dictionaries each time, not linked to the random seed.  '''

    r = random.uniform(0, sum(choices.itervalues()))
    s = 0.0
    for k, w in choices.iteritems():
        s += w
        if r < s: return k
    return k

	
def chance(number, top=100):
    ''' A simple function for automating a chance (out of 100) of something happening '''
    return roll(1, top) <= number


def clamp(minimum, num, maximum):
    ''' Clamps the input num to ensure it sits between min and max '''
    return max(minimum, min(num, maximum))

def join_list(string_list, conjunction='and', oxford_comma='', null_value="nothing"):
    if len(string_list) == 0:
        return null_value
    if len(string_list) == 1:
        return string_list[0]
    elif len(string_list) == 2:
        return '{0} {1} '.format(oxford_comma, conjunction).join(string_list)
    else:
        return '{0}, {1} {2}'.format(', '.join([s for s in string_list[:-1]]), conjunction, string_list[-1])