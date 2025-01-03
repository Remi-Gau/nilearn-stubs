import os
from typing import Any, Literal

from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from nilearn.decomposition._multi_pca import _MultiPCA
from nilearn.decomposition.canica import CanICA
from nilearn.decomposition.dict_learning import DictLearning
from nilearn.maskers import NiftiMasker, SurfaceMasker
from nilearn.regions.parcellations import Parcellations
from nilearn.surface import SurfaceImage
from numpy import (
    float64,
    memmap,
    ndarray,
    random,
)
from sklearn.utils._tags import Tags
from typing_extensions import TypeAlias

MemoryLike: TypeAlias = Memory | str | os.PathLike[str] | None
NiimgLike: TypeAlias = str | os.PathLike[str] | Nifti1Image | Nifti2Image
MemoryLike: TypeAlias = Memory | str | os.PathLike[str] | None

class _BaseDecomposition:
    def __init__(
        self,
        n_components: Any = ...,
        random_state: int | random.RandomState | None = ...,
        mask: NiimgLike
        | SurfaceImage
        | SurfaceMasker
        | NiftiMasker
        | None = ...,
        smoothing_fwhm: float | None = ...,
        standardize: bool = ...,
        standardize_confounds: bool = ...,
        detrend: bool = ...,
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: float | None = ...,
        target_affine: ndarray | None = ...,
        target_shape: tuple[int, int, int] | list[int] | None = ...,
        mask_strategy: Literal[
            "background",
            "epi",
            "whole-brain-template",
            "gm-template",
            "wm-template",
        ] = ...,
        mask_args: Any | None = ...,
        memory: MemoryLike = ...,
        memory_level: int = ...,
        n_jobs: int = ...,
        verbose: int = ...,
    ): ...
    def __sklearn_tags__(self) -> Tags: ...
    def fit(
        self,
        imgs: Any,
        y: memmap | ndarray | None = ...,
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
