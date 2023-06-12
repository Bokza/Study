import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')

# 와인 데이터셋 로드
wine = load_wine()
X = wine.data

# K-평균 클러스터링 모델 생성
k = 3
kmeans = KMeans(n_clusters=k, random_state=42)

# 모델 학습 및 클러스터 할당
kmeans.fit(X)
labels = kmeans.labels_

# 클러스터 할당 결과 시각화
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.xlabel(wine.feature_names[0])
plt.ylabel(wine.feature_names[1])
plt.title('K-means Clustering on Wine Dataset')
plt.show()
