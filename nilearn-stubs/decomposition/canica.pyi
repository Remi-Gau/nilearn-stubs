import os
from typing import Any, Literal

from joblib.memory import Memory
from numpy import ndarray, random
from typing_extensions import TypeAlias

MemoryLike: TypeAlias = Memory | str | os.PathLike[str] | None

class CanICA:
    def __init__(
        self,
        mask: Any | None = ...,
        n_components: Any = ...,
        smoothing_fwhm: ndarray | float | str | int | list[int] = ...,
        do_cca: Any = ...,
        threshold: ndarray | str | float | list[int] | int = ...,
        n_init: ndarray | float | str | int | list[int] = ...,
        random_state: int | random.RandomState | None = ...,
        standardize: Any = ...,
        standardize_confounds: Any = ...,
        detrend: Any = ...,
        low_pass: float | None = ...,
        high_pass: float | None = ...,
        t_r: float | None = ...,
        target_affine: ndarray | None = ...,
        target_shape: tuple[int, int, int] | list[int] | None = ...,
        mask_strategy: Literal[
            "background",
            "epi",
            "whole-brain-template",
            "gm-template",
            "wm-template",
        ] = ...,
        mask_args: Any | None = ...,
        memory: MemoryLike = ...,
        memory_level: int = ...,
        n_jobs: int = ...,
        verbose: int = ...,
    ): ...
