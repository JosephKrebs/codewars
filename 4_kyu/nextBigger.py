def next_bigger(num):
    num_str = str(num)
    n = len(num_str)
    
    # find the pivot point where the rightmost digit is smaller than the digit to its left
    pivot = n - 2
    while pivot >= 0 and num_str[pivot] >= num_str[pivot+1]:
        pivot -= 1
    
    if pivot == -1:
        return -1 # digits can't be rearranged to form a bigger number
    
    # find the rightmost digit that is greater than the pivot
    successor = n - 1
    while successor > pivot and num_str[successor] <= num_str[pivot]:
        successor -= 1
    
    # swap the pivot and the successor
    num_list = list(num_str)
    num_list[pivot], num_list[successor] = num_list[successor], num_list[pivot]
    
    # reverse the digits to the right of the pivot
    num_list[pivot+1:] = reversed(num_list[pivot+1:])
    
    # convert the list back to a number
    next_num = int("".join(num_list))
    
    return next_num
