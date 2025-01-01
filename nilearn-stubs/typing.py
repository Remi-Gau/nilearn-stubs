"""Nilearn types."""

import os

from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from typing_extensions import TypeAlias

NiimgLike: TypeAlias = str | os.PathLike[str] | Nifti1Image | Nifti2Image
