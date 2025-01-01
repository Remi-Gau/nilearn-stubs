from nibabel.nifti1 import Nifti1Image
from numpy import ndarray, str_

def connected_label_regions(
    labels_img: Nifti1Image,
    min_size: int | str | None = ...,
    connect_diag: bool | None = ...,
    labels: str | list[str] | ndarray | None = ...,
) -> (
    Nifti1Image
    | tuple[Nifti1Image, list[str]]
    | tuple[Nifti1Image, list[str_]]
): ...
def connected_regions(
    maps_img: Nifti1Image,
    min_region_size: int | float = ...,
    extract_type: int | str = ...,
    smoothing_fwhm: int | float = ...,
    mask_img: Nifti1Image | None = ...,
) -> tuple[Nifti1Image, list[int]]: ...

class RegionExtractor:
    def __init__(
        self,
        maps_img: Nifti1Image,
        mask_img: Nifti1Image | None = ...,
        min_region_size: int | float = ...,
        threshold: float | int | str | None = ...,
        thresholding_strategy: str = ...,
        two_sided: bool = ...,
        extractor: str = ...,
        smoothing_fwhm: int | float = ...,
        standardize: bool = ...,
        standardize_confounds: bool = ...,
        detrend: bool = ...,
        low_pass: None = ...,
        high_pass: None = ...,
        t_r: None = ...,
        memory: None = ...,
        memory_level: int = ...,
        verbose: int = ...,
    ): ...
    def fit(self, X: None = ..., y: None = ...) -> RegionExtractor: ...
