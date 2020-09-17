
def selection_sort(list_a):
    indexing_length = range(0, len(list_a)-1)

    for i in indexing_length:
        min_value = i

        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j

            if min_value != i:
                list_a[min_value], list_a[i] = list_a[i], list_a[min_value]

    return list_a

print(selection_sort([6,7,8,7,6,5,4,5,6,7,6,7,8,9,7,9,0]))
