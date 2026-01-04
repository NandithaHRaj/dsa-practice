'''
    Binary Search:
    Given a sorted array and target value as input, perform a binary
    search to find the index of the target value. Return the index.
    
    Iterative
    Time:  O(log(N)) - N is the number of elemnts in the array.
    Space: O(1) - No additional space

    Recursive
    Time:  O(log(N)) - N is the number of elemnts in the array.
    Space: O(log(N)) - Recursive call uses stack space 
    
    Last Practice: 2026-01-04 13:41:27
'''
def binarySearch_recursive(sortedArr, target, left=None, right=None):
    if left is None:
        left = 0
        right = len(sortedArr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if target < sortedArr[mid]:
        return binarySearch_recursive(sortedArr, target, left, mid - 1)
    elif target > sortedArr[mid]:
        return binarySearch_recursive(sortedArr, target, mid + 1, right)
    elif target == sortedArr[mid]:
        return mid
    
def binarySearch_iterative(sortedArr, target):
    left = 0
    right = len(sortedArr) - 1
    while (left <= right):
        mid = (left + right) // 2
        if sortedArr[mid] == target:
            return mid
        elif target < sortedArr[mid]:
            right = mid - 1
        else :
            left = mid + 1
    return -1

rec_index = binarySearch_recursive([1, 2, 3, 4, 5],3,None,None)
print("Recursive Search:",rec_index)
itr_index = binarySearch_recursive([1, 2, 3, 4, 5],3)
print("Iterative Search", itr_index)
