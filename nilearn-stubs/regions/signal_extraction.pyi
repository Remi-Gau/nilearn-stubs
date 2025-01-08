import os
from typing import Literal, TypeAlias

from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from numpy import ndarray

FilePath: TypeAlias = str | os.PathLike[str]
NiimgLike: TypeAlias = FilePath | Nifti1Image | Nifti2Image

def img_to_signals_labels(
    imgs: NiimgLike,
    labels_img: NiimgLike,
    mask_img: NiimgLike | None = ...,
    background_label: float = ...,
    order: Literal["C", "F"] = ...,
    strategy: Literal[
        "sum",
        "mean",
        "median",
        "minimum",
        "maximum",
        "variance",
        "standard_deviation",
    ] = ...,
    keep_masked_labels: bool = ...,
    return_masked_atlas: bool = ...,
) -> tuple[ndarray, list[float] | tuple[float], Nifti1Image]: ...
def img_to_signals_maps(
    imgs: NiimgLike,
    maps_img: NiimgLike,
    mask_img: NiimgLike | None = ...,
    keep_masked_maps: bool = ...,
) -> tuple[ndarray, list[float]]: ...
def signals_to_img_labels(
    signals: ndarray,
    labels_img: NiimgLike,
    mask_img: NiimgLike | None = ...,
    background_label: int = ...,
    order: Literal["C", "F"] = ...,
) -> Nifti1Image: ...
def signals_to_img_maps(
    region_signals: ndarray,
    maps_img: NiimgLike,
    mask_img: NiimgLike | None = ...,
) -> Nifti1Image: ...
