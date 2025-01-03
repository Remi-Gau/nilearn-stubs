import os
from typing import Literal

from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from numpy import ndarray
from typing_extensions import TypeAlias

MemoryLike: TypeAlias = Memory | str | os.PathLike[str] | None

FilePath: TypeAlias = str | os.PathLike[str]
NiimgLike: TypeAlias = FilePath | Nifti1Image | Nifti2Image

def connected_label_regions(
    labels_img: NiimgLike,
    min_size: float | None = ...,
    connect_diag: bool = ...,
    labels: list[str] | ndarray | None = ...,
) -> Nifti1Image | tuple[Nifti1Image, list[str]]: ...
def connected_regions(
    maps_img: NiimgLike,
    min_region_size: float = ...,
    extract_type: Literal["local_regions", "connected_components"] = ...,
    smoothing_fwhm: float = ...,
    mask_img: NiimgLike | None = ...,
) -> tuple[Nifti1Image, ndarray]: ...

class RegionExtractor:
    def __init__(
        self,
        maps_img: NiimgLike,
        mask_img: NiimgLike | None = ...,
        min_region_size: float = ...,
        threshold: float | None = ...,
        thresholding_strategy: Literal[
            "ratio_n_voxels", "img_value", "percentile"
        ] = ...,
        two_sided: bool = ...,
        extractor: Literal["local_regions", "connected_components"] = ...,
        str=...,
        smoothing_fwhm: float = ...,
        standardize: bool = ...,
        standardize_confounds: bool = ...,
        detrend: bool = ...,
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: float | None = ...,
        memory: MemoryLike = ...,
        memory_level: int = ...,
        verbose: int = ...,
    ): ...
    def fit(self, X: None = ..., y: None = ...) -> RegionExtractor: ...
