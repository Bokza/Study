import requests
import psycopg2
import os
import sys
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout


def putDataFrame(url, df, list, seq):
    try:
        for i in range(seq):
            urls = url + f'{i + 1}'
            response = requests.get(urls)

            print(response.text)
            text = response.json()
            l_list = []
            for j in range(len(list)):
                l_list.append(text.get(list[j]))
            df.append(l_list)

    except Exception as err:
        print(str(err))

    return df


def executeToDataFrame(df, colname, csvname):
    try:
        df = pd.DataFrame(df, columns=colname)
        df.to_csv(f'{csvname}.csv', index=False, encoding='euc-kr')

    except Exception as err:
        print(str(err))


def callData():
    try:
        # 데이터 불러오기
        df = pd.read_csv('lto.csv', encoding='euc-kr')
        data = df.values.tolist()

        # 입력 데이터 정규화
        data = np.array(data)
        max_number = 45
        data = data / max_number

    except Exception as err:
        print(str(err))

    return data, max_number


def executeModel(seq):
    try:
        # 5개의 모델 생성
        models = []
        seq = seq - 1
        for i in range(5):
            model = Sequential()
            model.add(LSTM(units=50, return_sequences=True, input_shape=(seq, 6)))
            model.add(Dropout(0.2))
            model.add(LSTM(units=50, return_sequences=True))
            model.add(Dropout(0.2))
            model.add(LSTM(units=50))
            model.add(Dropout(0.2))
            model.add(Dense(units=6, activation='sigmoid'))
            model.compile(optimizer='adam', loss='binary_crossentropy')
            models.append(model)

    except Exception as err:
        print(str(err))
    return models


def excuteLSTM(data, models, max_number, seq):
    try:
        seq = seq - 1
        # 각 모델을 독립적으로 훈련
        for i in range(5):
            np.random.shuffle(data)
            models[i].fit(data[:-1].reshape(1, seq, 6), data[-1].reshape(1, 6), epochs=100)

        # 번호 예측
        next_weeks = []
        for i in range(5):
            next_week = models[i].predict(data[-seq:].reshape(1, seq, 6))
            next_week = np.round(next_week * max_number)
            if len(next_week[0]) != len(set(next_week[0])):
                np.random.shuffle(data)
                models[i].fit(data[:-1].reshape(1, seq, 6), data[-1].reshape(1, 6), epochs=100)
                next_week = models[i].predict(data[-seq:].reshape(1, seq, 6))
                next_week = np.round(next_week * max_number)
            next_weeks.append(next_week)

        # 5개의 다른 조합 출력
        for i in range(5):
            print(f'이번주 추천 번호를 알려드리겠습니다. {i + 1}번째 조합은', next_weeks[i], '입니다.')

    except Exception as err:
        print(str(err))


def main():
    try:
        df = []
        url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=+'
        list = ['drwtNo1', 'drwtNo2', 'drwtNo3', 'drwtNo4', 'drwtNo5', 'drwtNo6']
        colname = ['당첨번호1', '당첨번호2', '당첨번호3', '당첨번호4', '당첨번호5', '당첨번호6']
        csvname = 'lto'
        seq = 1071  # 회차

        df = putDataFrame(url, df, list, seq)
        executeToDataFrame(df, colname, csvname)
        data, max_number = callData()
        models = executeModel(seq)
        excuteLSTM(data, models, max_number, seq)

    except Exception as err:
        print(str(err))


if __name__ == '__main__':
    main()