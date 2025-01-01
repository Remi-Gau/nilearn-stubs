"""Nilearn types."""

import os

from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image

NiimgLike = str | os.PathLike | Nifti1Image | Nifti2Image
