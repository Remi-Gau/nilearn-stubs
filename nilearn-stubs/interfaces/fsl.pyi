import os
from typing import TypeAlias

from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from pandas.core.frame import DataFrame

FilePath: TypeAlias = str | os.PathLike[str]
NiimgLike: TypeAlias = FilePath | Nifti1Image | Nifti2Image

def get_design_from_fslmat(fsl_design_matrix_path: FilePath, column_names: list[str] | None = ...) -> DataFrame: ...
