from typing import Union, Iterable, List
from numbers import Number

from formatik.utils import _is_iterable


def dollar_format(
    x: Union[Number, Iterable[Number]], negative_parens: bool = False
) -> Union[str, List[str]]:
    """
    Format numbers as currency values.

    Parameters:
        x: Numeric value(s) to format
        negative_parens: Format negatives with parentheses

    Returns:
        Formatted currency string(s)

    Examples:
        >>> dollar_format(1500)
        '$1,500'
        >>> dollar_format(-500, True)
        '($500)'
    """
    if _is_iterable(x):
        return [dollar_format(e, negative_parens) for e in x]
    if negative_parens and x < 0:
        return f"(${abs(x):,})"
    return f"${x:,}"
