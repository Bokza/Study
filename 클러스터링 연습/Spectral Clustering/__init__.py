import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.cluster import SpectralClustering

# 예시 데이터 생성
np.random.seed(42)
X, _ = make_moons(n_samples=200, noise=0.05)

# 스펙트럴 클러스터링 수행
spectral = SpectralClustering(n_clusters=2, affinity='nearest_neighbors')
labels = spectral.fit_predict(X)

# 클러스터 할당 결과 시각화
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Spectral Clustering')
plt.show()
