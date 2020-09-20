def biggest(aDict):
    """Returns the key corresponding to the entry with the largest number of values associated with it.
    If there is more than one such entry, return any of the matching keys

    :aDict: {string: [string]}
    :returns: string

    """
    result = ('', 0)
    for (k, v) in aDict.items():
        if len(v) > result[1]:
            result = (k, len(v))
    return result[0]
