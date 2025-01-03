"""Nilearn types."""

import os

from joblib.memory import Memory
from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from typing_extensions import TypeAlias

MemoryLike: TypeAlias = Memory | str | os.PathLike[str] | None
NiimgLike: TypeAlias = str | os.PathLike[str] | Nifti1Image | Nifti2Image
