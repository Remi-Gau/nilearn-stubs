from nibabel.nifti1 import Nifti1Image
from nilearn.plotting.img_plotting import _MNI152Template
from numpy import float32, float64, ndarray

def find_cut_slices(
    img: Nifti1Image | _MNI152Template,
    direction: str = ...,
    n_cuts: float | int = ...,
    spacing: int | str = ...,
) -> ndarray: ...
def find_parcellation_cut_coords(
    labels_img: Nifti1Image,
    background_label: int = ...,
    return_label_names: bool = ...,
    label_hemisphere: str = ...,
) -> tuple[ndarray, list[float64]] | ndarray: ...
def find_probabilistic_atlas_cut_coords(maps_img: Nifti1Image) -> ndarray: ...
def find_xyz_cut_coords(
    img: Nifti1Image | _MNI152Template,
    mask_img: Nifti1Image | None = ...,
    activation_threshold: int | float | float32 | None = ...,
) -> list[float]: ...
