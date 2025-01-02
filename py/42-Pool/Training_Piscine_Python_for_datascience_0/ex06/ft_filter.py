
def even(n):
    return n % 2 == 0


def ft_filter(func, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    return ([func(item) for item in iterable])



# list1 = [i for i in range(0, 11)]
# list2 = list(ft_filter(even, list1))
# print(list1)
# print(list2)

