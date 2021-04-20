"""
a recursive function is one that calls itself

this is a recursive binary search function

it also has a logarithmic runtime since it divides the initial list into sublists


"""


def recursive_binary_search(list, target):
    if len(list) == 0:    # First base case (stopping condition for the algorithm)
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:   # Second base case (stopping condition)
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)

def verify (result):
    print('Target found: ', result)
numbers = [1,2,3,4,5,6,7,8]
result = recursive_binary_search(numbers, 12)
verify(result)

result = result = recursive_binary_search(numbers, 6)
verify(result)