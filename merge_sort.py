def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr
    else:
        # splitting list into two arrays
        midpoint = len(arr) // 2
        l_list = arr[:midpoint]
        r_list = arr[midpoint:]

    # recursive call for each list
    merge_sort(l_list)
    merge_sort(r_list)

    left_index = 0      # interator left side
    right_index = 0     # iterator right side
    sorted_index = 0    # itereator for sorted_list
    sorted_list = []    # list populates going thru while loops

    while left_index < len(l_list) and right_index < len(r_list):
        if l_list[left_index] <= r_list[right_index]:
            arr[sorted_index] = l_list[left_index]
            left_index += 1
        else:
            arr[sorted_index] = r_list[right_index]
            right_index += 1
        sorted_index += 1

    while left_index < len(l_list):
        arr[sorted_index] = l_list[left_index]
        left_index += 1
        sorted_index +=1

    while right_index < len(r_list):
        arr[sorted_index] = r_list[right_index]
        right_index += 1
        sorted_index +=1

    return sorted_list

my_list = [6, 2, 3, 4, 2, 6]
merge_sort(my_list)
print(my_list)
