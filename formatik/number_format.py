from typing import Union, Iterable, List
from numbers import Number

from formatik.utils import _is_iterable


def number_format(x: Union[Number, Iterable[Number]]) -> Union[str, List[str]]:
    """
    Format numbers with comma as thousand separator.

    Parameters:
        x: A number or iterable of numbers

    Returns:
        Formatted string(s) with commas

    Examples:
        >>> number_format(1000)
        '1,000'
        >>> number_format([1234.5, 5678])
        ['1,234.5', '5,678']
    """
    if _is_iterable(x):
        return [number_format(e) for e in x]
    return "{:,}".format(x)
