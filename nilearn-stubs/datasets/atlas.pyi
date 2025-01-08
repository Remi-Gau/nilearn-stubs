import os
from typing import Literal, TypeAlias

from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from sklearn.utils._bunch import Bunch

FilePath: TypeAlias = str | os.PathLike[str]
NiimgLike: TypeAlias = FilePath | Nifti1Image | Nifti2Image

def fetch_atlas_aal(
    version: Literal["3v2", "SPM12", "SPM5", "SPM8"] = ...,
    data_dir: FilePath | None = ...,
    url: str | None = ...,
    resume: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_atlas_allen_2011(
    data_dir: FilePath | None = ...,
    url: str | None = ...,
    resume: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_atlas_basc_multiscale_2015(
    data_dir: FilePath | None = ...,
    url: str | None = ...,
    resume: bool = ...,
    verbose: int = ...,
    resolution: Literal[7, 12, 20, 36, 64, 122, 197, 325, 444, None] = ...,
    version: Literal["sym", "asym"] = ...,
) -> Bunch: ...
def fetch_atlas_craddock_2012(
    data_dir: FilePath | None = ...,
    url: str | None = ...,
    resume: bool = ...,
    verbose: int = ...,
    homogeneity: Literal["spatial", "temporal", "random", None] = ...,
    grp_mean: bool = ...,
) -> Bunch: ...
def fetch_atlas_destrieux_2009(
    lateralized: bool = ...,
    data_dir: FilePath | None = ...,
    url: str | None = ...,
    resume: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_atlas_difumo(
    dimension: Literal[64, 128, 256, 512, 1024] = ...,
    resolution_mm: int = ...,
    data_dir: FilePath | None = ...,
    resume: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_atlas_harvard_oxford(
    atlas_name: str,
    data_dir: FilePath | None = ...,
    symmetric_split: bool = ...,
    resume: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_atlas_juelich(
    atlas_name: str,
    data_dir: FilePath | None = ...,
    symmetric_split: bool = ...,
    resume: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_atlas_msdl(
    data_dir: FilePath | None = ...,
    url: str | None = ...,
    resume: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_atlas_pauli_2017(
    atlas_type: str = ...,
    data_dir: FilePath | None = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_atlas_schaefer_2018(
    n_rois: Literal[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000] = ...,
    yeo_networks: Literal[7, 17] = ...,
    resolution_mm: Literal[1, 2] = ...,
    data_dir: FilePath | None = ...,
    base_url: str | None = ...,
    resume: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_atlas_smith_2009(
    data_dir: FilePath | None = ...,
    url: str | None = ...,
    resume: bool = ...,
    verbose: int = ...,
    mirror: str = ...,
    dimension: Literal[10, 20, 70, None] = ...,
    resting: bool = ...,
) -> Bunch: ...
def fetch_atlas_surf_destrieux(
    data_dir: FilePath | None = ...,
    url: str | None = ...,
    resume: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_atlas_talairach(
    level_name: str,
    data_dir: FilePath | None = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_atlas_yeo_2011(
    data_dir: FilePath | None = ...,
    url: str | None = ...,
    resume: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_coords_dosenbach_2010(ordered_regions: bool = ...) -> Bunch: ...
def fetch_coords_power_2011() -> Bunch: ...
def fetch_coords_seitzman_2018(ordered_regions: bool = ...) -> Bunch: ...
