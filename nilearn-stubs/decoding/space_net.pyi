from pathlib import Path

from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from nilearn.surface.surface import SurfaceImage
from numpy import (
    ndarray,
)

class BaseSpaceNet:
    def __init__(
        self,
        penalty: str = ...,
        is_classif: bool = ...,
        loss: str | None = ...,
        l1_ratios: float | int = ...,
        alphas: float | list[float] | None = ...,
        n_alphas: int | float = ...,
        mask: SurfaceImage | str | Nifti1Image | None = ...,
        target_affine: ndarray | None = ...,
        target_shape: tuple[int, int, int] | list[int] | None = ...,
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: None = ...,
        max_iter: int = ...,
        tol: float = ...,
        memory: Memory | str | Path | None = ...,
        memory_level: int = ...,
        standardize: bool = ...,
        verbose: int = ...,
        mask_args: None = ...,
        n_jobs: int = ...,
        eps: float = ...,
        cv: int = ...,
        fit_intercept: bool = ...,
        screening_percentile: float | int = ...,
        debias: bool = ...,
    ): ...
    def check_params(self): ...
    def decision_function(self, X: ndarray) -> ndarray: ...
    def fit(
        self, X: SurfaceImage | Nifti1Image, y: ndarray
    ) -> SpaceNetClassifier | BaseSpaceNet | SpaceNetRegressor: ...
    def predict(self, X: Nifti1Image) -> ndarray: ...

class SpaceNetClassifier:
    def __init__(
        self,
        penalty: str = ...,
        loss: str = ...,
        l1_ratios: float = ...,
        alphas: float | None = ...,
        n_alphas: int = ...,
        mask: SurfaceImage | str | Nifti1Image | None = ...,
        target_affine: ndarray | None = ...,
        target_shape: tuple[int, int, int] | list[int] | None = ...,
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: None = ...,
        max_iter: int = ...,
        tol: float = ...,
        memory: Memory | str | Path | None = ...,
        memory_level: int = ...,
        standardize: bool = ...,
        verbose: int = ...,
        n_jobs: int = ...,
        eps: float = ...,
        cv: int = ...,
        fit_intercept: bool = ...,
        screening_percentile: float = ...,
        debias: bool = ...,
    ): ...
    def score(self, X: Nifti1Image, y: ndarray) -> float: ...

class SpaceNetRegressor:
    def __init__(
        self,
        penalty: str = ...,
        l1_ratios: float = ...,
        alphas: float | None = ...,
        n_alphas: int = ...,
        mask: SurfaceImage | str | Nifti1Image | None = ...,
        target_affine: ndarray | None = ...,
        target_shape: tuple[int, int, int] | list[int] | None = ...,
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: None = ...,
        max_iter: int = ...,
        tol: float = ...,
        memory: Memory | str | Path | None = ...,
        memory_level: int = ...,
        standardize: bool = ...,
        verbose: int = ...,
        n_jobs: int = ...,
        eps: float = ...,
        cv: int = ...,
        fit_intercept: bool = ...,
        screening_percentile: float = ...,
        debias: bool = ...,
    ): ...
