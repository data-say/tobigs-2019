from Apartment import Apartment
from Vile import Vile

f = open("Apartment.txt", 'r')
N = int(f.readline())

apartments=[]
for i in range(N):
    lst = f.readline().split(' ')
    a = Apartment(lst[0], lst[1], lst[2].strip())
    apartments.append(a)
    
f.close()

# 클래스 리스트 정렬
max_index=0
# magic method가 작동하는 것을 직관적으로 파악해보기 위해 for문을 이용하여 최댓값을 찾아보세요!
for j in range(N):
    if apartments[max_index] < apartments[j]:
        max_index = j

# 혹시 같은 인덱스가 있으면 같이 출력한다.
print(apartments[max_index])
for j in range(N):
    if apartments[max_index] == apartments[j] and max_index != j:
        print(apartments[j])

# Vile에 대한 최대평수 출력은 max를 활용해보세요~!
f = open("Vile.txt", 'r')
M = int(f.readline())

viles = []
for i in range(M):
    lst = f.readline().split(' ')
    v = Vile(lst[0], lst[1], lst[2], lst[3].strip())
    viles.append(v)
    
f.close()

print(max(viles))