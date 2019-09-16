import sys
import numpy as np

f = open("Apartment.txt", 'r')
N=int(f.readline())

dong_ho=[]
size=[]
rooms=[]
for i in range(N):
    lists=f.readline().split(' ')
    dong_ho.append(lists[0])
    size.append(int(lists[1]))
    rooms.append(int(lists[2].strip()))

f.close()

# 총 n개의 아파트 정보가 들어가있음
# Q 가장 평수가 큰 집을 찾아 "xxx동 xxxx호의 x개의 방이 있는 xx평의 집입니다" 라고 출력


def print_pretty(address,rooms,size):
    print('%s동 %s호의 %d개의 방이 있는 %d평의 아파트입니다.' %(address.split('-')[0],address.split('-')[1],rooms,size))

# 가장 큰 size를 가진 집의 index
max_size=np.argmax(size)
print('가장 큰 평수 아파트의 정보를 출력하세요.')
print_pretty(dong_ho[max_size],rooms[max_size],size[max_size])


f = open("Vile.txt", 'r')
N=int(f.readline())

address=[]
size_vile=[]
rooms_vile=[]
yard=[]
for i in range(N):
    lists=f.readline().split(' ')
    address.append(lists[0])
    size_vile.append(int(lists[1]))
    rooms_vile.append(int(lists[2].strip()))
    yard.append(lists[3])

f.close()

print()
def print_pretty_vile(address,rooms,size,yard):
    if(yard=='T'):
        print('%s에 위치해 있는 %d개의 방이 있고 마당이 있는 %d평의 주택입니다.' % (address, rooms, size))

    else:
        print('%s에 위치해 있는 %d개의 방이 있고 마당은 없는 %d평의 주택입니다.' % (address, rooms, size))


# 가장 큰 size를 가진 집의 index
max_size1=np.argmax(size_vile)
print('가장 큰 평수 주택의 정보를 출력하세요.')
print_pretty_vile(address[max_size1],size_vile[max_size1],rooms_vile[max_size1],yard[max_size])
