from pathlib import Path
from typing import (
    Any,
)

from joblib.memory import Memory
from numpy import ndarray

class DictLearning:
    def __init__(
        self,
        n_components: ndarray | float | str | int | list[int] = ...,
        n_epochs: ndarray | float | str | int | list[int] = ...,
        alpha: ndarray | float | str | int | list[int] = ...,
        reduction_ratio: ndarray | str | float | list[int] | int = ...,
        dict_init: Any | None = ...,
        random_state: Any | None = ...,
        batch_size: ndarray | float | str | int | list[int] = ...,
        method: ndarray | str | float | list[int] | int = ...,
        mask: Any | None = ...,
        smoothing_fwhm: ndarray | float | str | int | list[int] = ...,
        standardize: Any = ...,
        detrend: Any = ...,
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: Any | None = ...,
        target_affine: ndarray | None = ...,
        target_shape: tuple[int, int, int] | list[int] | None = ...,
        mask_strategy: ndarray | str | float | list[int] | int = ...,
        mask_args: Any | None = ...,
        n_jobs: ndarray | float | str | int | list[int] = ...,
        verbose: int = ...,
        memory: Memory | str | Path | None = ...,
        memory_level: ndarray | float | str | int | list[int] = ...,
    ): ...
