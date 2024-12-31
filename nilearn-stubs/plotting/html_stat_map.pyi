from nibabel.nifti1 import Nifti1Image
from nilearn.plotting.html_document import HTMLDocument

class StatMapView(HTMLDocument):
    pass

def view_img(
    stat_map_img: Nifti1Image,
    bg_img: Nifti1Image | str | None = ...,
    cut_coords: None = ...,
    colorbar: bool = ...,
    title: str | None = ...,
    threshold: float | str = ...,
    annotate: bool = ...,
    draw_cross: bool = ...,
    black_bg: str = ...,
    cmap: str = ...,
    symmetric_cmap: bool = ...,
    dim: str = ...,
    vmax: float | None = ...,
    vmin: None = ...,
    resampling_interpolation: str = ...,
    width_view: int = ...,
    opacity: int = ...,
) -> StatMapView: ...
