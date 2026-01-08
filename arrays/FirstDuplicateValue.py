'''
    First Duplicate Value:
    Given an array, return the instance of the first duplicate value.
    If there are no duplicate values, return -1

    Time: O(N), where N is the number of elements in the array
    Space: O(N), Additional space to store numbers in set

    Last Practice: 2026-01-08 11:29:35
'''
def firstDuplicate(array):
    seen = set()
    for num in array:
        if num in seen:
            return num
        else:
            seen.add(num)
    return -1
print(firstDuplicate([1, 3, 1, 4, 3, 6]))
