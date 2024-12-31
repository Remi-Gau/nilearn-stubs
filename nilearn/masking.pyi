from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from numpy import (
    memmap,
    ndarray,
)
from numpy.dtypes import (
    Float32DType,
    Float64DType,
    Int32DType,
)
from typing import (
    Any,
    List,
    Optional,
    Tuple,
    Union,
)

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
    imgs: Union[str, Nifti1Image],
    mask_img: Union[str, Nifti1Image],
    dtype: Union[Float64DType, Float32DType, Int32DType, str] = ...,
    smoothing_fwhm: Optional[int] = ...,
    ensure_finite: bool = ...
) -> ndarray: ...





def compute_background_mask(
    data_imgs: Union[memmap, ndarray, List[Nifti1Image], Nifti1Image],
    border_size: int = ...,
    connected: bool = ...,
    opening: Union[int, bool] = ...,
    target_affine: None = ...,
    target_shape: None = ...,
    memory: Optional[Memory] = ...,
    verbose: int = ...
) -> Nifti1Image: ...


def compute_brain_mask(
    target_img: Nifti1Image,
    threshold: Union[int, float] = ...,
    connected: bool = ...,
    opening: int = ...,
    memory: Optional[Memory] = ...,
    verbose: int = ...,
    mask_type: str = ...
) -> Nifti1Image: ...


def compute_epi_mask(
    epi_img: Nifti1Image,
    lower_cutoff: float = ...,
    upper_cutoff: float = ...,
    connected: bool = ...,
    opening: Union[int, bool] = ...,
    exclude_zeros: bool = ...,
    ensure_finite: bool = ...,
    target_affine: Optional[ndarray] = ...,
    target_shape: Optional[Tuple[int, int, int]] = ...,
    memory: None = ...,
    verbose: int = ...
) -> Nifti1Image: ...


def compute_multi_background_mask(
    data_imgs: Union[memmap, List[Nifti1Image], ndarray, List[List[Nifti1Image]]],
    border_size: int = ...,
    connected: bool = ...,
    opening: int = ...,
    threshold: float = ...,
    target_affine: None = ...,
    target_shape: None = ...,
    n_jobs: int = ...,
    memory: Optional[Memory] = ...,
    verbose: int = ...
) -> Nifti1Image: ...


def compute_multi_brain_mask(
    target_imgs: List[Union[Any, Nifti1Image]],
    threshold: float = ...,
    connected: bool = ...,
    opening: int = ...,
    memory: Optional[Memory] = ...,
    verbose: int = ...,
    mask_type: str = ...,
    **kwargs
) -> Nifti1Image: ...


def compute_multi_epi_mask(
    epi_imgs: List[Union[Any, Nifti1Image]],
    lower_cutoff: float = ...,
    upper_cutoff: float = ...,
    connected: bool = ...,
    opening: int = ...,
    threshold: float = ...,
    target_affine: Optional[ndarray] = ...,
    target_shape: Optional[Tuple[int, int, int]] = ...,
    exclude_zeros: bool = ...,
    n_jobs: int = ...,
    memory: None = ...,
    verbose: int = ...
) -> Nifti1Image: ...


def intersect_masks(
    mask_imgs: List[Union[str, Nifti1Image]],
    threshold: float = ...,
    connected: bool = ...
) -> Nifti1Image: ...


def unmask(
    X: Union[List[bool], List[ndarray], ndarray],
    mask_img: Union[str, Nifti1Image],
    order: str = ...
) -> Union[List[Nifti1Image], Nifti1Image]: ...
