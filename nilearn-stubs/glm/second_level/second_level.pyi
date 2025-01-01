from pathlib import PosixPath
from typing import Any

from nibabel.nifti1 import Nifti1Image
from nilearn.maskers.nifti_masker import NiftiMasker
from nilearn.surface.surface import SurfaceImage
from numpy import ndarray
from pandas.core.frame import DataFrame
from sklearn.utils._tags import Tags

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
    random_state: None = ...,
    n_jobs: int = ...,
    verbose: int = ...,
    threshold: float | None = ...,
    tfce: bool = ...,
) -> dict[str, Nifti1Image] | Nifti1Image: ...

class SecondLevelModel:
    def __init__(
        self,
        mask_img: Any | None = ...,
        target_affine: Any | None = ...,
        target_shape: Any | None = ...,
        smoothing_fwhm: Any | None = ...,
        memory: Any | None = ...,
        memory_level: ndarray | float | str | int | list[int] = ...,
        verbose: ndarray | float | str | int | list[int] = ...,
        n_jobs: ndarray | float | str | int | list[int] = ...,
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
