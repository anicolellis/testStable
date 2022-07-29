import math

def stable_binary_cross_entropy(input, target):
    max_val = max(target, 0)
    return input - input * target + max_val + math.log(math.exp(-1 * max_val) + math.exp(-1 * (input + max_val)))