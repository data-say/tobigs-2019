M, N = input().split()
A = [input() for i in range(int(M))]
B = [input() for i in range(int(N))]
result = list(set(A) & set(B))
print(len(result))
for i in sorted(result):
    print(i.capitalize())