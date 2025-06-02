import os
from typing import Any, Literal, TypeAlias

from joblib.memory import MemorizedResult, Memory
from nibabel.nifti1 import Nifti1Image
from numpy import memmap, ndarray
from numpy.typing import DTypeLike

MemoryLike: TypeAlias = Memory | str | os.PathLike[str] | None

class MultiNiftiMasker:
    def __init__(
        self,
        mask_img: int | str | Nifti1Image | None = ...,
        smoothing_fwhm: int | None = ...,
        standardize: int | bool | str = ...,
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
        mask_args: int | dict[str, int] | None = ...,
        dtype: DTypeLike | None = ...,
        memory: MemoryLike = ...,
        memory_level: int = ...,
        n_jobs: int = ...,
        verbose: int = ...,
        cmap: str = ...,
        **kwargs,
    ): ...
    def fit(
        self,
        imgs: Any | None = ...,
        y: memmap | ndarray | None = ...,
    ) -> MultiNiftiMasker: ...
    def transform(
        self,
        imgs: list[Nifti1Image] | list[list[Nifti1Image]] | ndarray | Nifti1Image,
        confounds: None = ...,
        sample_mask: None = ...,
    ) -> MemorizedResult | list[ndarray] | ndarray | list[MemorizedResult]: ...
    def transform_imgs(
        self,
        imgs_list: list[Nifti1Image | list[Nifti1Image]],
        confounds: None = ...,
        sample_mask: None = ...,
        copy: bool = ...,
        n_jobs: int = ...,
    ) -> list[ndarray | MemorizedResult]: ...
