import os
from typing import TypeAlias

from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from numpy import ndarray
from sklearn.utils._tags import Tags

from nilearn.surface.surface import SurfaceImage

MemoryLike: TypeAlias = Memory | str | os.PathLike[str] | None

FilePath: TypeAlias = str | os.PathLike[str]
NiimgLike: TypeAlias = FilePath | Nifti1Image | Nifti2Image

def recursive_neighbor_agglomeration(
    X: ndarray,
    mask_img: SurfaceImage | NiimgLike,
    n_clusters: int,
    n_iter: int = ...,
    threshold: float = ...,
    verbose: int = ...,
) -> tuple[int, ndarray]: ...

class ReNA:
    def __init__(
        self,
        mask_img: NiimgLike,
        n_clusters: int = ...,
        scaling: bool = ...,
        n_iter: int = ...,
        threshold: float = ...,
        memory: MemoryLike = ...,
        memory_level: int = ...,
        verbose: int = ...,
    ): ...
    def __sklearn_tags__(self) -> Tags: ...
    def fit(
        self,
        X: ndarray,
        y: None = ...,
    ) -> ReNA: ...
    def inverse_transform(self, X_red: ndarray) -> ndarray: ...
    def transform(self, X: ndarray, y: None = ...) -> ndarray: ...
