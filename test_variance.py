def stable_variance(a, b, c):
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
    variance = S/(N-1)
    return variance

def test_variance():
    assert stable_variance(100.0, 100.0, 100.0) == 0.0

    assert stable_variance(100.0, 1000.0, 10000.0) == 29970000.0

    #assert stable_variance([1e-3, 1e-12, 1e-6]) == 3.330003329996666604003873086992104646242296439595520496368408203125e-07
    #assert unstable_variance([1e-3, 1e-12, 1e-6]) == 3.330003329996666604003873086992104646242296439595520496368408203125e-07