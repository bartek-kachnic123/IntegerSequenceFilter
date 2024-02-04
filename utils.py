
def filter_list(seq):
    """
    Returns a new list of integers based on the input list, with items at positions
    which are multiples of 2 or 3 removed.
    """

    if len(seq) == 0 or len(seq) % 10 != 0:
        raise ValueError("Input list length is not a multiple of 10")

    return [x for i, x in enumerate(seq, 1) if i % 2 != 0 and i % 3 != 0]
