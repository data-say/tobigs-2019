N = int(input())
numList = list(map(int, input().split()))

def notNine(x):
    for i in str(x):
        if i == "9":
            return False
    return x
            
newList = list(filter(notNine, numList))
try:
    print(newList[N-1] ** 2)
except IndexError:
    print(999999999)