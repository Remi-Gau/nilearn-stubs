import os
from pathlib import Path
from typing import Literal, TypeAlias

from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from sklearn.utils._bunch import Bunch

from nilearn.surface.surface import SurfaceImage

FilePath: TypeAlias = str | os.PathLike[str]
NiimgLike: TypeAlias = FilePath | Nifti1Image | Nifti2Image

GM_MNI152_FILE_PATH: Path
MNI152_FILE_PATH: Path
WM_MNI152_FILE_PATH: Path

def fetch_icbm152_2009(
    data_dir: FilePath | None = ...,
    url: str | None = ...,
    resume: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_icbm152_brain_gm_mask(
    data_dir: FilePath | None = ...,
    threshold: float = ...,
    resume: bool = ...,
    n_iter: int = ...,
    verbose: int = ...,
) -> Nifti1Image: ...
def fetch_oasis_vbm(
    n_subjects: None = ...,
    dartel_version: bool = ...,
    data_dir: FilePath | None = ...,
    url: str | None = ...,
    resume: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_surf_fsaverage(mesh: str = ..., data_dir: str | None = ...) -> Bunch: ...
def load_fsaverage(
    mesh: Literal[
        "fsaverage",
        "fsaverage3",
        "fsaverage4",
        "fsaverage5",
        "fsaverage6",
        "fsaverage7",
    ] = ...,
    data_dir: None = ...,
) -> Bunch: ...
def load_fsaverage_data(
    mesh: Literal[
        "fsaverage",
        "fsaverage3",
        "fsaverage4",
        "fsaverage5",
        "fsaverage6",
        "fsaverage7",
    ] = ...,
    mesh_type: Literal["pial", "white_matter", "inflated", "sphere", "flat"] = ...,
    data_type: Literal["curvature", "sulcal", "thickness"] = ...,
    data_dir: FilePath | None = ...,
) -> SurfaceImage: ...
def load_mni152_brain_mask(resolution: int | None = ..., threshold: float = ...) -> Nifti1Image: ...
def load_mni152_gm_mask(resolution: int | None = ..., threshold: float = ..., n_iter: int = ...) -> Nifti1Image: ...
def load_mni152_gm_template(resolution: int | None = ...) -> Nifti1Image: ...
def load_mni152_template(resolution: int | None = ...) -> Nifti1Image: ...
def load_mni152_wm_mask(resolution: int | None = ..., threshold: float = ..., n_iter: int = ...) -> Nifti1Image: ...
def load_mni152_wm_template(resolution: int | None = ...) -> Nifti1Image: ...
