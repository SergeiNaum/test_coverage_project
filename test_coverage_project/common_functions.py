def right_get(coll: list, index: int, default=None):
    """Correct Function Implementation"""
    if (index >= len(coll) or index < 0):
        if default is not None:
            return default
        return None

    return coll[index]


def get_w1(coll: list, index: int, default=None):
    """Incorrect Function Implementation"""
    if (index >= len(coll) or index < 0):
        if default is not None:
            return False
        return None

    return coll[index]


def get_w2(coll: list, index: int, default=None):
    """Incorrect Function Implementation"""
    if (index >= len(coll) or index < 0):
        if default is not None:
            return default
        return False

    return coll[index]


def get_w3(coll: list, index: int, default=None):
    """Incorrect Function Implementation"""
    if default is not None:
        return default

    if (index >= len(coll) or index < 0):
        return default

    return coll[index]


def index_of_right(coll: list, value: int, from_index=0) -> int:
    """Correct Function Implementation"""
    length = len(coll)

    if length == 0:
        return -1

    index = from_index

    if index < 0:
        if index < -length:
            index = 0
        else:
            index += length

    try:
        return coll.index(value, index)
    except ValueError:
        return -1


def index_of_w1(coll: list, value: int, from_index=0) -> int or None:
    """Incorrect Function Implementation"""
    length = len(coll)

    if length == 0:
        return None

    try:
        return coll.index(value, from_index)
    except ValueError:
        return -1


def index_of_w2(coll, value, from_index=0):
    """Incorrect Function Implementation"""
    if from_index < 0:
        if from_index < -len(coll):
            return []

    try:
        return coll.index(value, from_index)
    except ValueError:
        return -1


def index_of_w3(coll: list, value: int, from_index=0) -> int:
    """Incorrect Function Implementation"""
    if from_index < 0:
        if from_index >= -len(coll):
            return coll.index(value)

    try:
        return coll.index(value, from_index)
    except ValueError:
        return -1


def my_slice_right(coll: list, start=0, end=None) -> list:
    """Correct Function Implementation"""
    length = len(coll)

    normalized_end = length if end is None else end

    if length == 0:
        return []

    normalized_start = start

    if normalized_start < 0:
        if normalized_start < -length:
            normalized_start = 0
        else:
            normalized_start += length

    return coll[normalized_start:normalized_end]


def my_slice_w1(coll: list, start=0, end=None) -> list or None:
    """Incorrect Function Implementation"""
    length = len(coll)

    normalized_end = length if end is None else end

    if length == 0:
        return None

    return coll[start:normalized_end]


def my_slice_w2(coll, start=0, end=None):
    """Incorrect Function Implementation"""
    length = len(coll)

    normalized_end = length if end is None else end

    if start < 0:
        if start < -length:
            return []

    return coll[start:normalized_end]


def my_slice_w3(coll: list, start=0, end=None) -> list:
    """Incorrect Function Implementation"""
    length = len(coll)

    normalized_end = length if end is None else end

    if start < 0:
        if start >= -length:
            return coll[1:]

    return coll[start:normalized_end]
