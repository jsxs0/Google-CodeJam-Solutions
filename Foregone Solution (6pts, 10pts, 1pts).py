#!/usr/bin/env python

def int_input():
    text = input()
    return int(text)

def float_input():
    text = input()
    return int(text)

def list_input(size=None):
    text = input()
    str_values = text.split(' ')
    if size is not None:
        assert len(str_values) == size
    return str_values

def intlist_input(size=None):
    return map(int, list_input(size))

def floatlist_input(size=None):
    return map(float, list_input(size))

def loop(count, func):
    for x in range(0, count):
        func(x)

def print_case(count, fmt, *args, **kw):
    prefix = 'Case #{}:'.format(count + 1)
    if len(args):
        print(prefix, fmt.format(*args, **kw))
    else:
        print(prefix, fmt)

import random

def find(pivot, n):
    if '4' not in str(pivot):
        if '4' not in str(n - pivot):
            return pivot, n - pivot
    if 1 < pivot-1:
        r = find(random.randint(1, pivot-1), n)
        if r is not None:
            return r
    if pivot+1 < n-1:
        r = find(random.randint(pivot+1, n-1), n)
        if r is not None:
            return r
    return None


def solution(count):
    n = int_input()
    a, b = find(random.randint(1, n-1), n)
    print_case(count, '{} {}', a, b)

if __name__ == '__main__':
    count = int_input()
    loop(count, solution)
