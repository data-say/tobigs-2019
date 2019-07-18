N = int(input())
P = [0 for i in range(N)]
C = [0 for i in range(N)]
code = {}

for i in range(N):
    P[i], C[i] = input().split()
    decode = lambda x: chr(ord(x) - 1 % 26) if x != 'a' else 'z'
    P[i] = ''.join(decode(ch) for ch in P[i])
    code[C[i]] = P[i]
    
sentence = input().split()
print(' '.join(code[i] for i in sentence))