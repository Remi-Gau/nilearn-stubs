from pathlib import PosixPath
from typing import (
    Any,
)

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
    t_r: int | str | None = ...,
    slice_time_ref: float | int | str | None = ...,
    hrf_model: str = ...,
    drift_model: str | None = ...,
    high_pass: float = ...,
    drift_order: int = ...,
    fir_delays: None = ...,
    min_onset: int = ...,
    mask_img: None = ...,
    target_affine: None = ...,
    target_shape: None = ...,
    smoothing_fwhm: None = ...,
    memory: None = ...,
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
        t_r: Any | None = ...,
        slice_time_ref: ndarray | str | float | list[int] | int = ...,
        hrf_model: Any = ...,
        drift_model: Any = ...,
        high_pass: ndarray | str | float | list[int] | int = ...,
        drift_order: ndarray | float | str | int | list[int] = ...,
        fir_delays: Any | None = ...,
        min_onset: ndarray | float | str | int | list[int] = ...,
        mask_img: Any | None = ...,
        target_affine: Any | None = ...,
        target_shape: Any | None = ...,
        smoothing_fwhm: Any | None = ...,
        memory: Any | None = ...,
        memory_level: ndarray | float | str | int | list[int] = ...,
        standardize: Any = ...,
        signal_scaling: Any = ...,
        noise_model: ndarray | float | str | int | list[int] = ...,
        verbose: ndarray | float | str | int | list[int] = ...,
        n_jobs: ndarray | float | str | int | list[int] = ...,
        minimize_memory: Any = ...,
        subject_label: Any | None = ...,
        random_state: Any | None = ...,
    ): ...
    def __sklearn_is_fitted__(self) -> bool: ...
    def __sklearn_tags__(self) -> Tags: ...
    def _check_fit_inputs(
        self,
        run_imgs: Any,
        events: Any,
        confounds: DataFrame
        | ndarray
        | list[DataFrame]
        | list[ndarray]
        | None,
        sample_masks: ndarray | None,
        design_matrices: Any,
    ) -> Any: ...
    def _check_fitted(self): ...
    def _create_all_designs(
        self,
        run_imgs: list[PosixPath | str | Nifti1Image | SurfaceImage],
        events: list[DataFrame] | None,
        confounds: list[ndarray] | list[DataFrame] | None,
        design_matrices: list[DataFrame] | None,
    ) -> list[DataFrame]: ...
    def _create_single_design(
        self,
        n_scans: int,
        events: list[DataFrame],
        confounds: list[DataFrame] | list[ndarray] | None,
        run_idx: int,
    ) -> DataFrame: ...
    def _fit_single_run(
        self,
        sample_masks: list[ndarray] | None,
        bins: int,
        run_img: Nifti1Image | PosixPath | str | SurfaceImage,
        run_idx: int,
    ): ...
    def _get_voxelwise_model_attribute(
        self, attribute: str, result_as_time_series: bool
    ) -> list[Nifti1Image | SurfaceImage]: ...
    def _log(
        self,
        step: str,
        run_idx: int | None = ...,
        n_runs: int | None = ...,
        t0: float | None = ...,
        time_in_second: float | None = ...,
    ): ...
    def _more_tags(self) -> Tags: ...
    def _prepare_mask(
        self, run_img: Nifti1Image | PosixPath | str | SurfaceImage
    ): ...
    def _report_progress(
        self, run_idx: int, n_runs: int, t0: float
    ) -> str: ...
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
