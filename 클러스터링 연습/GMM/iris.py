import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.mixture import GaussianMixture

# iris 데이터셋 로드
iris = load_iris()
X = iris.data

# GMM 클러스터링 수행
gmm = GaussianMixture(n_components=3)
gmm.fit(X)

# 클러스터 할당 결과 가져오기
labels = gmm.predict(X)

# 클러스터 할당 결과 시각화
plt.scatter(X[:, 2], X[:, 3], c=labels)
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('GMM Clustering (Iris Dataset)')
plt.show()
