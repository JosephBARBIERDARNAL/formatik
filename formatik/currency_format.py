from typing import Union, Iterable, List
from numbers import Number

from formatik.utils import _is_iterable


def currency_format(
    x: Union[Number, Iterable[Number]],
    prefix: str = "$",
    suffix: str = "",
    decimal: str = ".",
    thousands: str = ",",
    accuracy: int = 2,
) -> Union[str, List[str]]:
    """
    Format numbers as currency values.

    Parameters
    ----------

    `x`: Numeric value(s) to format. Can be a number or an iterable of numbers.

    `prefix`: Currency prefix.

    `suffix`: Currency suffix.

    `decimal`: Decimal separator character.

    `thousands`: Thousands separator character.

    `accuracy`: Number of decimal places.

    Returns
    -------

    Formatted currency string(s). If `x` is an iterable, returns a list of formatted strings of the same length.

    Examples:
    ----------

    ```python
    from formatik import currency_format
    ```

    ```python
    currency_format(1234.56)
    >>> '$1,234.56'
    ```

    ```python
    currency_format(1234.56, prefix="USD ")
    >>> 'USD 1,234.56'
    ```

    ```python
    currency_format(1234.56, prefix="£", suffix="p")
    >>> '£1,234.56p'
    ```

    ```python
    currency_format([1234.56, 5678.90])
    >>> ['$1,234.56', '$5,678.90']
    ```

    ```python
    currency_format([1234.56, 5678.90], prefix="£", suffix="p")
    >>> ['£1,234.56p', '£5,678.90p']
    ```

    ```python
    currency_format(1234.56, accuracy=1)
    >>> '$1,234.6'
    ```

    ```python
    currency_format(1234.56, thousands=".")
    >>> '$1.234.56'
    ```

    ```python
    currency_format(1234.56, thousands=".", accuracy=1)
    >>> '$1.234.6'
    ```

    ```python
    currency_format(1234.56, decimal=",")
    >>> '$1,234,56'
    ```

    ```python
    currency_format(1234.56, decimal=",", accuracy=1)
    >>> '$1,234,6'
    ```
    """

    if _is_iterable(x):
        return [
            currency_format(e, prefix, suffix, decimal, thousands, accuracy) for e in x
        ]

    number_str = f"{float(x):.{accuracy}f}"

    if "." in number_str:
        int_part, dec_part = number_str.split(".")
    else:
        int_part, dec_part = number_str, ""

    result = ""
    for i, char in enumerate(reversed(int_part)):
        if i > 0 and i % 3 == 0:
            result = thousands + result
        result = char + result

    if dec_part:
        formatted_number = f"{prefix}{result}{decimal}{dec_part}{suffix}"
    else:
        formatted_number = f"{prefix}{result}{suffix}"

    return formatted_number
