# 한줄 코딩 입력
string = input()

# 에러가 있으면 1, 없으면 0
flag = 0 
# 스택 자료구조 사용
stack = []
# one(n) 함수인지 two(n,n) 함수인지 확인용 스택
fun_stack = []

for i in range(len(string)):
    # one(n) 함수인지 two(n,n) 함수인지 확인
    if string[i:i+3] == "one":
        i += 2
        fun_stack.append("o")
    elif string[i:i+3] == "two":
        i += 2
        fun_stack.append("t")
        
    # 에러 체크
    # 여는 괄호 일때 스택 쌓기
    if string[i] == "(":
        stack.append(string[i])
    # 닫는 괄호 일때
    elif string[i] == ")":
        # one(n) 함수일 때
        if fun_stack[-1] == "o":
            # 인자 개수가 한 개인 경우
            if stack[-1] == "(":
                stack.pop() # "(" pop
                fun_stack.pop()
            # 인자 개수가 한 개가 아니면 에러
            else:
                flag = 1
                break
                
        # two(n,n) 함수일 때
        else:
            # 인자 개수가 두 개인 경우
            if stack[-1] == ",":
                stack.pop() # "," pop
                stack.pop() # "(" pop
                fun_stack.pop()
            # 인자 개수가 두 개가 아니면 에러
            else:
                flag = 1
                break
            
    # Comma stack에 넣기
    if string[i] == ",":
        stack.append(string[i])
        
# string 모두 확인 후 stack이 empty가 아니면 에러        
if len(stack) != 0:
    flag = 1

print("No Error" if flag == 0 else "Syntax Error")

