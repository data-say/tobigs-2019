# 퀴즈 결과 한 줄로 입력받기
score = input()

choco = 0
j = 0
# 문제 개수에 대해서
for i in range(len(score)):
    # 문제를 맞췄을 때
    if score[i] == 'O':
        # 초콜릿이 전에 맞춘 개수보다 하나 더 많이 받는다.
        j += 1
        choco += j
    # 틀렸으면 다시 한 문제에 대해 받을 수 있는 초콜릿 수 초기화
    else:
        j = 0
        
print(choco)