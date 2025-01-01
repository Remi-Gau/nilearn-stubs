from collections.abc import Iterator
from pathlib import Path, PosixPath
from typing import Any

from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from nibabel.spatialimages import SpatialImage
from numpy import (
    float32,
    float64,
    memmap,
    ndarray,
)
from numpy.ma.core import MaskedArray
from pandas.core.frame import DataFrame
from pandas.core.series import Series

def binarize_img(
    img: Nifti1Image,
    threshold: int | float | str = ...,
    mask_img: None = ...,
    two_sided: bool = ...,
    copy_header: bool = ...,
) -> Nifti1Image: ...
def clean_img(
    imgs: Nifti2Image | Nifti1Image,
    runs: None = ...,
    detrend: bool = ...,
    standardize: bool = ...,
    confounds: DataFrame | None = ...,
    low_pass: float | None = ...,
    high_pass: float | None = ...,
    t_r: float | None = ...,
    ensure_finite: bool = ...,
    mask_img: Nifti1Image | None = ...,
    **kwargs,
) -> Nifti2Image | Nifti1Image: ...
def concat_imgs(
    niimgs: Any,
    dtype: type[float32] | None = ...,
    ensure_ndim: int | None = ...,
    memory: Memory | str | Path | None = ...,
    memory_level: int = ...,
    auto_resample: bool = ...,
    verbose: int = ...,
) -> Nifti1Image: ...
def copy_img(img: int | Nifti1Image) -> Nifti1Image: ...
def crop_img(
    img: Nifti1Image,
    rtol: float = ...,
    copy: bool = ...,
    pad: bool = ...,
    return_offset: bool = ...,
    copy_header: bool = ...,
) -> tuple[Nifti1Image, tuple[slice, slice, slice]] | Nifti1Image: ...
def get_data(img: Any) -> MaskedArray | memmap | ndarray: ...
def high_variance_confounds(
    imgs: Nifti1Image,
    n_confounds: int = ...,
    percentile: float = ...,
    detrend: bool = ...,
    mask_img: Nifti1Image | None = ...,
) -> ndarray: ...
def index_img(
    imgs: list[Nifti1Image] | Nifti1Image | str | PosixPath, index: Any
) -> Nifti1Image: ...
def iter_img(
    imgs: list[Nifti1Image] | Nifti1Image | list[str] | str,
) -> Iterator[Any]: ...
def largest_connected_component_img(
    imgs: str | tuple[Nifti1Image, Nifti1Image] | Nifti1Image | list[str],
) -> list[Nifti1Image] | Nifti1Image: ...
def load_img(
    img: Any, wildcards: bool = ..., dtype: str | None = ...
) -> Nifti1Image: ...
def math_img(
    formula: str, copy_header_from: str | None = ..., **imgs
) -> Nifti1Image: ...
def mean_img(
    imgs: Nifti1Image | list[str] | list[Nifti1Image] | str | Series,
    target_affine: ndarray | None = ...,
    target_shape: tuple[int, int, int] | list[int] | None = ...,
    verbose: int = ...,
    n_jobs: int = ...,
    copy_header: bool = ...,
) -> Nifti1Image: ...
def new_img_like(
    ref_niimg: Any,
    data: MaskedArray | memmap | ndarray,
    affine: memmap | ndarray | None = ...,
    copy_header: bool = ...,
) -> SpatialImage: ...
def smooth_array(
    arr: MaskedArray | memmap | ndarray,
    affine: ndarray,
    fwhm: Any | None = ...,
    ensure_finite: bool = ...,
    copy: bool = ...,
) -> MaskedArray | memmap | ndarray: ...
def smooth_img(
    imgs: list[Nifti2Image]
    | Nifti1Image
    | list[str]
    | str
    | tuple[Nifti1Image, Nifti1Image],
    fwhm: float64 | tuple[float, float, float] | float | None,
) -> list[Nifti1Image] | list[Nifti2Image] | Nifti1Image: ...
def swap_img_hemispheres(img: Nifti1Image) -> Nifti1Image: ...
def threshold_img(
    img: Nifti1Image,
    threshold: float64 | str | float | None,
    cluster_threshold: int = ...,
    two_sided: bool = ...,
    mask_img: Nifti1Image | None = ...,
    copy: bool = ...,
    copy_header: bool = ...,
) -> Nifti1Image: ...
