def bubble_sort(item):
    n = len(item)
    for i in range(n - 1):
        for l in range(0, n - i - 1):
            if item[l] > item[l + 1]:
                item[l], item[l + 1] = item[l + 1], item[l]
    return item


unsorted_list = [15, 20, 5, 3, 51]
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)
