m = int(input())
n = int(input())

def fun(m, n):
    guest = [] # m층의 1호 ~ n호의 투숙객 수
    for j in range(n+1):
        guest.append(j+1)

    for i in range(m): # 계차수열의 diff값이 아래 층의 1 ~ n호 투숙객
        result = 1
        for j in range(n):
            guest[j] = result
            diff = guest[j+1]
            result += diff
            
    return guest[j]

print(fun(m, n))