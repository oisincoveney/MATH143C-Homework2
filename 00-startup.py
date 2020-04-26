from sympy import *
import numpy as np
import pandas as pd
import scipy as sp
import math
import array_to_latex as a2l
import pyperclip as pyp
from sympy.core.rules import Transform
import functools
import matplotlib.pyplot as plt

x = symbols('x')

def tex(a):
    pyp.copy(latex(a))

def get_diffs(eq, num=2, var=x):
    eqs = [eq]
    for i in range(num):
        eqs.append(eqs[i].diff(x))
    return eqs

def eq_round(expr):
    return expr.xreplace(Transform(lambda x: x.round(6), lambda x: isinstance(x, Float)))

def xterms(start, stop, X):
    if stop - start == 0:
        return sympify(1)
    return functools.reduce(lambda a, b: a * b, [(x - i) for i in X[start:stop]])

def atl(arr):
    a2l.to_ltx(arr, frmt='{:6.6f}', arraytype='array')

def atc(arr):
    a2l.to_clp(arr, frmt='{:6.6f}', arraytype='array')