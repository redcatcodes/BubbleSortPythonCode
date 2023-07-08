def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


array = [10, 5, 2, 3, 1, 8, 9, 7, 6]

sorted_array = bubble_sort(array)
print(sorted_array)









# for element in range(9):
#     print(element)

# def bubble_sort(array):
#     for i in range(len(array) - 1):
        
#         for j in range(len(array) - i - 1):
            
#             if array[j] > array[j + 1]:
#                 print(str(array) + " i = "+ str(i) + ", j = ", j)
#                 array[j], array[j + 1] = array[j + 1], array[j]
#             else:
#                 print(str(array) + " i = "+ str(i) + ", j = ", j, "NO SWAP")
            
           

#     return None

# array = [10, 5, 2, 3, 1, 8, 9, 7, 6]

# sorted_array = bubble_sort(array)

# print(sorted_array)
# for element in range(9):
#     print(element)