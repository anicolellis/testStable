import math

def stable_poisson(input, target, eps):
    return input - target * math.log(input + eps)

def stable_poisson_exp(input, target):
    return math.exp(input) - target * input

def test_poisson():
    assert stable_poisson(0.5, 0.0, 1e-8) == 0.0
    assert stable_poisson(0.5, 0.5, 0.5) == 0.5

def test_poisson_exp():
    assert stable_poisson_exp(0.0, 0.5) == 1.0
    assert stable_poisson_exp(1.0, 0.0) == math.e