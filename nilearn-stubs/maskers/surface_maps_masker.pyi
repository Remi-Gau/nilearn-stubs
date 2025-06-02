import os
from pathlib import PosixPath
from typing import Any, TypeAlias

from joblib.memory import Memory
from numpy import memmap, ndarray

from nilearn.surface.surface import SurfaceImage

MemoryLike: TypeAlias = Memory | str | os.PathLike[str] | None

class SurfaceMapsMasker:
    def __init__(
        self,
        maps_img: Any | None = ...,
        mask_img: Any | None = ...,
        allow_overlap: Any = ...,
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
        img: memmap | ndarray | None = ...,
        y: ndarray | memmap | None = ...,
    ) -> SurfaceMapsMasker: ...
    def fit_transform(
        self,
        img: SurfaceImage | ndarray,
        y: ndarray | None = ...,
        confounds: PosixPath | str | ndarray | None = ...,
        sample_mask: None = ...,
    ) -> ndarray: ...
    def inverse_transform(self, region_signals: ndarray | None) -> SurfaceImage: ...
    def transform(
        self,
        img: SurfaceImage | ndarray | None,
        confounds: str | PosixPath | ndarray | None = ...,
        sample_mask: ndarray | None = ...,
    ) -> ndarray: ...
