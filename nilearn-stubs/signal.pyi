from typing import Any, Literal

from numpy import memmap, ndarray

__all__ = [
    "butterworth",
    "clean",
    "high_variance_confounds",
]

def butterworth(
    signals: ndarray,
    sampling_rate: float | int,
    low_pass: float | None = ...,
    high_pass: float | None = ...,
    order: int = ...,
    padtype: Literal["odd", "even", "constant", None] = ...,
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
    low_pass: float | None = ...,
    high_pass: float | None = ...,
    t_r: float | int | None = ...,
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
