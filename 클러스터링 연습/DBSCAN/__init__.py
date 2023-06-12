import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN

# 예시 데이터 생성
np.random.seed(42)
X, y = make_moons(n_samples=200, noise=0.05)

# DBSCAN 클러스터링 수행
dbscan = DBSCAN(eps=0.3, min_samples=5)
labels = dbscan.fit_predict(X)

# 클러스터 할당 결과 시각화
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('DBSCAN Clustering')
plt.show()
