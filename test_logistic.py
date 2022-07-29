import math
from numpy import log1p

def stable_logistic(input, target):
    y = input * target
    if(y > 0):
        return log1p(math.exp(-1 * y))
    return (log1p(math.exp(y)) - y)