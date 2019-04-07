#!/usr/bin/env python

def int_input():
    text = input()
    return int(text)

def loop(count, func):
    for x in range(0, count):
        func(x)

def print_case(count, fmt, *args, **kw):
    prefix = 'Case #{}:'.format(count + 1)
    if len(args):
        print(prefix, fmt.format(*args, **kw))
    else:
        print(prefix, fmt)

def b(path):
    return ''.join('E' if p == 'S' else 'S' for p in path)

def solution(count):
    n = int_input()
    s = input()
    assert len(s) == 2 * n - 2

    m = b(s)
    print_case(count, m)

if __name__ == '__main__':
    count = int_input()
    loop(count, solution)
