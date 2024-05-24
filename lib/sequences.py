#!/usr/bin/env python3

def print_fibonacci(length):
   if length == 0:
        print('[]')
   elif length == 1:
        print('[0]')
   else:
        fib = [0, 1]
        for i in range(2, length):
            fib.append(fib[i - 1] + fib[i - 2])
        print('[' + ', '.join(map(str, fib)) + ']')