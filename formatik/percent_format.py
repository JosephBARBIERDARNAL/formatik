from typing import Union, Iterable, List
from numbers import Number

from formatik.utils import _is_iterable


def percent_format(
    x: Union[Number, Iterable[Number]], precision: int = 0
) -> Union[str, List[str]]:
    """
    Format decimal numbers as percentages.

    Parameters:
        x: Input value(s) between 0 and 1
        precision: Number of decimal places

    Returns:
        Formatted percentage string(s)

    Examples:
        >>> percent_format(0.05)
        '5%'
        >>> percent_format([0.123, 0.456], 1)
        ['12.3%', '45.6%']
    """
    if _is_iterable(x):
        return [percent_format(e, precision) for e in x]
    return f"{x:.{precision}%}"
