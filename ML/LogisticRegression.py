import numpy as np
import matplotlib.pyplot as plt


def prod(w, X):
    return np.dot(w.T, X)


def sigmoid(s):
    return 1 / (1 + np.exp(-s))


def my_logistic_sigmoid_regression(X, y, w_init, eta, epsilon=1e-3, M=10000):
    w = [w_init]
    N = X.shape[1]
    d = X.shape[0]
    count = 0
    check_w_after = 20
    while count < M:
        # mix data
        mix_id = np.random.permutation(N)
        for i in mix_id:
            xi = X[:, i].reshape(d, 1)
            yi = y[i]
            zi = sigmoid(np.dot(w[-1].T, xi))
            w_new = w[-1] + eta * (yi - zi) * xi
            count += 1
            # stopping criteria
            if count % check_w_after == 0:
                if np.linalg.norm(w_new - w[-check_w_after]) < epsilon:
                    return w
            w.append(w_new)
    return w


if __name__ == '__main__':

    X = np.array([[10, 5, 7, 4, 4, 5, 8, 8, 7, 6], [
                 1, 2, 1, 2.5, 1, 0.5, 0.5, 1, 0.3, 0.3]])
    y = np.array([1, 1, 1, 1, 0, 0, 0, 1, 0, 0])

    # extended data
    Xbar = np.concatenate((np.ones((1, X.shape[1])), X), axis=0)
    epsilon = .05
    d = Xbar.shape[0]
    w_init = np.random.randn(d, 1)
    w = my_logistic_sigmoid_regression(Xbar, y, w_init, epsilon)
    print(w[-1].T)

   #  cau b
    x_predict = np.array([[100], [1]])
    x_predict_bar = np.concatenate(
        (np.ones((1, x_predict.shape[1])), x_predict), axis=0)

    print(x_predict_bar)
    result = sigmoid(np.dot(w[-1].T, x_predict_bar))

    if result >= 0.5:
        print("label C: ", 1)
    else:
        print("label C: ", 0)
