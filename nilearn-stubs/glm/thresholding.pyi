from nibabel.nifti1 import Nifti1Image
from numpy import float64, ndarray

def cluster_level_inference(
    stat_img: Nifti1Image,
    mask_img: Nifti1Image | None = ...,
    threshold: int | list[int] = ...,
    alpha: float | int = ...,
    verbose: int = ...,
) -> Nifti1Image: ...
def fdr_threshold(z_vals: ndarray, alpha: float) -> float64 | float: ...
def threshold_stats_img(
    stat_img: Nifti1Image | None = ...,
    mask_img: Nifti1Image | None = ...,
    alpha: float = ...,
    threshold: int | float = ...,
    height_control: str | None = ...,
    cluster_threshold: int = ...,
    two_sided: bool = ...,
) -> (
    tuple[None, float]
    | tuple[Nifti1Image, float]
    | tuple[None, float64]
    | tuple[Nifti1Image, int]
    | tuple[Nifti1Image, float64]
): ...
