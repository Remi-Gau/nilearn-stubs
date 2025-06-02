import os
from typing import Literal, TypeAlias

from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from numpy import ndarray

FilePath: TypeAlias = str | os.PathLike[str]
NiimgLike: TypeAlias = FilePath | Nifti1Image | Nifti2Image

def coord_transform(
    x: float | ndarray,
    y: float | ndarray,
    z: float | ndarray,
    affine: ndarray,
) -> tuple[float | ndarray, float | ndarray, float | ndarray]: ...
def from_matrix_vector(matrix: ndarray, vector: ndarray) -> ndarray: ...
def get_bounds(shape: tuple[int, int, int], affine: ndarray) -> list[tuple[float, float]]: ...
def get_mask_bounds(
    img: NiimgLike,
) -> tuple[float, float, float, float, float, float]: ...
def reorder_img(
    img: NiimgLike,
    resample: Literal["continuous", "linear", "nearest", None] = ...,
    copy_header: bool = ...,
) -> Nifti1Image: ...
def resample_img(
    img: NiimgLike,
    target_affine: ndarray | None = ...,
    target_shape: tuple[int, int, int] | list[int] | None = ...,
    interpolation: Literal["continuous", "linear", "nearest"] = ...,
    copy: bool = ...,
    order: Literal["F", "C"] = ...,
    clip: bool = ...,
    fill_value: float = ...,
    force_resample: bool | None = ...,
    copy_header: bool = ...,
) -> Nifti1Image: ...
def resample_to_img(
    source_img: NiimgLike,
    target_img: NiimgLike,
    interpolation: Literal["continuous", "linear", "nearest"] = ...,
    copy: bool = ...,
    order: Literal["F", "C"] = ...,
    clip: bool = ...,
    fill_value: float = ...,
    force_resample: bool | None = ...,
    copy_header: bool = ...,
) -> Nifti1Image: ...
def to_matrix_vector(transform: ndarray) -> tuple[ndarray, ndarray]: ...
