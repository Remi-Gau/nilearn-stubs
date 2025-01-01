from nibabel.nifti1 import Nifti1Image
from numpy import float32, int8, int32, int64, ndarray, uint8

def img_to_signals_labels(
    imgs: str | Nifti1Image,
    labels_img: Nifti1Image,
    mask_img: Nifti1Image | None = ...,
    background_label: int = ...,
    order: str = ...,
    strategy: str = ...,
    keep_masked_labels: bool = ...,
    return_masked_atlas: bool = ...,
) -> (
    tuple[ndarray, list[uint8], Nifti1Image]
    | tuple[ndarray, list[float32], Nifti1Image]
    | tuple[ndarray, list[int32]]
    | tuple[ndarray, list[int8], Nifti1Image]
    | tuple[ndarray, list[int32], Nifti1Image]
): ...
def img_to_signals_maps(
    imgs: Nifti1Image,
    maps_img: Nifti1Image,
    mask_img: Nifti1Image | None = ...,
    keep_masked_maps: bool = ...,
) -> tuple[ndarray, list[int64]]: ...
def signals_to_img_labels(
    signals: ndarray | Nifti1Image,
    labels_img: str | Nifti1Image,
    mask_img: str | Nifti1Image | None = ...,
    background_label: int = ...,
    order: str = ...,
) -> Nifti1Image: ...
def signals_to_img_maps(
    region_signals: ndarray,
    maps_img: Nifti1Image,
    mask_img: Nifti1Image | None = ...,
) -> Nifti1Image: ...
