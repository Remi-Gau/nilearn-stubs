from typing import (
    Any,
)

from nibabel.nifti1 import Nifti1Image

def resolve_globbing(
    path: list[Any | Nifti1Image],
) -> list[Any | Nifti1Image]: ...
