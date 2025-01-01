from pathlib import Path
from typing import Any

from joblib.memory import Memory
from numpy import (
    memmap,
    ndarray,
)

def group_sparse_covariance(
    subjects: int | list[ndarray],
    alpha: float | str,
    max_iter: int = ...,
    tol: float = ...,
    verbose: int = ...,
    probe_function: None = ...,
    precisions_init: None = ...,
    debug: bool = ...,
) -> tuple[ndarray, ndarray]: ...

class GroupSparseCovariance:
    def __init__(
        self,
        alpha: Any = ...,
        tol: ndarray | str | float | list[int] | int = ...,
        max_iter: ndarray | float | str | int | list[int] = ...,
        verbose: int = ...,
        memory: Memory | str | Path | None = ...,
        memory_level: ndarray | float | str | int | list[int] = ...,
    ): ...
    def fit(
        self, subjects: Any, y: ndarray | memmap | None = ...
    ) -> GroupSparseCovariance: ...

class GroupSparseCovarianceCV:
    def __init__(
        self,
        alphas: ndarray | float | str | int | list[int] = ...,
        n_refinements: ndarray | float | str | int | list[int] = ...,
        cv: Any | None = ...,
        tol_cv: ndarray | str | float | list[int] | int = ...,
        max_iter_cv: ndarray | float | str | int | list[int] = ...,
        tol: ndarray | str | float | list[int] | int = ...,
        max_iter: ndarray | float | str | int | list[int] = ...,
        verbose: int = ...,
        n_jobs: ndarray | float | str | int | list[int] = ...,
        debug: Any = ...,
        early_stopping: Any = ...,
    ): ...
    def fit(
        self, subjects: Any, y: memmap | ndarray | None = ...
    ) -> GroupSparseCovarianceCV: ...
