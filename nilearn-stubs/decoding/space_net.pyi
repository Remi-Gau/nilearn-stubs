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
        target_affine: None = ...,
        target_shape: None = ...,
        low_pass: None = ...,
        high_pass: None = ...,
        t_r: None = ...,
        max_iter: int = ...,
        tol: float = ...,
        memory: Memory | None = ...,
        memory_level: int = ...,
        standardize: bool = ...,
        verbose: int | bool = ...,
        mask_args: None = ...,
        n_jobs: int = ...,
        eps: float = ...,
        cv: int = ...,
        fit_intercept: bool = ...,
        screening_percentile: float | int = ...,
        debias: bool = ...,
    ): ...
    def _set_coef_and_intercept(self, w: ndarray): ...
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
        target_affine: None = ...,
        target_shape: None = ...,
        low_pass: None = ...,
        high_pass: None = ...,
        t_r: None = ...,
        max_iter: int = ...,
        tol: float = ...,
        memory: None = ...,
        memory_level: int = ...,
        standardize: bool = ...,
        verbose: int | bool = ...,
        n_jobs: int = ...,
        eps: float = ...,
        cv: int = ...,
        fit_intercept: bool = ...,
        screening_percentile: float = ...,
        debias: bool = ...,
    ): ...
    def _binarize_y(self, y: ndarray) -> ndarray: ...
    def score(self, X: Nifti1Image, y: ndarray) -> float: ...

class SpaceNetRegressor:
    def __init__(
        self,
        penalty: str = ...,
        l1_ratios: float = ...,
        alphas: float | None = ...,
        n_alphas: int = ...,
        mask: SurfaceImage | str | Nifti1Image | None = ...,
        target_affine: None = ...,
        target_shape: None = ...,
        low_pass: None = ...,
        high_pass: None = ...,
        t_r: None = ...,
        max_iter: int = ...,
        tol: float = ...,
        memory: None = ...,
        memory_level: int = ...,
        standardize: bool = ...,
        verbose: int | bool = ...,
        n_jobs: int = ...,
        eps: float = ...,
        cv: int = ...,
        fit_intercept: bool = ...,
        screening_percentile: float = ...,
        debias: bool = ...,
    ): ...
