# 9명의 장군의 손바닥 길이 리스트에 입력
n = 9
lst = [int(input()) for _ in range(n)]

# 리스트 오름차순 정렬
lst.sort()
# 9명의 손바닥 길이의 합
total = sum(lst)

for i in range(n):
    for j in range(i+1, n):
        # 9명 중 2명을 제외한 길이가 100인 경우
        if (total - lst[i] - lst[j]) == 100:
            for k in range(n):
                # 2명을 제외한 손바닥 길이 출력
                if k != i and k != j:
                    print(lst[k])