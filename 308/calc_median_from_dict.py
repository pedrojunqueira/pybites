def calc_length_array(d: dict) -> int:
    length_array = 0
    for key in d.keys():
        length_array += d[key]
    return length_array


def calc_median_from_dict(d: dict) -> float:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """
    sorted_keys = sorted(d)
    length_array = calc_length_array(d)
    odd = length_array % 2 != 0
    if odd:
        median_index = (length_array - 1) / 2
    if not odd:
        median_index = (length_array / 2) - 1

    # find which key median for odd series
    median_value = 0.0
    if odd:
        cumm_value = 0
        for key in sorted_keys:
            cumm_value += d[key]
            if cumm_value >= (median_index + 1):
                median_value = key
                break
    # find which keys or keys median for even series
    if not odd:
        cumm_value = 0
        for i, key in enumerate(sorted_keys):
            cumm_value += d[key]
            # check if median is beyond bottom item key
            if cumm_value >= (median_index + 1) and (median_index + 2) > cumm_value:
                median_value = (sorted_keys[i] + sorted_keys[i + 1]) / 2
                break
            # both values in same key
            if cumm_value >= (median_index + 1):
                median_value = key
                break
    return median_value
