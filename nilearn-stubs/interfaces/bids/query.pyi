import os
from pathlib import PosixPath
from typing import TypeAlias

from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image

FilePath: TypeAlias = str | os.PathLike[str]
NiimgLike: TypeAlias = FilePath | Nifti1Image | Nifti2Image

def get_bids_files(
    main_path: FilePath,
    file_tag: str = ...,
    file_type: str = ...,
    sub_label: str = ...,
    modality_folder: str = ...,
    filters: list[tuple[str, str]] | None = ...,
    sub_folder: bool = ...,
) -> list[str]: ...
def parse_bids_filename(
    img_path: PosixPath | str,
) -> dict[str, PosixPath | str | list[str]]: ...
