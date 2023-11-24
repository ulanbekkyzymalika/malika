def binary_search(A, Val):
    global middle
    first = 0
    last = len(Val) - 1
    resultok = False
    while first <= last:
        middle = (first + last) // 2
        if Val[middle] == A:
            resultok = True
            break
        elif Val[middle] < A:
            first = middle + 1
        else:
            last = middle - 1
    if resultok:
        return middle
    else:
        return - 1


n = list(range(1, 5001))
search = binary_search(5002, n)
if search != -1:
    print(f'Индекс элемента найден: {search}')
else:
    print('Такого элемента нет!')
