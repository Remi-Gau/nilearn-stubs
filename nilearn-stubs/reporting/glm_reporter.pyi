import os
from typing import Literal, TypeAlias

from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from numpy import ndarray

from nilearn.glm.first_level.first_level import FirstLevelModel
from nilearn.glm.second_level.second_level import SecondLevelModel
from nilearn.reporting.html_report import HTMLReport

NiimgLike: TypeAlias = str | os.PathLike[str] | Nifti1Image | Nifti2Image

def make_glm_report(
    model: FirstLevelModel | SecondLevelModel,
    contrasts: dict[str, str] | dict[str, ndarray] | ndarray | str | list[ndarray],
    title: str | None = ...,
    bg_img: NiimgLike | Literal["MNI152TEMPLATE"] = ...,
    threshold: float = ...,
    alpha: float = ...,
    cluster_threshold: int = ...,
    height_control: Literal["fpr", "fdr", "bonferroni", None] = ...,
    two_sided: bool = ...,
    min_distance: float = ...,
    plot_type: Literal["slice", "glass"] = ...,
    cut_coords: tuple[float, ...] = ...,
    display_mode: Literal[
        "ortho",
        "x",
        "y",
        "z",
        "xz",
        "yx",
        "yz",
        "l",
        "r",
        "lr",
        "lzr",
        "lyr",
        "lzry",
        "lyrz",
        None,
    ] = ...,
    report_dims: tuple[int, int] = ...,
) -> HTMLReport: ...
