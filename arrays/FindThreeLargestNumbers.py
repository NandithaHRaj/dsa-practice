'''
	Find Three Largest Numbers:
	Given an input array, find the three largest numbers
    in the array and return them in an array of their own,
    in sorted order. Example:

    Input:  [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    Output: [18, 141, 541]

    Time:  O(N) - N is number of elements in the array.Iterates the array once.
    Space: O(1) - Uses only 3 varaiables (constant space).

    Last Practiced: 2026-01-08 11:32:50
'''
def findThreeLargestNumbers(array):
    three_largest = [float('-inf'), float('-inf'), float('-inf')]
    for num in array:
        if num > three_largest[2]:
            three_largest[0] = three_largest[1]
            three_largest[1] = three_largest[2]
            three_largest[2] = num
        elif num > three_largest[1]:
            three_largest[0] = three_largest[1]
            three_largest[1] = num
        elif num > three_largest[0]:
            three_largest[0] = num
    return three_largest
print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))
