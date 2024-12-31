from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from numpy import ndarray

class MultiNiftiMapsMasker:
    def __init__(
        self,
        maps_img: int | str | Nifti1Image,
        mask_img: int | str | Nifti1Image | None = ...,
        allow_overlap: int | bool = ...,
        smoothing_fwhm: int | None = ...,
        standardize: int | bool = ...,
        standardize_confounds: int | bool = ...,
        high_variance_confounds: int | bool = ...,
        detrend: int | bool = ...,
        low_pass: int | None = ...,
        high_pass: int | None = ...,
        t_r: int | None = ...,
        dtype: int | None = ...,
        resampling_target: int | str | None = ...,
        memory: int | Memory | None = ...,
        memory_level: int = ...,
        verbose: int = ...,
        reports: int | bool = ...,
        n_jobs: int = ...,
        **kwargs,
    ): ...
    def transform(
        self,
        imgs: list[Nifti1Image] | ndarray | Nifti1Image,
        confounds: None = ...,
        sample_mask: list[ndarray] | None = ...,
    ) -> list[ndarray] | ndarray: ...
    def transform_imgs(
        self,
        imgs_list: list[Nifti1Image],
        confounds: None = ...,
        n_jobs: int = ...,
        sample_mask: list[ndarray] | None = ...,
    ) -> list[ndarray]: ...