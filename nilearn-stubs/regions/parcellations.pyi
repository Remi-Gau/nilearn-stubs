import os
from pathlib import Path
from typing import Literal

from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from nilearn.surface.surface import SurfaceImage
from numpy import ndarray, random
from typing_extensions import TypeAlias

FilePath: TypeAlias = str | os.PathLike[str]
NiimgLike: TypeAlias = FilePath | Nifti1Image | Nifti2Image

class Parcellations:
    def __init__(
        self,
        method: Literal[
            "kmeans",
            "ward",
            "complete",
            "average",
            "rena",
            "hierarchical_kmeans",
        ],
        n_parcels: int = ...,
        random_state: int | random.mtrand.RandomState | None = ...,
        mask: NiimgLike | SurfaceImage | None = ...,
        smoothing_fwhm: float = ...,
        standardize: bool = ...,
        detrend: bool = ...,
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: float | None = ...,
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
        imgs: list[NiimgLike] | NiimgLike | SurfaceImage | list[SurfaceImage],
        confounds: list[ndarray] | None = ...,
    ) -> list[ndarray] | ndarray: ...
    def inverse_transform(
        self, signals: list[ndarray] | ndarray
    ) -> Nifti1Image | SurfaceImage: ...
    def transform(
        self,
        imgs: list[NiimgLike] | NiimgLike | SurfaceImage | list[SurfaceImage],
        confounds: list[ndarray] | None = ...,
    ) -> list[ndarray] | ndarray: ...
