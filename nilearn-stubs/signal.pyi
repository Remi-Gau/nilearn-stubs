from pathlib import Path
from typing import Literal

import pandas as pd
from numpy import ndarray

__all__ = [
    "butterworth",
    "clean",
    "high_variance_confounds",
]

def butterworth(
    signals: ndarray,
    sampling_rate: float,
    low_pass: float | None = ...,
    high_pass: float | None = ...,
    order: int = ...,
    padtype: Literal["odd", "even", "constant", None] = ...,
    padlen: int | None = ...,
    copy: bool = ...,
) -> ndarray: ...
def clean(
    signals: ndarray,
    runs: ndarray | None = ...,
    detrend: bool = ...,
    standardize: Literal["zscore_sample", "zscore", "psc", True, False] = ...,
    sample_mask: str | list[ndarray] | ndarray | None = ...,  # TODO
    confounds: (
        ndarray
        | str
        | Path
        | pd.DataFrame
        | list[ndarray | str | Path | pd.DataFrame]
        | tuple[ndarray | str | Path | pd.DataFrame]
        | None
    ) = ...,
    standardize_confounds: bool = ...,
    filter: Literal["butterworth", "cosine", False] = ...,
    low_pass: float | None = ...,
    high_pass: float | None = ...,
    t_r: float = ...,
    ensure_finite: bool = ...,
    extrapolate: bool = ...,
    **kwargs,
) -> ndarray: ...
def high_variance_confounds(
    series: ndarray,
    n_confounds: int = ...,
    percentile: float = ...,
    detrend: bool = ...,
) -> ndarray: ...
