from typing import (
    Any,
)

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
        target_affine: Any | None = ...,
        target_shape: Any | None = ...,
        mask_strategy: ndarray | float | str | int | list[int] = ...,
        mask_args: Any | None = ...,
        memory: Any | None = ...,
        memory_level: ndarray | float | str | int | list[int] = ...,
        n_jobs: ndarray | float | str | int | list[int] = ...,
        verbose: Any = ...,
    ): ...
