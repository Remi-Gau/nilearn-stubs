from typing import (
    Any,
)

from joblib.memory import (
    MemorizedResult,
    Memory,
)
from nibabel.nifti1 import Nifti1Image
from numpy import (
    memmap,
    ndarray,
)
from sklearn.utils.estimator_checks import _NotAnArray

class MultiNiftiMasker:
    def __init__(
        self,
        mask_img: int | str | Nifti1Image | None = ...,
        smoothing_fwhm: int | None = ...,
        standardize: int | bool | str = ...,
        standardize_confounds: int | bool = ...,
        detrend: int | bool = ...,
        high_variance_confounds: int | bool = ...,
        low_pass: int | None = ...,
        high_pass: int | None = ...,
        t_r: int | None = ...,
        target_affine: int | None = ...,
        target_shape: int | None = ...,
        mask_strategy: int | str = ...,
        mask_args: int | dict[str, int] | None = ...,
        dtype: int | str | None = ...,
        memory: int | Memory | None = ...,
        memory_level: int = ...,
        n_jobs: int = ...,
        verbose: int = ...,
        cmap: int | str = ...,
        **kwargs,
    ): ...
    def fit(
        self,
        imgs: Any | None = ...,
        y: _NotAnArray | memmap | ndarray | None = ...,
    ) -> MultiNiftiMasker: ...
    def transform(
        self,
        imgs: list[Nifti1Image]
        | list[list[Nifti1Image]]
        | ndarray
        | Nifti1Image,
        confounds: None = ...,
        sample_mask: None = ...,
    ) -> MemorizedResult | list[ndarray] | ndarray | list[MemorizedResult]: ...
    def transform_imgs(
        self,
        imgs_list: list[Nifti1Image | list[Nifti1Image]],
        confounds: None = ...,
        sample_mask: None = ...,
        copy: bool = ...,
        n_jobs: int = ...,
    ) -> list[ndarray | MemorizedResult]: ...
