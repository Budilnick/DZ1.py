from module_4.sortfunc import bubble_sort, insertion_sort, selection_sort


data1 = [9, 5, 4, 3, 8, 4, 1, 2]
data2 = [9, 5, 4, 3, 8, 4, 1, 2, 54, 6]
data3 = [9, 5, 4, 3, 8, 4, 1, 3, 54, 15, 2, 6]

print(insertion_sort(data1))
print(insertion_sort(data2))
print(insertion_sort(data3))

print(bubble_sort(data1))
print(bubble_sort(data2))
print(bubble_sort(data3))

print(selection_sort(data1))
print(selection_sort(data2))
print(selection_sort(data3))
