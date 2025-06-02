import os
from typing import Any, TypeAlias

from joblib.memory import Memory
from numpy import memmap, ndarray

from nilearn.reporting.html_report import HTMLReport
from nilearn.surface.surface import SurfaceImage

MemoryLike: TypeAlias = Memory | str | os.PathLike[str] | None

class SurfaceMasker:
    def __init__(
        self,
        mask_img: Any | None = ...,
        smoothing_fwhm: Any | None = ...,
        standardize: Any = ...,
        standardize_confounds: Any = ...,
        detrend: Any = ...,
        high_variance_confounds: Any = ...,
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: float | None = ...,
        memory: MemoryLike = ...,
        memory_level: int = ...,
        verbose: int = ...,
        reports: Any = ...,
        cmap: ndarray | str | float | list[int] | int = ...,
        clean_args: Any | None = ...,
    ): ...
    def __sklearn_is_fitted__(self) -> bool: ...
    def fit(
        self,
        img: Any | None = ...,
        y: ndarray | memmap | None = ...,
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
