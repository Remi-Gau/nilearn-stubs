from nibabel.nifti1 import Nifti1Image
from numpy import ndarray
from pandas.core.frame import DataFrame

from nilearn.surface.surface import SurfaceImage

def _get_indices_from_image(image: Nifti1Image | ndarray | list[int] | SurfaceImage) -> ndarray: ...
def check_look_up_table(
    lut: DataFrame, atlas: Nifti1Image | SurfaceImage, strict: bool = ..., verbose: int = ...
) -> None: ...
def generate_atlas_look_up_table(
    function: str | None = ...,
    name: list[str] | None = ...,
    index: ndarray | SurfaceImage | Nifti1Image | list[int] | None = ...,
    strict: bool = ...,
) -> DataFrame: ...
