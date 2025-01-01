from pathlib import PosixPath

from nilearn.glm.first_level.first_level import FirstLevelModel
from nilearn.glm.second_level.second_level import SecondLevelModel
from numpy import ndarray

def save_glm_to_bids(
    model: FirstLevelModel | SecondLevelModel,
    contrasts: (
        dict[str, int]
        | list[str]
        | dict[int, ndarray]
        | str
        | dict[str, ndarray]
    ),
    contrast_types: dict[int, str] | dict[str, str] | None = ...,
    out_dir: PosixPath = ...,
    prefix: int | str | None = ...,
    **kwargs,
) -> None: ...
