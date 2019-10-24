import numpy as np

# C 입력 받기
C = int(input())
# C개의 줄에서 받은 정수를 리스트로 받아 numpy array로 저장
lst = [list(map(int, input().split())) for _ in range(C)]
lst = np.array(lst)

# 각 작물의 구역 수 딕셔너리
cnt = {-1:0, 0:0, 1:0}

def fun(lst):
    # 리스트의 길이 계산
    n = len(lst)
    
    # 빈 리스트에 구역 내 작물 종류를 넣기
    data = []
    for i in range(n):
        data.extend(lst[i])
        
    # 구역 내에 같은 작물만 심어져 있거나 구역을 다 나누었을 때
    if len(set(data)) == 1 or n == 1:
        # 작물 종류에 해당하는 구역 개수 + 1
        cnt[list(set(data))[0]] += 1
    
    # 구역 내에 다른 작물이 존재할 때 9개 구역으로 나누기
    else:
        for i in range(3):
            for j in range(3):
                fun(lst[i*int(n/3):(i+1)*int(n/3), j*int(n/3):(j+1)*int(n/3)])
        
    return cnt

cnt = fun(lst)
print(cnt[-1])
print(cnt[0])
print(cnt[1])