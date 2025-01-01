from typing import Literal

from numpy import ndarray
from pandas.core.frame import DataFrame

def load_confounds_strategy(
    img_files: str | list[str],
    denoise_strategy: Literal[
        "simple", "scrubbing", "compcor", "ica_aroma"
    ] = ...,
    **kwargs,
) -> tuple[
    DataFrame | list[DataFrame], None | ndarray | list[ndarray, None]
]: ...
