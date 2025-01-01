# TODO
import os

from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from sklearn.utils._bunch import Bunch
from typing_extensions import TypeAlias

FilePath: TypeAlias = str | os.PathLike[str]
NiimgLike: TypeAlias = FilePath | Nifti1Image | Nifti2Image

def fetch_atlas_aal(
    version: str = ...,
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
    resolution: int | None = ...,
    version: str = ...,
) -> Bunch: ...
def fetch_atlas_craddock_2012(
    data_dir: FilePath | None = ...,
    url: str | None = ...,
    resume: bool = ...,
    verbose: int = ...,
    homogeneity: str | None = ...,
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
    dimension: int = ...,
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
    n_rois: int = ...,
    yeo_networks: int = ...,
    resolution_mm: int = ...,
    data_dir: FilePath | None = ...,
    base_url: None = ...,
    resume: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_atlas_smith_2009(
    data_dir: FilePath | None = ...,
    url: str | None = ...,
    resume: bool = ...,
    verbose: int = ...,
    mirror: str = ...,
    dimension: int | None = ...,
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
