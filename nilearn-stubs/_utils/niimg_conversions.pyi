from collections.abc import Iterator
from pathlib import PosixPath
from typing import (
    Any,
)

from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from numpy import ndarray

from nilearn._utils.tests.test_niimg_conversions import PhonyNiimage

def _check_fov(img: Nifti1Image, affine: ndarray, shape: tuple[int, int, int]) -> bool: ...
def _index_img(img: Nifti1Image, index: int) -> Nifti1Image: ...
def check_niimg(
    niimg: Any,
    ensure_ndim: int | None = ...,
    atleast_4d: bool = ...,
    dtype: str | None = ...,
    return_iterator: bool = ...,
    wildcards: bool = ...,
) -> PhonyNiimage | Nifti1Image: ...
def check_niimg_3d(
    niimg: str | PosixPath | Nifti1Image | list[Nifti1Image], dtype: str | None = ...
) -> Nifti1Image: ...
def check_niimg_4d(niimg: Any, return_iterator: bool = ..., dtype: None = ...) -> PhonyNiimage | Nifti1Image: ...
def check_same_fov(*args, **kwargs) -> bool: ...
def iter_check_niimg(
    niimgs: Any,
    ensure_ndim: int | None = ...,
    atleast_4d: bool = ...,
    target_fov: None = ...,
    dtype: None = ...,
    memory: Memory | None = ...,
    memory_level: int = ...,
) -> Iterator[Nifti1Image]: ...
