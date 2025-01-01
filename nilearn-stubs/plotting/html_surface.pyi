from pathlib import PosixPath

from matplotlib.colors import LinearSegmentedColormap
from nibabel.nifti1 import Nifti1Image
from nilearn.plotting.html_document import HTMLDocument
from nilearn.surface.surface import InMemoryMesh
from numpy import ndarray
from sklearn.utils._bunch import Bunch

class SurfaceView(HTMLDocument):
    pass

def view_img_on_surf(
    stat_map_img: PosixPath | list[Nifti1Image] | Nifti1Image | str,
    surf_mesh: Bunch | str = ...,
    threshold: float | int | str | None = ...,
    cmap: LinearSegmentedColormap | str = ...,
    black_bg: bool = ...,
    vmax: None = ...,
    vmin: None = ...,
    symmetric_cmap: bool = ...,
    bg_on_data: bool = ...,
    darkness: float = ...,
    colorbar: bool = ...,
    colorbar_height: float = ...,
    colorbar_fontsize: int = ...,
    title: str | None = ...,
    title_fontsize: int = ...,
    vol_to_surf_kwargs: dict[str, int | float | str] | None = ...,
) -> SurfaceView: ...
def view_surf(
    surf_mesh: InMemoryMesh | str | None = ...,
    surf_map: str | ndarray | None = ...,
    bg_map: ndarray | str | None = ...,
    hemi: float | str | None = ...,
    threshold: None = ...,
    cmap: LinearSegmentedColormap | str = ...,
    black_bg: bool = ...,
    vmax: None = ...,
    vmin: None = ...,
    bg_on_data: bool = ...,
    darkness: float = ...,
    symmetric_cmap: bool = ...,
    colorbar: bool = ...,
    colorbar_height: float = ...,
    colorbar_fontsize: int = ...,
    title: str | None = ...,
    title_fontsize: int = ...,
) -> SurfaceView: ...
