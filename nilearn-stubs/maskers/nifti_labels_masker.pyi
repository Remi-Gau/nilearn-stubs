from typing import Any

from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from nilearn.maskers.multi_nifti_labels_masker import MultiNiftiLabelsMasker
from numpy import float32, int8, int32, int64, memmap, ndarray
from sklearn.utils.estimator_checks import _NotAnArray

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
        low_pass: int | None = ...,
        high_pass: int | None = ...,
        t_r: int | None = ...,
        dtype: int | None = ...,
        resampling_target: int | str | None = ...,
        memory: int | Memory | None = ...,
        memory_level: int = ...,
        verbose: int = ...,
        strategy: int | str = ...,
        keep_masked_labels: int | bool = ...,
        reports: int | bool = ...,
        **kwargs,
    ): ...
    def _check_fitted(self): ...
    def _check_mismatch_labels_regions(
        self,
        region_ids: list[int32] | list[int8] | list[float32] | ndarray,
        tolerant: bool = ...,
        resampling_done: bool = ...,
    ): ...
    def _get_labels_values(
        self, labels_image: int | Nifti1Image
    ) -> ndarray: ...
    def _number_of_regions(
        self, region_ids: list[int32] | list[float32] | ndarray
    ) -> int64: ...
    def _resample_labels(
        self, imgs_: Nifti1Image
    ) -> MultiNiftiLabelsMasker | NiftiLabelsMasker: ...
    def _sanitize_labels(
        self, labels: list[str] | list[int] | str | None
    ) -> list[str] | None: ...
    def fit(
        self,
        imgs: Any | None = ...,
        y: memmap | _NotAnArray | ndarray | None = ...,
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
