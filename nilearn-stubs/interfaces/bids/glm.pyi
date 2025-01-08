import os
from typing import Literal, TypeAlias

from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from nilearn.glm.first_level.first_level import FirstLevelModel
from nilearn.glm.second_level.second_level import SecondLevelModel
from numpy import ndarray

FilePath: TypeAlias = str | os.PathLike[str]
NiimgLike: TypeAlias = FilePath | Nifti1Image | Nifti2Image

def save_glm_to_bids(
    model: FirstLevelModel | SecondLevelModel,
    contrasts: str
    | ndarray
    | list[str | ndarray]
    | dict[str, str | list | ndarray],
    contrast_types: dict[str, Literal["t", "F"]] | None = ...,
    out_dir: FilePath = ...,
    prefix: str | None = ...,
    **kwargs,
) -> None: ...
