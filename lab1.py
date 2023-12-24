def max_list_iter(int_list):  # must use iteration not recursion
    '''Finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError'''

    if int_list is None:
        raise ValueError
    elif len(int_list) == 0:
        return None
    else:
        max_val = int_list[0]
        for i in range(len(int_list)):
            if int_list[i] >= max_val:
                max_val = int_list[i]
        return max_val


def reverse_rec(int_list):  # must use recursion
    '''Recursively reverses a list of numbers and returns the reversed list
   Should not mutate the input list
   If list is None, raises ValueError'''
    if int_list is None:
        raise ValueError
    elif len(int_list) == 0:
        return []
    elif len(int_list) == 1:
        return int_list
    else:
        first = int_list[0:1]
        shortened_list = int_list[1:len(int_list)]
        return reverse_rec(shortened_list) + first


def bin_search(target, low, high, int_list):  # must use recursion
    '''Searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError 
   Assume that int_list is sorted and contains no duplicates'''
    midpoint = (low + high) // 2
    if int_list is None:
        raise ValueError
    elif target not in int_list:
        return None
    elif target == int_list[midpoint]:
        return midpoint
    elif target < int_list[midpoint]:
        return bin_search(target, low, midpoint - 1, int_list)
    elif target > int_list[midpoint]:
        return bin_search(target, midpoint + 1, high, int_list)


# Signature: Maybe_List -> None
# Purpose: Reverse the original input list 
def reverse_list_mutate(int_list):
    '''Reverses a list, modifies the input list, returns None
   If list is None, raises ValueError'''
    if int_list is None:
        raise ValueError
    else:
        first = 0
        last = -1
        for i in range(len(int_list) // 2):
            int_list[first], int_list[last] = int_list[last], int_list[first]
            first += 1
            last -= 1
    return None
