from typing import Any

from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from numpy import memmap, ndarray
from numpy.dtypes import Float32DType, Float64DType, Int32DType

__all__ = [
    "apply_mask",
    "compute_background_mask",
    "compute_brain_mask",
    "compute_epi_mask",
    "compute_multi_background_mask",
    "compute_multi_brain_mask",
    "compute_multi_epi_mask",
    "intersect_masks",
    "unmask",
]

def apply_mask(
    imgs: str | Nifti1Image,
    mask_img: str | Nifti1Image,
    dtype: Float64DType | Float32DType | Int32DType | str = ...,
    smoothing_fwhm: int | None = ...,
    ensure_finite: bool = ...,
) -> ndarray: ...
def compute_background_mask(
    data_imgs: memmap | ndarray | list[Nifti1Image] | Nifti1Image,
    border_size: int = ...,
    connected: bool = ...,
    opening: int | bool = ...,
    target_affine: None = ...,
    target_shape: None = ...,
    memory: Memory | None = ...,
    verbose: int = ...,
) -> Nifti1Image: ...
def compute_brain_mask(
    target_img: Nifti1Image,
    threshold: int | float = ...,
    connected: bool = ...,
    opening: int = ...,
    memory: Memory | None = ...,
    verbose: int = ...,
    mask_type: str = ...,
) -> Nifti1Image: ...
def compute_epi_mask(
    epi_img: Nifti1Image,
    lower_cutoff: float = ...,
    upper_cutoff: float = ...,
    connected: bool = ...,
    opening: int | bool = ...,
    exclude_zeros: bool = ...,
    ensure_finite: bool = ...,
    target_affine: ndarray | None = ...,
    target_shape: tuple[int, int, int] | None = ...,
    memory: None = ...,
    verbose: int = ...,
) -> Nifti1Image: ...
def compute_multi_background_mask(
    data_imgs: memmap | list[Nifti1Image] | ndarray | list[list[Nifti1Image]],
    border_size: int = ...,
    connected: bool = ...,
    opening: int = ...,
    threshold: float = ...,
    target_affine: None = ...,
    target_shape: None = ...,
    n_jobs: int = ...,
    memory: Memory | None = ...,
    verbose: int = ...,
) -> Nifti1Image: ...
def compute_multi_brain_mask(
    target_imgs: list[Any | Nifti1Image],
    threshold: float = ...,
    connected: bool = ...,
    opening: int = ...,
    memory: Memory | None = ...,
    verbose: int = ...,
    mask_type: str = ...,
    **kwargs,
) -> Nifti1Image: ...
def compute_multi_epi_mask(
    epi_imgs: list[Any | Nifti1Image],
    lower_cutoff: float = ...,
    upper_cutoff: float = ...,
    connected: bool = ...,
    opening: int = ...,
    threshold: float = ...,
    target_affine: ndarray | None = ...,
    target_shape: tuple[int, int, int] | None = ...,
    exclude_zeros: bool = ...,
    n_jobs: int = ...,
    memory: None = ...,
    verbose: int = ...,
) -> Nifti1Image: ...
def intersect_masks(
    mask_imgs: list[str | Nifti1Image],
    threshold: float = ...,
    connected: bool = ...,
) -> Nifti1Image: ...
def unmask(
    X: list[bool] | list[ndarray] | ndarray,
    mask_img: str | Nifti1Image,
    order: str = ...,
) -> list[Nifti1Image] | Nifti1Image: ...
