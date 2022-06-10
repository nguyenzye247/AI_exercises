import numpy as np


class Kmean:
    def __init__(self, data, K):
        X = np.array(data)
        centroids, idx = self.find_k_means(X, K)
        self.idx = idx
        self.centroids = centroids

    def initialize_K_centroids(self, X, K):
        m, n = X.shape
        k_rand = np.ones((K, n))
        # Chon k cai tam ngau nhien
        k_rand = X[np.random.choice(range(len(X)), K, replace=False), :]
        return k_rand

    def find_closest_centroids(self, X, centroids):
        m = len(X)
        c = np.zeros(m)
        for i in range(m):
            # tinh khoang cach tu diem X[i] den k tam
            # vd: distances = [ 69.37709259  41.80362193 126.33989712 181.10241081] (k = 4)
            distances = np.linalg.norm(X[i] - centroids, axis=1)
            # chon khoang cach nho nhat trong k khoang cach sau do lay index cua no
            c[i] = np.argmin(distances)
        return c

    def compute_means(self, X, idx, K):
        m, n = X.shape
        centroids = np.zeros((K, n))
        for k in range(K):
            points_belong_k = X[np.where(idx == k)]
            centroids[k] = np.mean(points_belong_k, axis=0)
        return centroids

    def find_k_means(self, X, K):
        _, n = X.shape
        centroids = self.initialize_K_centroids(X, K)
        centroid_history = [centroids]

        while True:
            idx = self.find_closest_centroids(X, centroids)
            centroids = self.compute_means(X, idx, K)

            if (centroid_history[-1] == centroids).all():
                break
            else:
                centroid_history.append(centroids)

        return centroids, idx


if __name__ == '__main__':

    X = np.array([[0, 3], [2, 0], [3, 0], [1, 4]])

    kmean = Kmean(X, K=2)
    print("Tam cac cum: \n", kmean.centroids)
    print("Cac diem: ", end='')
    [print(X[i], end=' ') for i in range(len(X))]
    print("")
    print("Nhan cua cac dem: ", kmean.idx)
