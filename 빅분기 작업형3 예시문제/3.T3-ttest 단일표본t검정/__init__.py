# 문제: 다음은 22명의 학생들이 국어시험에서 받은 점수이다. 학생들의 평균이 75보다 크다고 할 수 있는가?
# 귀무가설(H0): 모평균은 mu와 같다. (μ = mu), 학생들의 평균은 75이다
# 대립가설(H1): 모평균은 mu보다 크다. (μ > mu), 학생들의 평균은 75보다 크다
# 가정:
# 모집단은 정규분포를 따른다.
# 표본의 크기가 충분히 크다.
# 검정통계량, p-value, 검정결과를 출력하시오

import pandas as pd
from scipy import stats

scores = [75, 80, 68, 72, 77, 82, 81, 79, 70, 74, 76, 78, 81, 73, 81, 78, 75, 72, 74, 79, 78, 79]
mu = 75
print(stats.ttest_1samp(scores, mu, alternative='greater'))
ts, pv = stats.ttest_1samp(scores, mu, alternative='greater')
print(ts)
print(pv)

if pv < 0.05:
    print('귀무가설 기각 대립가설 채택'
          '\n평균이 75보다 크다고 할 수 있다.')
else:
    print('귀무가설 채택'
          '\n평균이 75보다 크다고 할 수 없다.')