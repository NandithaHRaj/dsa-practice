'''
    BubbleSort:
    Given an unsorted array as input, perform a BubbleSort and
    return the sorted array

    Average Time: O(N^2), where N = number of elements in array
    Best Time: O(N), when the array is already sorted
    Space: O(1) , No additional Space used

    NOTE : Not used in real world, because of poor performance O(N^2), 
    extremely slow for large data set!


    Last Practiced: 2026-01-05 06:05:36
'''
def bubbleSort(array):
    n = len(array)
    for i in range(n - 1):
        swapped = False
        #After each i - outer loop, the largest element bubbles to the end!
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
    return array

print(bubbleSort([4, 3, 2, 1]))
print(bubbleSort([5, 1, 4, 2, 8]))


