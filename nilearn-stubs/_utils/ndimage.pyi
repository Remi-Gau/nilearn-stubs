from nibabel.nifti1 import Nifti1Image
from numpy import ndarray

def get_border_data(data: ndarray, border_size: int) -> ndarray: ...
def largest_connected_component(volume: str | ndarray | Nifti1Image) -> ndarray: ...
def peak_local_max(
    image: ndarray,
    min_distance: int = ...,
    threshold_abs: int = ...,
    threshold_rel: int | float = ...,
    num_peaks: float = ...,
) -> ndarray: ...
