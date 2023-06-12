import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

# 데이터
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

# 그래프 그리기
plt.plot(x, y)

# 그래프 타이틀
plt.title('Example Graph')

# 축 레이블
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# 그래프 표시
plt.show()
