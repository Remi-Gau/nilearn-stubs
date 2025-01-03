import os
from pathlib import PosixPath
from typing import Any, Literal

from joblib.memory import MemorizedResult, Memory
from nibabel.nifti1 import Nifti1Image
from numpy import memmap, ndarray
from numpy.typing import DTypeLike
from pandas.core.frame import DataFrame
from typing_extensions import TypeAlias

MemoryLike: TypeAlias = Memory | str | os.PathLike[str] | None

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
        mask_strategy: Literal[
            "background",
            "epi",
            "whole-brain-template",
            "gm-template",
            "wm-template",
        ] = ...,
        mask_args: (
            dict[str, float] | dict[str, int] | int | dict[str, bool] | None
        ) = ...,
        dtype: DTypeLike | None = ...,
        memory_level: int = ...,
        memory: MemoryLike = ...,
        verbose: int = ...,
        reports: int | bool = ...,
        cmap: int | str = ...,
        **kwargs,
    ): ...
    def fit(
        self,
        imgs: Any | None = ...,
        y: ndarray | memmap | None = ...,
    ) -> NiftiMasker: ...
    def transform_single_imgs(
        self,
        imgs: Any,
        confounds: list[DataFrame] | list[ndarray] | None = ...,
        sample_mask: ndarray | None = ...,
        copy: bool = ...,
    ) -> memmap | ndarray | MemorizedResult: ...
