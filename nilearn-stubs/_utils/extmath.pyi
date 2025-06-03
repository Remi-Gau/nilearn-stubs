from numpy import (
    bool,
    int64,
    ndarray,
)

def fast_abs_percentile(data: ndarray, percentile: int | int64 = ...) -> int64: ...
def is_spd(M: ndarray, decimal: int = ..., verbose: int = ...) -> bool | bool: ...
