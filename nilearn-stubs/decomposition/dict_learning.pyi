import os
from typing import Any, Literal

from joblib.memory import Memory
from numpy import ndarray, random
from typing_extensions import TypeAlias

MemoryLike: TypeAlias = Memory | str | os.PathLike[str] | None

class DictLearning:
    def __init__(
        self,
        n_components: ndarray | float | str | int | list[int] = ...,
        n_epochs: ndarray | float | str | int | list[int] = ...,
        alpha: ndarray | float | str | int | list[int] = ...,
        reduction_ratio: ndarray | str | float | list[int] | int = ...,
        dict_init: Any | None = ...,
        random_state: int | random.RandomState | None = ...,
        batch_size: ndarray | float | str | int | list[int] = ...,
        method: ndarray | str | float | list[int] | int = ...,
        mask: Any | None = ...,
        smoothing_fwhm: ndarray | float | str | int | list[int] = ...,
        standardize: Any = ...,
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
        n_jobs: int = ...,
        verbose: int = ...,
        memory: MemoryLike = ...,
        memory_level: int = ...,
    ): ...
