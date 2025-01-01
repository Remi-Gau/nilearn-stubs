from typing import Literal

from numpy import ndarray, random
from sklearn.utils._tags import Tags

class HierarchicalKMeans:
    def __init__(
        self,
        n_clusters: int,
        init: Literal["k-means++", "random"] | ndarray = ...,
        batch_size: int = ...,
        n_init: int = ...,
        max_no_improvement: int = ...,
        verbose: int = ...,
        random_state: int | random.RandomState | None = ...,
        scaling: bool = ...,
    ): ...
    def __sklearn_tags__(self) -> Tags: ...
    def fit(
        self,
        X: ndarray,
        y: None = ...,
    ) -> HierarchicalKMeans: ...
    def inverse_transform(self, X_red: ndarray) -> ndarray: ...
    def transform(self, X: ndarray, y: None = ...) -> ndarray: ...
