from typing import Union, Iterable, List
from numbers import Number

from formatik.utils import _is_iterable


def scientific_format(
    x: Union[Number, Iterable[Number]], precision: int = 2
) -> Union[str, List[str]]:
    """
    Format numbers in scientific notation.

    Parameters:
        x: Numeric value(s) to format
        precision: Significant figures

    Returns:
        Formatted scientific notation string(s)

    Examples:
        >>> scientific_format(12345)
        '1.23e+04'
        >>> scientific_format(0.000123)
        '1.23e-04'
    """
    if _is_iterable(x):
        return [scientific_format(e, precision) for e in x]
    return f"{x:.{precision}e}".replace("e-0", "e-").replace("e+0", "e+")
