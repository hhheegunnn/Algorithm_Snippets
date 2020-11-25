

def recursive_function(i):
    # 10번째 호출을 했을 때 종료되도록 종료 조건 명시
    if i == 10:
        return
    print(i, '번째 재귀함수에서 ',i+1, '번째 재귀함수를 호출')
    recursive_function(i+1)
    print(i,'번째 재귀함수를 종료')

recursive_function(1)