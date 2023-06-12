import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture
import warnings
warnings.filterwarnings('ignore')

# 예시 데이터 생성
np.random.seed(42)
X, y = make_blobs(n_samples=200, centers=3, n_features=2, random_state=42)

# GMM 클러스터링 수행
gmm = GaussianMixture(n_components=3)
gmm.fit(X)

# 클러스터 할당 결과 가져오기
labels = gmm.predict(X)

# 클러스터 할당 결과 시각화
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('GMM Clustering')
plt.show()
