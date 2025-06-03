from typing import (
    Any,
)

from nilearn._utils.tests.test_class_inspect import A
from nilearn.maskers.multi_nifti_masker import MultiNiftiMasker
from nilearn.maskers.nifti_masker import NiftiMasker
from nilearn.maskers.surface_masker import SurfaceMasker

def get_params(
    cls: type[SurfaceMasker] | type[MultiNiftiMasker] | type[A] | type[NiftiMasker],
    instance: Any,
    ignore: list[str] | None = ...,
) -> dict[str, bool | str | int | None]: ...
