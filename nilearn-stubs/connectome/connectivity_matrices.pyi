from typing import Any, Literal

from numpy import (
    ndarray,
)
from pandas.core.frame import DataFrame

def cov_to_corr(covariance: ndarray) -> ndarray: ...
def prec_to_partial(precision: ndarray) -> ndarray: ...
def sym_matrix_to_vec(symmetric: ndarray, discard_diagonal: bool = ...) -> ndarray: ...
def vec_to_sym_matrix(vec: ndarray | list[ndarray], diagonal: ndarray | None = ...) -> ndarray: ...

class ConnectivityMeasure:
    def __init__(
        self,
        cov_estimator: Any | None = ...,
        kind: Literal[
            "covariance",
            "correlation",
            "partial correlation",
            "tangent",
            "precision",
        ] = ...,
        vectorize: bool = ...,
        discard_diagonal: bool = ...,
        standardize: bool = ...,
    ): ...
    def __sklearn_is_fitted__(self) -> bool: ...
    def fit(self, X: ndarray, y: None = ...) -> ConnectivityMeasure: ...
    def fit_transform(
        self,
        X: list[ndarray],
        y: None = ...,
        confounds: ndarray | DataFrame | None = ...,
    ) -> ndarray: ...
    def inverse_transform(self, connectivities: ndarray, diagonal: ndarray | None = ...) -> ndarray: ...
    def transform(self, X: list[ndarray], confounds: ndarray | None = ...) -> ndarray: ...
