from typing import Any

from nibabel.nifti1 import Nifti1Image
from nilearn.surface.surface import SurfaceImage
from numpy import memmap, ndarray
from sklearn.utils._tags import Tags
from sklearn.utils.estimator_checks import _NotAnArray

def recursive_neighbor_agglomeration(
    X: ndarray,
    mask_img: SurfaceImage | Nifti1Image,
    n_clusters: int,
    n_iter: int = ...,
    threshold: float = ...,
    verbose: int = ...,
) -> tuple[int, ndarray]: ...

class ReNA:
    def __init__(
        self,
        mask_img: Any,
        n_clusters: ndarray | float | str | int | list[int] = ...,
        scaling: Any = ...,
        n_iter: ndarray | float | str | int | list[int] = ...,
        threshold: ndarray | str | float | list[int] | int = ...,
        memory: Any | None = ...,
        memory_level: ndarray | float | str | int | list[int] = ...,
        verbose: ndarray | float | str | int | list[int] = ...,
    ): ...
    def __sklearn_tags__(self) -> Tags: ...
    def _more_tags(self) -> Tags: ...
    def fit(
        self,
        X: _NotAnArray | memmap | ndarray,
        y: memmap | _NotAnArray | ndarray | None = ...,
    ) -> ReNA: ...
    def inverse_transform(self, X_red: ndarray) -> ndarray: ...
    def transform(self, X: ndarray, y: None = ...) -> ndarray: ...
