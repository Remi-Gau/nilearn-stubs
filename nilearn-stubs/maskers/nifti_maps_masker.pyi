import os
from typing import Any, TypeAlias

from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from numpy import memmap, ndarray
from numpy.typing import DTypeLike

from nilearn.maskers.multi_nifti_maps_masker import MultiNiftiMapsMasker

MemoryLike: TypeAlias = Memory | str | os.PathLike[str] | None

class NiftiMapsMasker:
    def __init__(
        self,
        maps_img: int | Nifti1Image | str,
        mask_img: int | Nifti1Image | str | None = ...,
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
        resampling_target: int | str | None = ...,
        keep_masked_maps: int | bool = ...,
        memory: MemoryLike = ...,
        memory_level: int = ...,
        verbose: int = ...,
        reports: int | bool = ...,
        **kwargs,
    ): ...
    def fit(
        self,
        imgs: Any | None = ...,
        y: ndarray | memmap | None = ...,
    ) -> MultiNiftiMapsMasker | NiftiMapsMasker: ...
    def fit_transform(
        self,
        imgs: Nifti1Image | ndarray | list[Nifti1Image],
        confounds: ndarray | None = ...,
        sample_mask: list[ndarray] | None = ...,
    ) -> list[ndarray] | ndarray: ...
    def inverse_transform(self, region_signals: ndarray) -> Nifti1Image: ...
    def transform_single_imgs(
        self,
        imgs: Nifti1Image | list[Nifti1Image],
        confounds: None = ...,
        sample_mask: ndarray | None = ...,
    ) -> ndarray: ...
