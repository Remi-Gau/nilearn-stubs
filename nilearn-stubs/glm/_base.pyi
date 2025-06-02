import os
from typing import Literal, TypeAlias

from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from numpy import ndarray

from nilearn.reporting.html_report import HTMLReport

FilePath: TypeAlias = str | os.PathLike[str]
NiimgLike: TypeAlias = FilePath | Nifti1Image | Nifti2Image

class BaseGLM:
    def generate_report(
        self,
        contrasts: dict[str, ndarray] | str | list[str] | ndarray,
        title: str | None = ...,
        bg_img: NiimgLike | Literal["MNI152TEMPLATE"] | None = ...,
        threshold: float = ...,
        alpha: float = ...,
        cluster_threshold: int = ...,
        height_control: Literal["fpr", "fdr", "bonferroni", None] = ...,
        min_distance: float = ...,
        plot_type: Literal["slice", "glass"] = ...,
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
