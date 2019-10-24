# N과 X int type으로 입력 받기
N, X = map(int, input().split())
# N개의 입력 한 줄에 받기
W = list(map(int, input().split()))

# 동적 프로그래밍
def knapsack(N, X):
    # array[i][x] = 배낭 무게 한도가 x일 때, i개의 물건을 넣었을 때의 최대 무게
    array = [[0 for _ in range(X+1)] for _ in range(N+1)]
    for i in range(1, N+1): 
        for x in range(1, X+1):
            # 짐의 무게가 x보다 크면
            if W[i-1] > x: 
                # 넣을 수 없으므로 전 단계의 최적값 그대로 가져오기
                array[i][x] = array[i-1][x] 
            # 물건의 무게가 x보다 작거나 같으면
            else:
                # 1. i번째 짐만큼의 무게를 비웠을 때의 최적값에 i번째 짐 무게를 더한 값
                # 2. i-1개의 짐들을 가지고 구한 전 단계의 최적값
                # 1과 2 중 큰 값 선택
                array[i][x] = max(W[i-1] + array[i-1][x-W[i-1]], array[i-1][x])
    return array[N][X]

print(knapsack(N, X))

