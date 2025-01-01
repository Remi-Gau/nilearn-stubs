from pathlib import Path

from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from nilearn.surface.surface import SurfaceImage
from numpy import ndarray

class Parcellations:
    def __init__(
        self,
        method: str | None,
        n_parcels: int = ...,
        random_state: int = ...,
        mask: Nifti1Image | SurfaceImage | None = ...,
        smoothing_fwhm: float = ...,
        standardize: bool = ...,
        detrend: bool = ...,
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: None = ...,
        target_affine: ndarray | None = ...,
        target_shape: tuple[int, int, int] | list[int] | None = ...,
        mask_strategy: str = ...,
        mask_args: None = ...,
        scaling: bool = ...,
        n_iter: int = ...,
        memory: Memory | str | Path | None = ...,
        memory_level: int = ...,
        n_jobs: int = ...,
        verbose: int = ...,
    ): ...
    def fit_transform(
        self,
        imgs: list[Nifti1Image]
        | Nifti1Image
        | SurfaceImage
        | list[SurfaceImage],
        confounds: list[ndarray] | None = ...,
    ) -> list[ndarray] | ndarray: ...
    def inverse_transform(
        self, signals: list[ndarray] | ndarray
    ) -> list[Nifti1Image] | Nifti1Image | SurfaceImage: ...
    def transform(
        self,
        imgs: list[Nifti1Image]
        | Nifti1Image
        | SurfaceImage
        | list[SurfaceImage],
        confounds: list[ndarray] | None = ...,
    ) -> list[ndarray] | ndarray: ...
