from typing import Union, Iterable, List
import datetime

from formatik.utils import _is_iterable


def date_format(
    x: Union[datetime.date, Iterable[datetime.date]], fmt: str = "%Y-%m-%d"
) -> Union[str, List[str]]:
    """
    Format dates using strftime specifiers.

    Parameters:
        x: Date object(s) to format
        fmt: Format string

    Returns:
        Formatted date string(s)

    Examples:
        >>> date_format(datetime.date(2023, 12, 31))
        '2023-12-31'
    """
    if _is_iterable(x):
        return [date_format(e, fmt) for e in x]
    return x.strftime(fmt)
