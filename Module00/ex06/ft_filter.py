
def ft_filter(function, list):
    """Return an iterator yielding those items of iterable \
for which function(item)
is true. If function is None, return the items that are true."""
    if function:
        return [item for item in list if function(item)]
    return [item for item in list if item]
