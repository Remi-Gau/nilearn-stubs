import os
from collections.abc import Iterable, Iterator
from pathlib import Path
from typing import Any, Literal

from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from nibabel.spatialimages import SpatialImage
from numpy import (
    memmap,
    ndarray,
)
from numpy.typing import DTypeLike
from typing_extensions import TypeAlias

FilePath: TypeAlias = str | os.PathLike[str]
NiimgLike: TypeAlias = FilePath | Nifti1Image | Nifti2Image

def binarize_img(
    img: NiimgLike,
    threshold: float | str = ...,
    mask_img: NiimgLike | None = ...,
    two_sided: bool = ...,
    copy_header: bool = ...,
) -> Nifti1Image: ...
def clean_img(
    imgs: NiimgLike,
    runs: ndarray | None = ...,
    detrend: bool = ...,
    standardize: bool = ...,
    confounds: str | ndarray | None = ...,
    low_pass: float | None = ...,
    high_pass: float | None = ...,
    t_r: float | None = ...,
    ensure_finite: bool = ...,
    mask_img: NiimgLike | None = ...,
    **kwargs,
) -> Nifti1Image: ...
def concat_imgs(
    niimgs: Iterable[NiimgLike],
    dtype: DTypeLike | None = ...,
    ensure_ndim: int | None = ...,
    memory: Memory | str | Path | None = ...,
    memory_level: int = ...,
    auto_resample: bool = ...,
    verbose: int = ...,
) -> Nifti1Image: ...
def copy_img(img: SpatialImage) -> Nifti1Image: ...
def crop_img(
    img: NiimgLike,
    rtol: float = ...,
    copy: bool = ...,
    pad: bool = ...,
    return_offset: bool = ...,
    copy_header: bool = ...,
) -> tuple[Nifti1Image, tuple[slice, slice, slice]] | Nifti1Image: ...
def get_data(img: NiimgLike) -> ndarray: ...
def high_variance_confounds(
    imgs: NiimgLike,
    n_confounds: int = ...,
    percentile: float = ...,
    detrend: bool = ...,
    mask_img: NiimgLike | None = ...,
) -> ndarray: ...
def index_img(
    imgs: NiimgLike | Iterable[NiimgLike], index: Any
) -> Nifti1Image: ...
def iter_img(
    imgs: NiimgLike | list[NiimgLike],
) -> Iterator[Nifti1Image]: ...
def largest_connected_component_img(
    imgs: NiimgLike | Iterable[NiimgLike],
) -> Nifti1Image | list[Nifti1Image]: ...
def load_img(
    img: NiimgLike, wildcards: bool = ..., dtype: DTypeLike | None = ...
) -> Nifti1Image: ...
def math_img(
    formula: str, copy_header_from: str | None = ..., **imgs
) -> Nifti1Image: ...
def mean_img(
    imgs: NiimgLike | Iterable[NiimgLike],
    target_affine: ndarray | None = ...,
    target_shape: tuple[int, int, int] | list[int] | None = ...,
    verbose: int = ...,
    n_jobs: int = ...,
    copy_header: bool = ...,
) -> Nifti1Image: ...
def new_img_like(
    ref_niimg: NiimgLike,
    data: ndarray,
    affine: memmap | ndarray | None = ...,
    copy_header: bool = ...,
) -> Nifti1Image: ...
def smooth_array(
    arr: ndarray,
    affine: ndarray,
    fwhm: float
    | ndarray
    | tuple[float, ...]
    | list[float]
    | Literal["fast"]
    | None = ...,
    ensure_finite: bool = ...,
    copy: bool = ...,
) -> ndarray: ...
def smooth_img(
    imgs: NiimgLike | Iterable[NiimgLike],
    fwhm: float
    | ndarray
    | tuple[float, ...]
    | list[float]
    | Literal["fast"]
    | None,
) -> Nifti1Image | list[Nifti1Image]: ...
def swap_img_hemispheres(img: NiimgLike) -> Nifti1Image: ...
def threshold_img(
    img: NiimgLike,
    threshold: float | str,
    cluster_threshold: int = ...,
    two_sided: bool = ...,
    mask_img: NiimgLike | None = ...,
    copy: bool = ...,
    copy_header: bool = ...,
) -> Nifti1Image: ...
