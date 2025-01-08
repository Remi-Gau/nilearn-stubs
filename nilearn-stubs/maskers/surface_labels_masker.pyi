import os
from pathlib import PosixPath
from typing import Any, TypeAlias

from joblib.memory import Memory
from nilearn.surface.surface import SurfaceImage
from numpy import memmap, ndarray

MemoryLike: TypeAlias = Memory | str | os.PathLike[str] | None

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
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: float | None = ...,
        memory: MemoryLike = ...,
        memory_level: int = ...,
        verbose: int = ...,
        reports: Any = ...,
        cmap: ndarray | float | str | int | list[int] = ...,
        clean_args: Any | None = ...,
    ): ...
    def __sklearn_is_fitted__(self) -> bool: ...
    def fit(
        self,
        img: memmap | ndarray | None = ...,
        y: memmap | ndarray | None = ...,
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
