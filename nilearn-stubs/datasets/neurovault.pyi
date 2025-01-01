import os
from typing import (
    Callable,
)

from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from numpy import (
    int64,
    ndarray,
)
from sklearn.utils._bunch import Bunch
from typing_extensions import TypeAlias

FilePath: TypeAlias = str | os.PathLike[str]
NiimgLike: TypeAlias = FilePath | Nifti1Image | Nifti2Image

def fetch_neurovault(
    max_images: int = ...,
    collection_terms: None = ...,
    collection_filter: Callable = ...,
    image_terms: None = ...,
    image_filter: Callable = ...,
    mode: str = ...,
    data_dir: FilePath | None = ...,
    fetch_neurosynth_words: bool = ...,
    resample: bool = ...,
    vectorize_words: bool = ...,
    verbose: int = ...,
    **kwarg_image_filters,
) -> Bunch: ...
def fetch_neurovault_ids(
    collection_ids: list[int64] | tuple[()] = ...,
    image_ids: list[int64] | tuple[()] | ndarray = ...,
    mode: str = ...,
    data_dir: FilePath | None = ...,
    fetch_neurosynth_words: bool = ...,
    resample: bool = ...,
    vectorize_words: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_neurovault_auditory_computation_task(
    data_dir: FilePath | None = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_neurovault_motor_task(
    data_dir: FilePath | None = ...,
    verbose: int = ...,
) -> Bunch: ...
