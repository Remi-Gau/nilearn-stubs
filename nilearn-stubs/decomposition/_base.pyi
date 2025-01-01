from pathlib import Path
from typing import (
    Any,
)

from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from nilearn.decomposition._multi_pca import _MultiPCA
from nilearn.decomposition.canica import CanICA
from nilearn.decomposition.dict_learning import DictLearning
from nilearn.regions.parcellations import Parcellations
from numpy import (
    float64,
    memmap,
    ndarray,
)
from sklearn.utils._tags import Tags
from sklearn.utils.estimator_checks import _NotAnArray

class _BaseDecomposition:
    def __init__(
        self,
        n_components: Any = ...,
        random_state: Any | None = ...,
        mask: Any | None = ...,
        smoothing_fwhm: Any | None = ...,
        standardize: Any = ...,
        standardize_confounds: Any = ...,
        detrend: Any = ...,
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: Any | None = ...,
        target_affine: ndarray | None = ...,
        target_shape: tuple[int, int, int] | list[int] | None = ...,
        mask_strategy: ndarray | float | str | int | list[int] = ...,
        mask_args: Any | None = ...,
        memory: Memory | str | Path | None = ...,
        memory_level: ndarray | float | str | int | list[int] = ...,
        n_jobs: ndarray | float | str | int | list[int] = ...,
        verbose: int = ...,
    ): ...
    def __sklearn_tags__(self) -> Tags: ...
    def fit(
        self,
        imgs: Any,
        y: memmap | ndarray | _NotAnArray | None = ...,
        confounds: list[ndarray] | None = ...,
    ) -> _MultiPCA | DictLearning | Parcellations | CanICA: ...
    def inverse_transform(
        self, loadings: list[ndarray]
    ) -> list[Nifti1Image]: ...
    def score(
        self,
        imgs: Nifti1Image | list[Nifti1Image],
        confounds: None = ...,
        per_component: bool = ...,
    ) -> float64 | ndarray: ...
    def transform(
        self, imgs: list[Nifti1Image] | ndarray, confounds: None = ...
    ) -> list[ndarray]: ...
