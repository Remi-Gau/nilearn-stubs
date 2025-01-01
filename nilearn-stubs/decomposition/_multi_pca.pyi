from pathlib import Path
from typing import Any

from joblib.memory import Memory
from numpy import ndarray

class _MultiPCA:
    def __init__(
        self,
        n_components: Any = ...,
        mask: Any | None = ...,
        smoothing_fwhm: Any | None = ...,
        do_cca: Any = ...,
        random_state: Any | None = ...,
        standardize: Any = ...,
        standardize_confounds: Any = ...,
        detrend: Any = ...,
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: Any | None = ...,
        target_affine: ndarray | None = ...,
        target_shape: tuple[int, int, int] | list[int] | None = ...,
        mask_strategy: ndarray | float | str | int | list[int] = ...,
        mask_args: Any | None = ...,
        memory: Memory | str | Path | None = ...,
        memory_level: int = ...,
        n_jobs: ndarray | float | str | int | list[int] = ...,
        verbose: int = ...,
    ): ...
