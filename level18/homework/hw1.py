def my_min(lst):
    smallest = lst[0]
    for x in lst:
        if x < smallest:
            smallest = x
    return smallest

def my_max(lst):
    biggest = lst[0]
    for x in lst:
        if x > biggest:
            biggest = x
    return biggest
