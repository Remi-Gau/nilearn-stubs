import os
from pathlib import PosixPath
from typing import Any

from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from nilearn.maskers.nifti_masker import NiftiMasker
from nilearn.surface.surface import SurfaceImage
from numpy import ndarray, random
from pandas.core.frame import DataFrame
from sklearn.utils._tags import Tags
from typing_extensions import TypeAlias

MemoryLike: TypeAlias = Memory | str | os.PathLike[str] | None

def non_parametric_inference(
    second_level_input: Any,
    confounds: DataFrame | None = ...,
    design_matrix: DataFrame | None = ...,
    second_level_contrast: ndarray | str | list[int] | None = ...,
    first_level_contrast: str | None = ...,
    mask: NiftiMasker | PosixPath | None = ...,
    smoothing_fwhm: float | None = ...,
    model_intercept: bool = ...,
    n_perm: int = ...,
    two_sided_test: bool = ...,
    random_state: int | random.RandomState | None = ...,
    n_jobs: int = ...,
    verbose: int = ...,
    threshold: float | None = ...,
    tfce: bool = ...,
) -> dict[str, Nifti1Image] | Nifti1Image: ...

class SecondLevelModel:
    def __init__(
        self,
        mask_img: Any | None = ...,
        target_affine: ndarray | None = ...,
        target_shape: tuple[int, int, int] | list[int] | None = ...,
        smoothing_fwhm: Any | None = ...,
        memory: MemoryLike = ...,
        memory_level: int = ...,
        verbose: int = ...,
        n_jobs: int = ...,
        minimize_memory: Any = ...,
    ): ...
    def __sklearn_tags__(self) -> Tags: ...
    def compute_contrast(
        self,
        second_level_contrast: ndarray | str | list[int] | None = ...,
        first_level_contrast: str | None = ...,
        second_level_stat_type: str | None = ...,
        output_type: str = ...,
    ) -> (
        SurfaceImage
        | dict[str, Nifti1Image]
        | Nifti1Image
        | dict[str, SurfaceImage]
    ): ...
    def fit(
        self,
        second_level_input: Any,
        confounds: Any | None = ...,
        design_matrix: Any | None = ...,
    ) -> SecondLevelModel: ...
