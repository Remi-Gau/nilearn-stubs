from pathlib import Path, PosixPath
from typing import Any

from joblib.memory import MemorizedResult, Memory
from nibabel.nifti1 import Nifti1Image
from numpy import memmap, ndarray
from pandas.core.frame import DataFrame
from sklearn.utils.estimator_checks import _NotAnArray

class NiftiMasker:
    def __init__(
        self,
        mask_img: str | int | PosixPath | Nifti1Image | None = ...,
        runs: int | ndarray | None = ...,
        smoothing_fwhm: float | None = ...,
        standardize: int | str | bool = ...,
        standardize_confounds: int | bool = ...,
        detrend: int | bool = ...,
        high_variance_confounds: int | bool = ...,
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: float | None = ...,
        target_affine: ndarray | None = ...,
        target_shape: tuple[int, int, int] | list[int] | None = ...,
        mask_strategy: int | str = ...,
        mask_args: (
            dict[str, float] | dict[str, int] | int | dict[str, bool] | None
        ) = ...,
        dtype: int | str | None = ...,
        memory_level: int = ...,
        memory: Memory | str | Path | None = ...,
        verbose: int = ...,
        reports: int | bool = ...,
        cmap: int | str = ...,
        **kwargs,
    ): ...
    def fit(
        self,
        imgs: Any | None = ...,
        y: _NotAnArray | ndarray | memmap | None = ...,
    ) -> NiftiMasker: ...
    def transform_single_imgs(
        self,
        imgs: Any,
        confounds: list[DataFrame] | list[ndarray] | None = ...,
        sample_mask: ndarray | None = ...,
        copy: bool = ...,
    ) -> memmap | ndarray | MemorizedResult: ...
