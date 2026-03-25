"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable, List

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.

def mul(x: float, y: float):
    return x * y


def id(x: float):
    return x


def add(x: float, y: float):
    return x + y


def neg(x: float):
    return -x


def lt(x: float, y: float):
    return x < y


def eq(x: float, y: float):
    return x == y


def max(x: float, y: float):
    return x if x > y else y


def is_close(x: float, y: float):
    return abs(x - y) < 1e-2


def sigmoid(x: float):
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    else:
        ex = math.exp(x)
        return ex / (1.0 + ex)


def relu(x: float):
    return x if x > 0 else 0.0


def log(x: float):
    return math.log(x)


def exp(x: float):
    return math.exp(x)


def inv(x: float):
    return 1.0 / x


def log_back(x: float, y: float):
    return y / x


def inv_back(x: float, y: float):
    return -y / (x * x)


def relu_back(x: float, y: float):
    return y if x > 0 else 0.0



# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists

def addLists(a: list[float], b: list[float]):
    return (1,1)

def negList(ls: List[float]):
    return ls

def sum(ls: List[float]):
    return 3

def prod(ls: List[float]):
    return 3

# TODO: Implement for Task 0.3.
