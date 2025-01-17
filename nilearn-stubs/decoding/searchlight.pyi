from typing import Any

from nibabel.nifti1 import Nifti1Image
from numpy import (
    memmap,
    ndarray,
)
from sklearn.utils._tags import Tags

class SearchLight:
    def __init__(
        self,
        mask_img: Any,
        process_mask_img: Any | None = ...,
        radius: ndarray | str | float | list[int] | int = ...,
        estimator: ndarray | str | float | list[int] | int = ...,
        n_jobs: int = ...,
        scoring: Any | None = ...,
        cv: Any | None = ...,
        verbose: int = ...,
    ): ...
    def __sklearn_is_fitted__(self) -> bool: ...
    def __sklearn_tags__(self) -> Tags: ...
    def fit(
        self,
        imgs: Nifti1Image | list[Nifti1Image] | ndarray | memmap,
        y: ndarray | memmap | list[int],
        groups: ndarray | None = ...,
    ) -> SearchLight: ...
    @property
    def scores_img_(self): ...
    def transform(self, imgs: Nifti1Image | ndarray) -> ndarray: ...
