#12명의 수험생이 빅데이터 분석기사 시험에서 받은 점수이다. Shapiro-Wilk 검정을 사용하여 데이터가 정규 분포를 따르는지 검증하시오
# 귀무 가설(H0): 데이터는 정규 분포를 따른다.
# 대립 가설(H1): 데이터는 정규 분포를 따르지 않는다.
# Shapiro-Wilk 검정 통계량, p-value, 검증결과를 출력하시오

from scipy import stats

data = [75, 83, 81, 92, 68, 77, 78, 80, 85, 95, 79, 89]

print(stats.shapiro(data))

statistic, pvalue = stats.shapiro(data)

print(statistic)
print(pvalue)

if pvalue <0.05:
    print('귀무가설 기각 대립가설 채택'
          '\n따라서 해당 데이터는 정규 분포를 따르지 않는다')
else:
    print('귀무가설 채택'
          '\n따라서 해당 데이터는 정규 분포를 따른다')