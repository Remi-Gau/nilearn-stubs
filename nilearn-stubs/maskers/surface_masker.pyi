from typing import (
    Any,
)

from matplotlib.figure import Figure
from nilearn.reporting.html_report import HTMLReport
from nilearn.surface.surface import SurfaceImage
from numpy import (
    memmap,
    ndarray,
)
from sklearn.utils.estimator_checks import _NotAnArray

class SurfaceMasker:
    def __init__(
        self,
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
        memory_level: ndarray | str | float | list[int] | int = ...,
        verbose: ndarray | str | float | list[int] | int = ...,
        reports: Any = ...,
        cmap: ndarray | str | float | list[int] | int = ...,
        clean_args: Any | None = ...,
    ): ...
    def __sklearn_is_fitted__(self) -> bool: ...
    def _check_fitted(self): ...
    def _create_figure_for_report(self) -> Figure: ...
    def _fit_mask_img(self, img: Any): ...
    def _reporting(self) -> list[str]: ...
    def fit(
        self,
        img: Any | None = ...,
        y: _NotAnArray | ndarray | memmap | None = ...,
    ) -> SurfaceMasker: ...
    def fit_transform(
        self,
        img: ndarray,
        y: ndarray | None = ...,
        confounds: None = ...,
        sample_mask: None = ...,
    ): ...
    def generate_report(self) -> HTMLReport: ...
    def inverse_transform(self, signals: ndarray) -> SurfaceImage: ...
    def transform(
        self,
        img: SurfaceImage | ndarray | list[SurfaceImage],
        confounds: None = ...,
        sample_mask: None = ...,
    ) -> ndarray: ...
