from nilearn.maskers.nifti_masker import NiftiMasker
from numpy import (
    ndarray,
)

def permuted_ols(
    tested_vars: ndarray,
    target_vars: ndarray,
    confounding_vars: ndarray | None = ...,
    model_intercept: bool = ...,
    n_perm: int | float = ...,
    two_sided_test: bool = ...,
    random_state: int | None = ...,
    n_jobs: int = ...,
    verbose: int = ...,
    masker: NiftiMasker | None = ...,
    tfce: bool = ...,
    threshold: float | None = ...,
    output_type: str = ...,
) -> dict[str, ndarray] | tuple[ndarray, ndarray, ndarray]: ...
