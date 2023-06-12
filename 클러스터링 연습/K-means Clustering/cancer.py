import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')
# 유방암 데이터셋 로드
cancer = load_breast_cancer()
X = cancer.data

# K-평균 클러스터링 모델 생성
k = 2
kmeans = KMeans(n_clusters=k, random_state=42)

# 모델 학습 및 클러스터 할당
kmeans.fit(X)
labels = kmeans.labels_

# 클러스터 할당 결과 시각화
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.xlabel(cancer.feature_names[0])
plt.ylabel(cancer.feature_names[1])
plt.title('K-means Clustering on Breast Cancer Dataset')
plt.show()
