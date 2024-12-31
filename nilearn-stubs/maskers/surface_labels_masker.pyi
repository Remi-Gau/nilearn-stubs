from pathlib import PosixPath
from typing import (
    Any,
)

from nilearn.surface.surface import SurfaceImage
from numpy import (
    memmap,
    ndarray,
)
from sklearn.utils.estimator_checks import _NotAnArray

class SurfaceLabelsMasker:
    def __init__(
        self,
        labels_img: Any | None = ...,
        labels: Any | None = ...,
        background_label: ndarray | float | str | int | list[int] = ...,
        mask_img: Any | None = ...,
        smoothing_fwhm: Any | None = ...,
        standardize: Any = ...,
        standardize_confounds: Any = ...,
        detrend: Any = ...,
        high_variance_confounds: Any = ...,
        low_pass: Any | None = ...,
        high_pass: Any | None = ...,
        t_r: Any | None = ...,
        memory: Any | None = ...,
        memory_level: ndarray | float | str | int | list[int] = ...,
        verbose: ndarray | float | str | int | list[int] = ...,
        reports: Any = ...,
        cmap: ndarray | float | str | int | list[int] = ...,
        clean_args: Any | None = ...,
    ): ...
    def __sklearn_is_fitted__(self) -> bool: ...
    def _check_fitted(self): ...
    def _generate_reporting_data(
        self,
    ) -> dict[str, SurfaceImage | list[str] | None]: ...
    @property
    def _labels_data(self) -> ndarray: ...
    def fit(
        self,
        img: memmap | ndarray | _NotAnArray | None = ...,
        y: memmap | ndarray | _NotAnArray | None = ...,
    ) -> SurfaceLabelsMasker: ...
    def fit_transform(
        self,
        img: SurfaceImage | ndarray,
        y: ndarray | None = ...,
        confounds: str | PosixPath | ndarray | None = ...,
        sample_mask: None = ...,
    ) -> ndarray: ...
    def inverse_transform(self, signals: ndarray) -> SurfaceImage: ...
    def transform(
        self,
        img: SurfaceImage | list[SurfaceImage] | ndarray,
        confounds: str | PosixPath | ndarray | None = ...,
        sample_mask: ndarray | None = ...,
    ) -> ndarray: ...
