from pathlib import Path, PosixPath
from typing import Any

from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from nilearn.glm.regression import RegressionResults
from nilearn.surface.surface import SurfaceImage
from numpy import ndarray, random, str_
from pandas.core.frame import DataFrame
from sklearn.utils._tags import Tags

def first_level_from_bids(
    dataset_path: int | PosixPath | str,
    task_label: int | str,
    space_label: int | str | None = ...,
    sub_labels: list[str | int] | list[str] | str | list[int] | None = ...,
    img_filters: str
    | list[tuple[int, int]]
    | list[tuple[str, str]]
    | None = ...,
    t_r: float | None = ...,
    slice_time_ref: float | str | None = ...,
    hrf_model: str = ...,
    drift_model: str | None = ...,
    high_pass: float | None = ...,
    drift_order: int = ...,
    fir_delays: None = ...,
    min_onset: int = ...,
    mask_img: None = ...,
    target_affine: ndarray | None = ...,
    target_shape: tuple[int, int, int] | list[int] | None = ...,
    smoothing_fwhm: None = ...,
    memory: Memory | str | Path | None = ...,
    memory_level: int = ...,
    standardize: bool = ...,
    signal_scaling: int = ...,
    noise_model: str = ...,
    verbose: int = ...,
    n_jobs: int = ...,
    minimize_memory: bool = ...,
    derivatives_folder: int | str = ...,
    **kwargs,
) -> (
    tuple[
        list[FirstLevelModel],
        list[list[str]],
        list[list[DataFrame]],
        list[list[DataFrame]],
    ]
    | tuple[
        list[FirstLevelModel],
        list[list[str]],
        list[list[DataFrame]],
        list[None],
    ]
    | tuple[
        list[FirstLevelModel],
        list[list[SurfaceImage]],
        list[list[DataFrame]],
        list[list[DataFrame]],
    ]
): ...
def mean_scaling(Y: ndarray, axis: int = ...) -> tuple[ndarray, ndarray]: ...
def run_glm(
    Y: ndarray,
    X: ndarray,
    noise_model: str = ...,
    bins: int = ...,
    n_jobs: int = ...,
    verbose: int = ...,
    random_state: int | random.mtrand.RandomState | None = ...,
) -> (
    tuple[ndarray, dict[str_, RegressionResults]]
    | tuple[ndarray, dict[float, RegressionResults]]
): ...

class FirstLevelModel:
    def __init__(
        self,
        t_r: float | None = ...,
        slice_time_ref: ndarray | str | float | list[int] | int = ...,
        hrf_model: Any = ...,
        drift_model: Any = ...,
        high_pass: float | None = ...,
        drift_order: ndarray | float | str | int | list[int] = ...,
        fir_delays: Any | None = ...,
        min_onset: ndarray | float | str | int | list[int] = ...,
        mask_img: Any | None = ...,
        target_affine: ndarray | None = ...,
        target_shape: tuple[int, int, int] | list[int] | None = ...,
        smoothing_fwhm: Any | None = ...,
        memory: Memory | str | Path | None = ...,
        memory_level: int = ...,
        standardize: Any = ...,
        signal_scaling: Any = ...,
        noise_model: ndarray | float | str | int | list[int] = ...,
        verbose: int = ...,
        n_jobs: int = ...,
        minimize_memory: Any = ...,
        subject_label: Any | None = ...,
        random_state: int | random.mtrand.RandomState | None = ...,
    ): ...
    def __sklearn_is_fitted__(self) -> bool: ...
    def __sklearn_tags__(self) -> Tags: ...
    def compute_contrast(
        self,
        contrast_def: list[ndarray] | ndarray | str | int,
        stat_type: str | None = ...,
        output_type: str = ...,
    ) -> (
        Nifti1Image
        | dict[str, SurfaceImage]
        | dict[str, Nifti1Image]
        | SurfaceImage
    ): ...
    def fit(
        self,
        run_imgs: Any,
        events: Any | None = ...,
        confounds: DataFrame
        | ndarray
        | list[DataFrame]
        | list[ndarray]
        | None = ...,
        sample_masks: ndarray | None = ...,
        design_matrices: Any | None = ...,
        bins: int = ...,
    ) -> FirstLevelModel: ...
