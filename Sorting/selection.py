def selection_sort(array):

    for i in range(len(array)):
        min_index = i # 가장 작은 원소의 인덱스
        for j in range(i+1,len(array)):
            if array[min_index] > array[j]:
                min_index = j
            
        array[i], array[min_index] = array[min_index], array[i] # swap
        
        print('step',i, array)

    return array

"""
array = [9, 6, 7, 3, 5]
selection_sort(array)
"""