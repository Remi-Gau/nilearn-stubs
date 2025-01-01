from typing import Literal

from nilearn.maskers import MultiNiftiMasker, NiftiMasker
from numpy import (
    ndarray,
    random,
)

def permuted_ols(
    tested_vars: ndarray,
    target_vars: ndarray,
    confounding_vars: ndarray | None = ...,
    model_intercept: bool = ...,
    n_perm: float = ...,
    two_sided_test: bool = ...,
    random_state: int | random.RandomState | None = ...,
    n_jobs: int = ...,
    verbose: int = ...,
    masker: NiftiMasker | MultiNiftiMasker | None = ...,
    tfce: bool = ...,
    threshold: float | None = ...,
    output_type: Literal["legacy", "dict"] = ...,
) -> tuple[ndarray, ndarray, ndarray] | dict[str, ndarray]: ...
