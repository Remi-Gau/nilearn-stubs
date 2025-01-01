from pathlib import PosixPath

from nibabel.freesurfer.mghformat import MGHImage
from nibabel.nifti1 import Nifti1Image
from nilearn.plotting.img_plotting import _MNI152Template
from numpy import (
    float64,
    ndarray,
)

def coord_transform(
    x: float64 | ndarray | float | list[int],
    y: float64 | ndarray | float | list[int],
    z: float64 | ndarray | float | list[int] | int,
    affine: ndarray,
) -> tuple[float, float, float] | tuple[ndarray, ndarray, ndarray]: ...
def from_matrix_vector(matrix: ndarray, vector: ndarray) -> ndarray: ...
def get_bounds(
    shape: tuple[int, int, int], affine: ndarray
) -> list[tuple[float64, float64]]: ...
def get_mask_bounds(
    img: _MNI152Template | Nifti1Image | None,
) -> tuple[float64, float64, float64, float64, float64, float64]: ...
def reorder_img(
    img: _MNI152Template | Nifti1Image,
    resample: str | None = ...,
    copy_header: bool = ...,
) -> _MNI152Template | Nifti1Image: ...
def resample_img(
    img: PosixPath | str | Nifti1Image | MGHImage,
    target_affine: ndarray | None = ...,
    target_shape: tuple[int, int, int] | list[int] | None = ...,
    interpolation: str = ...,
    copy: bool = ...,
    order: str = ...,
    clip: bool = ...,
    fill_value: float = ...,
    force_resample: bool | None = ...,
    copy_header: bool = ...,
) -> MGHImage | Nifti1Image: ...
def resample_to_img(
    source_img: Nifti1Image,
    target_img: Nifti1Image,
    interpolation: str = ...,
    copy: bool = ...,
    order: str = ...,
    clip: bool = ...,
    fill_value: float = ...,
    force_resample: bool | None = ...,
    copy_header: bool = ...,
) -> Nifti1Image: ...
def to_matrix_vector(transform: ndarray) -> tuple[ndarray, ndarray]: ...
