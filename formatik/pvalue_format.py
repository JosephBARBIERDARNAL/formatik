from typing import Union, Iterable, List

from formatik.utils import _is_iterable


def pvalue_format(
    x: Union[float, Iterable[float]], precision: int = 3, thresholds: List[float] = None
) -> Union[str, List[str]]:
    """
    Format p-values with scientific notation thresholds.

    Parameters:
        x: P-value(s) to format
        precision: Decimal places for display
        thresholds: Significance cutoffs

    Returns:
        Formatted p-value string(s)

    Examples:
        >>> pvalue_format(0.0001)
        '<0.001'
        >>> pvalue_format(0.005, thresholds=[0.01])
        '<0.01'
    """
    thresholds = thresholds or [0.001]
    if _is_iterable(x):
        return [pvalue_format(e, precision, thresholds) for e in x]
    for threshold in sorted(thresholds, reverse=True):
        if x < threshold:
            return f"<{threshold:.{precision}f}"
    return f"{x:.{precision}f}"
