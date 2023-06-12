import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# iris 데이터셋 로드
iris = load_iris()
X = iris.data
# K-평균 클러스터링 모델 생성
k = 3
kmeans = KMeans(n_clusters=k, random_state=42)

# 모델 학습 및 클러스터 할당
kmeans.fit(X)
labels = kmeans.labels_

# 클러스터 중심 좌표
centroids = kmeans.cluster_centers_

# 클러스터 할당 결과 시각화
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='r')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title('K-means Clustering on Iris Dataset')
plt.show()
