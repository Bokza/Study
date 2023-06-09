# iris에서 Sepal Length와 Sepal Width의 상관계수 계산하고 소수 둘째자리까지 출력하시오

import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

corr = df.corr()
result = corr.loc['sepal length (cm)', 'sepal width (cm)']
print(round(result,2))