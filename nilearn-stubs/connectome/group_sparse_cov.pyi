import os
from typing import Callable

from joblib.memory import Memory
from numpy import ndarray
from typing_extensions import TypeAlias

MemoryLike: TypeAlias = Memory | str | os.PathLike[str] | None

def group_sparse_covariance(
    subjects: list[ndarray],
    alpha: float,
    max_iter: int = ...,
    tol: float | None = ...,
    verbose: int = ...,
    probe_function: Callable | None = ...,
    precisions_init: ndarray | None = ...,
    debug: bool = ...,
) -> tuple[ndarray, ndarray]: ...

class GroupSparseCovariance:
    def __init__(
        self,
        alpha: float = ...,
        tol: float = ...,
        max_iter: int = ...,
        verbose: int = ...,
        memory: MemoryLike = ...,
        memory_level: int = ...,
    ): ...
    def fit(
        self, subjects: list[ndarray], y: None = ...
    ) -> GroupSparseCovariance: ...

class GroupSparseCovarianceCV:
    def __init__(
        self,
        alphas: int = ...,
        n_refinements: int = ...,
        cv: int | None = ...,
        tol_cv: float = ...,
        max_iter_cv: int = ...,
        tol: float = ...,
        max_iter: int = ...,
        verbose: int = ...,
        n_jobs: int = ...,
        debug: bool = ...,
        early_stopping: bool = ...,
    ): ...
    def fit(
        self, subjects: list[ndarray], y: None = ...
    ) -> GroupSparseCovarianceCV: ...
