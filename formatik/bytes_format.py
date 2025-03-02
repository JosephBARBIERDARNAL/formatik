from typing import Union, Iterable, List

from formatik.utils import _is_iterable


def bytes_format(
    x: Union[int, Iterable[int]], precision: int = 1
) -> Union[str, List[str]]:
    """
    Format bytes into human-readable units (kB, MB, GB, etc.).

    Parameters
    ----------

    `x`: Number of bytes or an iterable of byte counts.

    `precision`: Number of decimal places to round to.

    Returns
    -------

    Formatted string(s) with the appropriate unit. If `x` is an iterable, returns a list of formatted strings of the same length.

    Examples:
    ----------

    ```python
    from formatik import bytes_format
    ```

    ```python
    bytes_format(1024)
    >>> '1.0 kB'
    ```

    ```python
    bytes_format(1500000)
    >>> '1.4 MB'
    ```

    ```python
    bytes_format([1024, 1500000])
    >>> ['1.0 kB', '1.4 MB']
    ```
    """

    units = ["B", "kB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]

    def _format_single(value: int) -> str:
        if value == 0:
            return f"0 {units[0]}"
        for unit in units:
            if abs(value) < 1024.0:
                return f"{value:.{precision}f} {unit}"
            value /= 1024.0
        return f"{value:.{precision}f} {units[-1]}"

    if _is_iterable(x):
        return [_format_single(e) for e in x]
    return _format_single(x)
