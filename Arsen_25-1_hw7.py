def binary_search(n, list1):
    global pos
    first = 0
    last = len(list1) - 1
    result_ok = False


    while first < last:
        mid = (last + first) // 2
        pos = None
        if n == lst[mid]:
            first = mid
            last = first
            result_ok = True
            pos = mid

        elif n > list1[mid]:
            first = mid + 1

        else:
            last = mid

    if result_ok is True:
        print(f'Число найдено! Индекс числа  - {pos}')


    else:
        print('Число не найдено!')

lst = [1,2,3,5,7,8,9,10,11,13,14,16,17,18,20,21,23,24,25]

# binary_search(23, lst)


def selection_sort(array, size):
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])


arr = [11, 23, 15, 2, 4, 37, -1, 21, -4]
size = len(arr)
selection_sort(arr, size)
print(arr)

