from typing import Union, Iterable, List

from formatik.utils import _is_iterable


def ordinal_format(x: Union[int, Iterable[int]]) -> Union[str, List[str]]:
    """
    Convert integers to ordinal numbers.

    Parameters:
        x: Integer value(s) to format

    Returns:
        Ordinal string(s)

    Examples:
        >>> ordinal_format(2)
        '2nd'
        >>> ordinal_format([21, 22, 23])
        ['21st', '22nd', '23rd']
    """
    if _is_iterable(x):
        return [ordinal_format(e) for e in x]
    n = abs(x)
    suffix = (
        "th" if 11 <= n % 100 <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    )
    return f"{x}{suffix}"
