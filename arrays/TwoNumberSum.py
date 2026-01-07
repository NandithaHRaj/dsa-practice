'''
    Two-Number Sum:
    Given an unsorted array as input and a target integer,
    locate two elements in the array that sum up to the target integer.
    If there are no two such numbers, return an empty array

    Time: O(NlogN), where N is the number of elements in the array
    Space: O(1)

    O(N)/O(N) Time/Space is possible if using a dictionary 

    Last Practiced: 2026-01-08 13:40:12
'''
def twoNumberSum(array, targetSum):
    left =  0
    right = len(array) - 1
    array.sort()
    while left < right:
        if array[left] + array[right] > targetSum:
            left += 1
        elif array[left] + array[right] < targetSum:
            right -= 1
        else:
            return [array[left],array[right]]
    return []
print(twoNumberSum([4, 1, 2, 3, 5], 6))
print(twoNumberSum([4, 1, 2, 3, 5], 10))



