from math import floor

def linear_search(values, target):
    n = len(values)
    
    for i in range(n):
        if values[i] == target:
            return i
        
    return -1

def binary_search(values, target, start, end):
    mid = int(floor((start + end) / 2))
    
    if target == values[end]:
        return end

    if target == values[mid]:
        return mid
    elif target < values[mid]:
        return binary_search(values, target, start, mid)
    else:
        return binary_search(values, target, mid, end)