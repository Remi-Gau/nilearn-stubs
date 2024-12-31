from numpy import (
    float64,
    memmap,
    ndarray,
)
from pandas.core.frame import DataFrame
from pathlib import PosixPath
from typing import (
    Any,
    List,
    Optional,
    Tuple,
    Union,
)

__all__ = [
    "butterworth",
    "clean",
    "high_variance_confounds",
]

def butterworth(
    signals: ndarray,
    sampling_rate: Union[float, float64, int],
    low_pass: Optional[Union[float, float64, int]] = ...,
    high_pass: Optional[Union[float, float64, int]] = ...,
    order: int = ...,
    padtype: Optional[str] = ...,
    padlen: Optional[int] = ...,
    copy: bool = ...
) -> ndarray: ...


def clean(
    signals: Union[memmap, List[List[float]], ndarray],
    runs: Optional[ndarray] = ...,
    detrend: Optional[bool] = ...,
    standardize: Union[bool, str] = ...,
    sample_mask: Optional[Union[str, List[ndarray], ndarray]] = ...,
    confounds: Optional[Any] = ...,
    standardize_confounds: bool = ...,
    filter: Union[bool, str] = ...,
    low_pass: Optional[Union[float, bool, float64]] = ...,
    high_pass: Optional[Union[float64, float, int, bool]] = ...,
    t_r: Optional[Union[float, float64, int]] = ...,
    ensure_finite: Optional[bool] = ...,
    extrapolate: bool = ...,
    **kwargs
) -> Union[memmap, ndarray]: ...


def high_variance_confounds(
    series: ndarray,
    n_confounds: int = ...,
    percentile: float = ...,
    detrend: bool = ...
) -> ndarray: ...
