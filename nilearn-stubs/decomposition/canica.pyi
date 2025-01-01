from typing import (
    Any,
)

from numpy import ndarray

class CanICA:
    def __init__(
        self,
        mask: Any | None = ...,
        n_components: Any = ...,
        smoothing_fwhm: ndarray | float | str | int | list[int] = ...,
        do_cca: Any = ...,
        threshold: ndarray | str | float | list[int] | int = ...,
        n_init: ndarray | float | str | int | list[int] = ...,
        random_state: Any | None = ...,
        standardize: Any = ...,
        standardize_confounds: Any = ...,
        detrend: Any = ...,
        low_pass: Any | None = ...,
        high_pass: Any | None = ...,
        t_r: Any | None = ...,
        target_affine: Any | None = ...,
        target_shape: Any | None = ...,
        mask_strategy: ndarray | float | str | int | list[int] = ...,
        mask_args: Any | None = ...,
        memory: Any | None = ...,
        memory_level: ndarray | float | str | int | list[int] = ...,
        n_jobs: ndarray | float | str | int | list[int] = ...,
        verbose: ndarray | float | str | int | list[int] = ...,
    ): ...
    def _raw_fit(self, data: ndarray) -> CanICA: ...
    def _unmix_components(self, components: ndarray): ...
