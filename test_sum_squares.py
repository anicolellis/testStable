def stable_sum_squares(a, b, c):
    X_vector = [a, b, c]
    M = 0
    S = 0
    N = len(X_vector)
    for i in range(0, N):
        x = X_vector[i]
        M_new = M + (x-M)/(i+1)
        S_new = S + (x-M)*(x-M_new)
        M = M_new
        S = S_new
    return S

def test_sum_squares():
    assert stable_sum_squares(100.0, 100.0, 100.0) == 0.0

    assert stable_sum_squares(100.0, 1000.0, 10000.0) == 29970000.0