from pathlib import PosixPath
from typing import (
    Any,
)

from nibabel.nifti1 import Nifti1Image
from nilearn.surface.surface import SurfaceImage
from numpy import (
    int64,
    memmap,
    ndarray,
    str_,
)
from sklearn.utils._tags import Tags
from sklearn.utils.estimator_checks import _NotAnArray

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
        target_affine: Any | None = ...,
        target_shape: Any | None = ...,
        mask_strategy: ndarray | str | float | list[int] | int = ...,
        low_pass: Any | None = ...,
        high_pass: Any | None = ...,
        t_r: Any | None = ...,
        memory: Any | None = ...,
        memory_level: ndarray | float | str | int | list[int] = ...,
        n_jobs: ndarray | float | str | int | list[int] = ...,
        verbose: ndarray | float | str | int | list[int] = ...,
    ): ...
    def __sklearn_tags__(self) -> Tags: ...
    def _more_tags(self) -> Tags: ...

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
        target_affine: Any | None = ...,
        target_shape: Any | None = ...,
        mask_strategy: ndarray | str | float | list[int] | int = ...,
        low_pass: Any | None = ...,
        high_pass: Any | None = ...,
        t_r: Any | None = ...,
        memory: Any | None = ...,
        memory_level: ndarray | str | float | list[int] | int = ...,
        n_jobs: ndarray | str | float | list[int] | int = ...,
        verbose: ndarray | str | float | list[int] | int = ...,
    ): ...
    def __sklearn_tags__(self) -> Tags: ...
    def _more_tags(self) -> Tags: ...

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
        target_affine: Any | None = ...,
        target_shape: Any | None = ...,
        mask_strategy: ndarray | str | float | list[int] | int = ...,
        low_pass: Any | None = ...,
        high_pass: Any | None = ...,
        t_r: Any | None = ...,
        memory: Any | None = ...,
        memory_level: ndarray | float | str | int | list[int] = ...,
        n_jobs: ndarray | float | str | int | list[int] = ...,
        verbose: ndarray | float | str | int | list[int] = ...,
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
        target_affine: Any | None = ...,
        target_shape: Any | None = ...,
        mask_strategy: ndarray | float | str | int | list[int] = ...,
        low_pass: Any | None = ...,
        high_pass: Any | None = ...,
        t_r: Any | None = ...,
        memory: Any | None = ...,
        memory_level: ndarray | float | str | int | list[int] = ...,
        n_jobs: ndarray | float | str | int | list[int] = ...,
        verbose: ndarray | float | str | int | list[int] = ...,
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
        target_affine: Any | None = ...,
        target_shape: Any | None = ...,
        low_pass: Any | None = ...,
        high_pass: Any | None = ...,
        t_r: Any | None = ...,
        mask_strategy: ndarray | str | float | list[int] | int = ...,
        is_classification: Any = ...,
        memory: Any | None = ...,
        memory_level: ndarray | float | str | int | list[int] = ...,
        n_jobs: ndarray | float | str | int | list[int] = ...,
        verbose: ndarray | float | str | int | list[int] = ...,
    ): ...
    def __sklearn_tags__(self) -> Tags: ...
    def _apply_mask(self, X: Any) -> ndarray: ...
    def _binarize_y(self, y: ndarray) -> ndarray: ...
    def _fetch_parallel_fit_outputs(
        self, parallel_fit_outputs: list[Any], y: ndarray, n_problems: int
    ) -> Any: ...
    def _more_tags(self) -> Tags: ...
    def _output_image(
        self, classes: ndarray | list[str], coefs: ndarray, std_coef: ndarray
    ) -> (
        tuple[dict[str_, Nifti1Image], dict[str_, Nifti1Image]]
        | tuple[dict[int64, SurfaceImage], dict[int64, SurfaceImage]]
        | tuple[dict[int64, Nifti1Image], dict[int64, Nifti1Image]]
        | tuple[dict[str, Nifti1Image], dict[str, Nifti1Image]]
        | tuple[dict[str, SurfaceImage], dict[str, SurfaceImage]]
    ): ...
    def _predict_dummy(self, n_samples: int) -> ndarray: ...
    def _set_scorer(self): ...
    def decision_function(
        self, X: SurfaceImage | Nifti1Image | list[PosixPath] | ndarray
    ) -> ndarray: ...
    def fit(
        self,
        X: Any,
        y: _NotAnArray | ndarray | list[str] | memmap | None,
        groups: ndarray | None = ...,
    ): ...
    def predict(
        self, X: SurfaceImage | list[PosixPath] | Nifti1Image
    ) -> ndarray: ...
    def score(self, X: Nifti1Image, y: ndarray, *args) -> float: ...
