from pathlib import Path, PosixPath
from typing import Any

from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from nilearn.surface.surface import SurfaceImage
from numpy import (
    memmap,
    ndarray,
)
from sklearn.utils._tags import Tags

class Decoder:
    def __init__(
        self,
        estimator: Any = ...,
        mask: Any | None = ...,
        cv: Any = ...,
        param_grid: Any | None = ...,
        screening_percentile: Any = ...,
        scoring: Any = ...,
        smoothing_fwhm: Any | None = ...,
        standardize: Any = ...,
        target_affine: ndarray | None = ...,
        target_shape: tuple[int, int, int] | list[int] | None = ...,
        mask_strategy: ndarray | str | float | list[int] | int = ...,
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: float | None = ...,
        memory: Memory | str | Path | None = ...,
        memory_level: int = ...,
        n_jobs: ndarray | float | str | int | list[int] = ...,
        verbose: int = ...,
    ): ...
    def __sklearn_tags__(self) -> Tags: ...

class DecoderRegressor:
    def __init__(
        self,
        estimator: Any = ...,
        mask: Any | None = ...,
        cv: ndarray | str | float | list[int] | int = ...,
        param_grid: Any | None = ...,
        screening_percentile: Any = ...,
        scoring: Any = ...,
        smoothing_fwhm: Any | None = ...,
        standardize: Any = ...,
        target_affine: ndarray | None = ...,
        target_shape: tuple[int, int, int] | list[int] | None = ...,
        mask_strategy: ndarray | str | float | list[int] | int = ...,
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: float | None = ...,
        memory: Memory | str | Path | None = ...,
        memory_level: int = ...,
        n_jobs: ndarray | str | float | list[int] | int = ...,
        verbose: int = ...,
    ): ...
    def __sklearn_tags__(self) -> Tags: ...

class FREMClassifier:
    def __init__(
        self,
        estimator: ndarray | str | float | list[int] | int = ...,
        mask: Any | None = ...,
        cv: Any = ...,
        param_grid: Any | None = ...,
        clustering_percentile: ndarray | float | str | int | list[int] = ...,
        screening_percentile: ndarray | str | float | list[int] | int = ...,
        scoring: ndarray | str | float | list[int] | int = ...,
        smoothing_fwhm: Any | None = ...,
        standardize: Any = ...,
        target_affine: ndarray | None = ...,
        target_shape: tuple[int, int, int] | list[int] | None = ...,
        mask_strategy: ndarray | str | float | list[int] | int = ...,
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: float | None = ...,
        memory: Memory | str | Path | None = ...,
        memory_level: int = ...,
        n_jobs: ndarray | float | str | int | list[int] = ...,
        verbose: int = ...,
    ): ...

class FREMRegressor:
    def __init__(
        self,
        estimator: ndarray | float | str | int | list[int] = ...,
        mask: Any | None = ...,
        cv: Any = ...,
        param_grid: Any | None = ...,
        clustering_percentile: ndarray | float | str | int | list[int] = ...,
        screening_percentile: ndarray | float | str | int | list[int] = ...,
        scoring: ndarray | float | str | int | list[int] = ...,
        smoothing_fwhm: Any | None = ...,
        standardize: Any = ...,
        target_affine: ndarray | None = ...,
        target_shape: tuple[int, int, int] | list[int] | None = ...,
        mask_strategy: ndarray | float | str | int | list[int] = ...,
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: float | None = ...,
        memory: Memory | str | Path | None = ...,
        memory_level: int = ...,
        n_jobs: ndarray | float | str | int | list[int] = ...,
        verbose: int = ...,
    ): ...

class _BaseDecoder:
    def __init__(
        self,
        estimator: Any = ...,
        mask: Any | None = ...,
        cv: Any = ...,
        param_grid: Any | None = ...,
        clustering_percentile: ndarray | float | str | int | list[int] = ...,
        screening_percentile: Any = ...,
        scoring: Any | None = ...,
        smoothing_fwhm: Any | None = ...,
        standardize: Any = ...,
        target_affine: ndarray | None = ...,
        target_shape: tuple[int, int, int] | list[int] | None = ...,
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: float | None = ...,
        mask_strategy: ndarray | str | float | list[int] | int = ...,
        is_classification: Any = ...,
        memory: Memory | str | Path | None = ...,
        memory_level: int = ...,
        n_jobs: ndarray | float | str | int | list[int] = ...,
        verbose: int = ...,
    ): ...
    def __sklearn_tags__(self) -> Tags: ...
    def decision_function(
        self, X: SurfaceImage | Nifti1Image | list[PosixPath] | ndarray
    ) -> ndarray: ...
    def fit(
        self,
        X: Any,
        y: ndarray | list[str] | memmap | None,
        groups: ndarray | None = ...,
    ): ...
    def predict(
        self, X: SurfaceImage | list[PosixPath] | Nifti1Image
    ) -> ndarray: ...
    def score(self, X: Nifti1Image, y: ndarray, *args) -> float: ...
