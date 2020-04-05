__author__ = "liwen"
__time__ = "1:19 下午"

from itertools import permutations
from random import randint

exps = (
    '((%s %s %s) %s %s) %s %s',
    '(%s %s %s) %s (%s %s %s)',
    '(%s %s (%s %s %s)) %s %s',
    '%s %s ((%s %s %s) %s %s)',
    '%s %s (%s %s (%s %s %s))',
)

ops = r"+-*/"

def check(exp):
    try:
        return int(eval(exp)) == 24
    except:
        return False


def test24(v):
    result = []
    for a in permutations(v):
        print(a)
        t = [exp % (a[0],op1,a[1],op2,a[2],op3,a[3]) for op1 in ops for op2 in ops for op3 in ops for exp in exps
             if check(exp %(a[0], op1, a[1], op2, a[2], op3, a[3]))]
        if t:
            result.append(t)
    return result

lst = [randint(1,15) for j in range(4)]
r = test24(lst)
print(r)