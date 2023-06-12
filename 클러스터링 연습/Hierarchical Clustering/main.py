import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from scipy.cluster.hierarchy import dendrogram, linkage

# 예시 데이터 생성
np.random.seed(42)
X, y = make_blobs(n_samples=50, centers=3, n_features=2, random_state=42)

# 병합 계층적 클러스터링 수행
linked = linkage(X, 'ward')

# 덴드로그램 시각화
plt.figure(figsize=(10, 6))
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample Index')
plt.ylabel('Distance')
plt.show()
