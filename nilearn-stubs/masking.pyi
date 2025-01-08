import os
from typing import Literal, TypeAlias

from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from numpy import ndarray
from numpy.typing import DTypeLike

MemoryLike: TypeAlias = Memory | str | os.PathLike[str] | None

FilePath: TypeAlias = str | os.PathLike[str]
NiimgLike: TypeAlias = FilePath | Nifti1Image | Nifti2Image

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
    imgs: NiimgLike,
    mask_img: NiimgLike,
    dtype: DTypeLike | Literal["f"] = ...,
    smoothing_fwhm: int | None = ...,
    ensure_finite: bool = ...,
) -> ndarray: ...
def compute_background_mask(
    data_imgs: NiimgLike,
    border_size: int = ...,
    connected: bool = ...,
    opening: int | bool = ...,
    target_affine: ndarray | None = ...,
    target_shape: tuple[int, int, int] | list[int] | None = ...,
    memory: MemoryLike = ...,
    verbose: int = ...,
) -> Nifti1Image: ...
def compute_brain_mask(
    target_img: NiimgLike,
    threshold: float = ...,
    connected: bool = ...,
    opening: int | bool = ...,
    memory: MemoryLike = ...,
    verbose: int = ...,
    mask_type: Literal["whole-brain", "gm", "wm"] = ...,
) -> Nifti1Image: ...
def compute_epi_mask(
    epi_img: NiimgLike,
    lower_cutoff: float = ...,
    upper_cutoff: float = ...,
    connected: bool = ...,
    opening: int | bool = ...,
    exclude_zeros: bool = ...,
    ensure_finite: bool = ...,
    target_affine: ndarray | None = ...,
    target_shape: tuple[int, int, int] | list[int] | None = ...,
    memory: MemoryLike = ...,
    verbose: int = ...,
) -> Nifti1Image: ...
def compute_multi_background_mask(
    data_imgs: list[NiimgLike],
    border_size: int = ...,
    connected: bool = ...,
    opening: int | bool = ...,
    threshold: float = ...,
    target_affine: ndarray | None = ...,
    target_shape: tuple[int, int, int] | list[int] | None = ...,
    n_jobs: int = ...,
    memory: MemoryLike = ...,
    verbose: int = ...,
) -> Nifti1Image: ...
def compute_multi_brain_mask(
    target_imgs: list[NiimgLike],
    threshold: float = ...,
    connected: bool = ...,
    opening: int | bool = ...,
    memory: MemoryLike = ...,
    verbose: int = ...,
    mask_type: Literal["whole-brain", "gm", "wm"] = ...,
    **kwargs,
) -> Nifti1Image: ...
def compute_multi_epi_mask(
    epi_imgs: list[NiimgLike],
    lower_cutoff: float = ...,
    upper_cutoff: float = ...,
    connected: bool = ...,
    opening: int | bool = ...,
    threshold: float = ...,
    target_affine: ndarray | None = ...,
    target_shape: tuple[int, int, int] | list[int] | None = ...,
    exclude_zeros: bool = ...,
    n_jobs: int = ...,
    memory: MemoryLike = ...,
    verbose: int = ...,
) -> Nifti1Image: ...
def intersect_masks(
    mask_imgs: list[NiimgLike],
    threshold: float = ...,
    connected: bool = ...,
) -> Nifti1Image: ...
def unmask(
    X: list[ndarray] | ndarray,
    mask_img: NiimgLike,
    order: str = ...,
) -> Nifti1Image: ...
