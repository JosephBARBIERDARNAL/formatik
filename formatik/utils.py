from typing import Union, Iterable, List, Any


def _is_iterable(x: Any) -> bool:
    return isinstance(x, Iterable) and not isinstance(x, (str, bytes))
