import os
from typing import TypeAlias

from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image

FilePath: TypeAlias = str | os.PathLike[str]
NiimgLike: TypeAlias = FilePath | Nifti1Image | Nifti2Image

def get_data_dirs(data_dir: FilePath | None = ...) -> list[str]: ...
