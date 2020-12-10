

####### 이진탐색 재귀 ############################################

def binary_search_iterarion(array, target, start, end):

    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary_search_iterarion(array, target, start, mid-1)

    else:
        return binary_search_iterarion(array, target, mid+1, end)

####################################################################


####### 이진탐색 반복 #################################################
def binary_search_recursive(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid


        elif array[mid] > target:
            return mid -1
        
        else:
            start = mid + 1

    return None
####################################################################


n = 8
target = 50
array = [1,7,13,29,38,42,50,63]


result_iteration = binary_search_iterarion(array, target, 0, n-1)

if result_iteration == None:
    print('원소가 존재하지 않습니다.')
else:
    print('target %d의 위치는 %d입니다.'%(target,result_iteration + 1))



result_recursive = binary_search_recursive(array, target, 0, n-1)

if result_recursive == None:
    print('원소가 존재하지 않습니다.')
else:
    print('target %d의 위치는 %d입니다.'%(target,result_recursive + 1))

