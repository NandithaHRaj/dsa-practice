'''
    Three Number Sum:
    Take in an array and a target value. return all the sets of
    three numbers from within the array that sum up to the target value

    Time:  O(N^2) - Exponential
    Space: O(N)   - Linear

    Last Practiced: 2026-01-07 13:52:50
'''
def threeNumberSum(array, targetSum):
    array.sort()
    for i in range(len(array)):
        left = i + 1
        right = len(array) - 1
        while left < right:
            if array[i] + array[left] + array[right] == targetSum:
                return [array[i] , array[left], array[right]]
            elif array[i] + array[left] + array[right] < targetSum:
                left += 1
            elif array[i] + array[left] + array[right] > targetSum:
                right -= 1
    return []
print(threeNumberSum([9, 1, 2, 5, 3], 10))
print(threeNumberSum([9, 1, 2, 5, 3], 11))

    



