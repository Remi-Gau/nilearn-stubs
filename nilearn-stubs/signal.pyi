from typing import Any

from numpy import float64, memmap, ndarray

__all__ = [
    "butterworth",
    "clean",
    "high_variance_confounds",
]

def butterworth(
    signals: ndarray,
    sampling_rate: float | float64 | int,
    low_pass: float | float64 | int | None = ...,
    high_pass: float | float64 | int | None = ...,
    order: int = ...,
    padtype: str | None = ...,
    padlen: int | None = ...,
    copy: bool = ...,
) -> ndarray: ...
def clean(
    signals: memmap | list[list[float]] | ndarray,
    runs: ndarray | None = ...,
    detrend: bool | None = ...,
    standardize: bool | str = ...,
    sample_mask: str | list[ndarray] | ndarray | None = ...,
    confounds: Any | None = ...,
    standardize_confounds: bool = ...,
    filter: bool | str = ...,
    low_pass: float | bool | float64 | None = ...,
    high_pass: float64 | float | int | bool | None = ...,
    t_r: float | float64 | int | None = ...,
    ensure_finite: bool | None = ...,
    extrapolate: bool = ...,
    **kwargs,
) -> memmap | ndarray: ...
def high_variance_confounds(
    series: ndarray,
    n_confounds: int = ...,
    percentile: float = ...,
    detrend: bool = ...,
) -> ndarray: ...
