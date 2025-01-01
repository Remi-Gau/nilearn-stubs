from pathlib import Path
from typing import Any

from joblib.memory import Memory
from numpy import ndarray, random

class CanICA:
    def __init__(
        self,
        mask: Any | None = ...,
        n_components: Any = ...,
        smoothing_fwhm: ndarray | float | str | int | list[int] = ...,
        do_cca: Any = ...,
        threshold: ndarray | str | float | list[int] | int = ...,
        n_init: ndarray | float | str | int | list[int] = ...,
        random_state: int | random.mtrand.RandomState | None = ...,
        standardize: Any = ...,
        standardize_confounds: Any = ...,
        detrend: Any = ...,
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: float | None = ...,
        target_affine: ndarray | None = ...,
        target_shape: tuple[int, int, int] | list[int] | None = ...,
        mask_strategy: ndarray | float | str | int | list[int] = ...,
        mask_args: Any | None = ...,
        memory: Memory | str | Path | None = ...,
        memory_level: int = ...,
        n_jobs: int = ...,
        verbose: int = ...,
    ): ...
