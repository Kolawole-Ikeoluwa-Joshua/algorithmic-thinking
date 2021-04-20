def binary_search(list, target):

   
    """
    Lines (13 - 14 , 17 - 26): run in constant runtimes
    """

    """
    Line (16): run in logarithmic runtimes, because each time the while loop iterates it divides the list by a certain factor
    """


    first = 0
    last = len(list) - 1 

    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint

        elif list[midpoint] < target:
            first = midpoint + 1

        else:
            last = midpoint - 1

    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")



"""
1. Binary search has a prerequsite that the list to search 
has to be sorted
"""
numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 6)
verify(result)