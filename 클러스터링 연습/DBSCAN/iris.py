import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN

# iris 데이터셋 로드
iris = load_iris()
X = iris.data

# PCA를 사용하여 데이터 축소
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# DBSCAN 클러스터링 수행
dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X_pca)

# 클러스터 할당 결과 시각화
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('DBSCAN Clustering (Iris Dataset)')
plt.show()
