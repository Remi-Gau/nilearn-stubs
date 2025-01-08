import os
from typing import TypeAlias

from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from numpy import memmap, ndarray
from numpy.typing import DTypeLike

MemoryLike: TypeAlias = Memory | str | os.PathLike[str] | None

class NiftiSpheresMasker:
    def __init__(
        self,
        seeds: (
            list[tuple[int, int, int]]
            | list[tuple[float, float, float]]
            | list[int]
            | int
        ),
        radius: int | float | None = ...,
        mask_img: Nifti1Image | int | None = ...,
        allow_overlap: int | bool = ...,
        smoothing_fwhm: int | None = ...,
        standardize: int | str | bool = ...,
        standardize_confounds: int | bool = ...,
        high_variance_confounds: int | bool = ...,
        detrend: int | bool = ...,
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: float | None = ...,
        dtype: DTypeLike | None = ...,
        memory: MemoryLike = ...,
        memory_level: int = ...,
        verbose: int = ...,
        reports: int | bool = ...,
        **kwargs,
    ): ...
    def fit(
        self,
        X: ndarray | memmap | Nifti1Image | None = ...,
        y: ndarray | memmap | None = ...,
    ) -> NiftiSpheresMasker: ...
    def fit_transform(
        self,
        imgs: Nifti1Image | ndarray,
        confounds: ndarray | None = ...,
        sample_mask: None = ...,
    ) -> ndarray: ...
    def inverse_transform(self, region_signals: ndarray) -> Nifti1Image: ...
    def transform_single_imgs(
        self, imgs: Nifti1Image, confounds: None = ..., sample_mask: None = ...
    ) -> ndarray: ...
