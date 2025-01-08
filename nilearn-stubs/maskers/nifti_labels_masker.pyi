import os
from typing import Any, TypeAlias

from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from nilearn.maskers.multi_nifti_labels_masker import MultiNiftiLabelsMasker
from numpy import memmap, ndarray

MemoryLike: TypeAlias = Memory | str | os.PathLike[str] | None

class NiftiLabelsMasker:
    def __init__(
        self,
        labels_img: int | Nifti1Image,
        labels: list[str] | str | int | list[int] | None = ...,
        background_label: int = ...,
        mask_img: int | Nifti1Image | None = ...,
        smoothing_fwhm: int | None = ...,
        standardize: int | str | bool = ...,
        standardize_confounds: int | bool = ...,
        high_variance_confounds: int | bool = ...,
        detrend: int | bool = ...,
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: float | None = ...,
        dtype: int | None = ...,
        resampling_target: int | str | None = ...,
        memory: MemoryLike = ...,
        memory_level: int = ...,
        verbose: int = ...,
        strategy: int | str = ...,
        keep_masked_labels: int | bool = ...,
        reports: int | bool = ...,
        **kwargs,
    ): ...
    def fit(
        self,
        imgs: Any | None = ...,
        y: memmap | ndarray | None = ...,
    ) -> MultiNiftiLabelsMasker | NiftiLabelsMasker: ...
    def fit_transform(
        self,
        imgs: list[Nifti1Image] | Nifti1Image | str | ndarray,
        confounds: ndarray | None = ...,
        sample_mask: list[ndarray] | None = ...,
    ) -> list[ndarray] | ndarray: ...
    def inverse_transform(self, signals: ndarray) -> Nifti1Image: ...
    def transform_single_imgs(
        self,
        imgs: list[Nifti1Image] | Nifti1Image | str,
        confounds: None = ...,
        sample_mask: ndarray | None = ...,
    ) -> ndarray: ...
