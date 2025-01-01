from pathlib import PosixPath
from typing import (
    Callable,
)

from numpy import (
    int64,
    ndarray,
)
from sklearn.utils._bunch import Bunch

def fetch_neurovault(
    max_images: int = ...,
    collection_terms: None = ...,
    collection_filter: Callable = ...,
    image_terms: None = ...,
    image_filter: Callable = ...,
    mode: str = ...,
    data_dir: PosixPath | None = ...,
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
    data_dir: PosixPath | None = ...,
    fetch_neurosynth_words: bool = ...,
    resample: bool = ...,
    vectorize_words: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
