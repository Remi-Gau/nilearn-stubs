import os
from collections.abc import Container
from typing import Callable, Literal, TypeAlias

from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from sklearn.utils._bunch import Bunch

FilePath: TypeAlias = str | os.PathLike[str]
NiimgLike: TypeAlias = FilePath | Nifti1Image | Nifti2Image

def fetch_neurovault(
    max_images: int = ...,
    collection_terms: None = ...,
    collection_filter: Callable = ...,
    image_terms: dict | None = ...,
    image_filter: Callable = ...,
    mode: Literal["download_new", "overwrite", "offline"] = ...,
    data_dir: FilePath | None = ...,
    fetch_neurosynth_words: bool = ...,
    resample: bool = ...,
    vectorize_words: bool = ...,
    verbose: int = ...,
    **kwarg_image_filters,
) -> Bunch: ...
def fetch_neurovault_ids(
    collection_ids: Container[int] = ...,
    image_ids: Container[int] = ...,
    mode: Literal["download_new", "overwrite", "offline"] = ...,
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
