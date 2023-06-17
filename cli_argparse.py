#!/usr/bin/python3
# python idle-type calculator, much of the code is from https://learnbyexample.github.io/practice_python_projects/calculator/exercises.html
# code has been modified by me

import argparse, sys
from math import *

parser = argparse.ArgumentParser()
parser.add_argument('ip_expr', nargs="?",
                    help="input expression to be evaluated")
parser.add_argument('-F', action='store_true',
                    help="Used if no pointer precision is needed")
parser.add_argument('-f', type=int,
                    help="specify floating point output precision")
parser.add_argument('-b', action="store_true",
                    help="output in binary format")
parser.add_argument('-o', action="store_true",
                    help="output in octal format")
parser.add_argument('-x', action="store_true",
                    help="output in hexadecimal format")
parser.add_argument('-v', action="store_true",
                    help="verbose mode, shows both input and output")
args = parser.parse_args()

if args.ip_expr in (None, '-'):
    args.ip_expr = sys.stdin.readline().strip()

try:
    result = eval(args.ip_expr)
    if args.b:
        print(f"{int(result):b}#b")
    elif args.o:
        print(f"{int(result):o}#o")
    elif args.x:
        print(f"{int(result):x}#x")
    
    if args.v:
        print(f"{args.ip_expr} = {result}")
    else: 
        if type(result) == float:
            if args.F:
                print(result)
            elif not args.f:
                print(f"{result:.2f}")
            else:
                print(f"{result:.{args.f}f}") 
        else:
            print(result)
except (NameError, SyntaxError):
    print("invalid expression")

            
