from typing import (
    Any,
)

from joblib.memory import (
    MemorizedResult,
)
from nibabel.nifti1 import Nifti1Image
from numpy import (
    memmap,
    ndarray,
)
from pandas.core.frame import DataFrame
from sklearn.utils._tags import Tags
from sklearn.utils.estimator_checks import _NotAnArray

class BaseMasker:
    def __sklearn_tags__(self) -> Tags: ...
    def _check_fitted(self): ...
    def _more_tags(self) -> Tags: ...
    def fit(
        self,
        imgs: memmap | _NotAnArray | ndarray | None = ...,
        y: memmap | _NotAnArray | ndarray | None = ...,
    ): ...
    def fit_transform(
        self,
        X: memmap | _NotAnArray | Nifti1Image | ndarray | list[Nifti1Image],
        y: memmap | _NotAnArray | ndarray | None = ...,
        confounds: DataFrame | None = ...,
        sample_mask: ndarray | None = ...,
        **fit_params,
    ) -> MemorizedResult | list[ndarray] | ndarray | list[MemorizedResult]: ...
    def inverse_transform(self, X: memmap | ndarray) -> Nifti1Image: ...
    def transform(
        self,
        imgs: Any,
        confounds: ndarray | list[ndarray] | DataFrame | None = ...,
        sample_mask: ndarray | None = ...,
    ) -> memmap | ndarray: ...

class _BaseSurfaceMasker:
    def __sklearn_tags__(self) -> Tags: ...
    def _more_tags(self) -> Tags: ...
