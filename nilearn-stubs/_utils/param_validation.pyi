from typing import (
    Any,
    Callable,
)

from nibabel.nifti1 import Nifti1Image
from numpy import (
    float64,
    ndarray,
)
from sklearn.feature_selection._univariate_selection import SelectPercentile

def _cast_to_int32(sample_mask: ndarray) -> ndarray: ...
def _convert_bool2index(sample_mask: ndarray) -> ndarray: ...
def _get_mask_extent(mask_img: Nifti1Image) -> float64: ...
def adjust_screening_percentile(
    screening_percentile: int, mask_img: Nifti1Image, verbose: int = ..., mesh_n_vertices: None = ...
) -> float64: ...
def check_feature_screening(
    screening_percentile: int | None,
    mask_img: Nifti1Image,
    is_classification: bool,
    verbose: int = ...,
    mesh_n_vertices: None = ...,
) -> SelectPercentile | None: ...
def check_params(fn_dict: dict[str, Any]) -> None: ...
def check_run_sample_masks(n_runs: int, sample_masks: str | ndarray | list[ndarray]) -> list[ndarray]: ...
def check_threshold(
    threshold: str | int | float | object | float64,
    data: ndarray,
    percentile_func: Callable,
    name: str = ...,
    two_sided: bool = ...,
) -> float64 | float | int: ...
