from typing import Any

from numpy import memmap, ndarray
from sklearn.utils._tags import Tags
from sklearn.utils.estimator_checks import _NotAnArray

class HierarchicalKMeans:
    def __init__(
        self,
        n_clusters: ndarray | float | str | int | list[int],
        init: ndarray | str | float | list[int] | int = ...,
        batch_size: ndarray | float | str | int | list[int] = ...,
        n_init: ndarray | float | str | int | list[int] = ...,
        max_no_improvement: ndarray | float | str | int | list[int] = ...,
        verbose: int = ...,
        random_state: ndarray | float | str | int | list[int] = ...,
        scaling: Any = ...,
    ): ...
    def __sklearn_tags__(self) -> Tags: ...
    def fit(
        self,
        X: _NotAnArray | memmap | ndarray,
        y: ndarray | _NotAnArray | memmap | None = ...,
    ) -> HierarchicalKMeans: ...
    def inverse_transform(self, X_red: ndarray) -> ndarray: ...
    def transform(self, X: ndarray, y: None = ...) -> ndarray: ...
