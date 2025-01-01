from typing import Any

from numpy import ndarray
from pandas.core.frame import DataFrame

def load_confounds(
    img_files: list[str] | list[list[str]] | str,
    strategy: Any = ...,
    motion: str = ...,
    scrub: int = ...,
    fd_threshold: float = ...,
    std_dvars_threshold: int = ...,
    wm_csf: str = ...,
    global_signal: str = ...,
    compcor: str = ...,
    n_compcor: int | str = ...,
    ica_aroma: str = ...,
    demean: bool = ...,
) -> (
    tuple[list[DataFrame], list[ndarray]]
    | tuple[DataFrame, ndarray]
    | tuple[DataFrame, None]
    | tuple[None, ndarray]
): ...
