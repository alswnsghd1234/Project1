# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random
import time

words = []  # 영어 단어 리스트

n = 1  # 게임 시도 횟수
cor_cnt = 0  # 정답 개수

with open('C:/Users/min/OneDrive/바탕 화면/My_developed/Project_BE/Project_Test_Folder/resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())
print(words)
