from pathlib import PosixPath
from typing import (
    Any,
    Callable,
)

from matplotlib.axes._axes import Axes
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.axes3d import Axes3D
from nibabel.nifti1 import Nifti1Image
from nilearn.plotting.displays._figures import PlotlySurfaceFigure
from nilearn.surface.surface import (
    InMemoryMesh,
    PolyMesh,
)
from numpy import (
    float32,
    float64,
    ndarray,
)
from sklearn.utils._bunch import Bunch

def plot_img_on_surf(
    stat_map: Nifti1Image | PosixPath | str,
    surf_mesh: Bunch | str = ...,
    mask_img: None = ...,
    hemispheres: list[str] | None = ...,
    bg_on_data: bool = ...,
    inflate: bool = ...,
    views: list[str | dict[str, str]]
    | list[str]
    | list[tuple[float, float]]
    | int
    | None = ...,
    output_file: str | None = ...,
    title: str | None = ...,
    colorbar: bool = ...,
    vmin: int | None = ...,
    vmax: int | None = ...,
    threshold: int | None = ...,
    symmetric_cbar: bool | str = ...,
    cmap: str = ...,
    cbar_tick_format: str = ...,
    **kwargs,
) -> tuple[Figure, list[Axes3D]] | tuple[Figure, list[Axes3D | Axes]]: ...
def plot_surf(
    surf_mesh: str | InMemoryMesh | PolyMesh | None = ...,
    surf_map: Any | None = ...,
    bg_map: str | ndarray | None = ...,
    hemi: str = ...,
    view: tuple[float, float] | str | None = ...,
    engine: str = ...,
    cmap: str | None = ...,
    symmetric_cmap: bool | None = ...,
    colorbar: bool = ...,
    avg_method: str | Callable | None = ...,
    threshold: float | int | None = ...,
    alpha: float | int | str | None = ...,
    bg_on_data: bool = ...,
    darkness: float | None = ...,
    vmin: Any | None = ...,
    vmax: Any | None = ...,
    cbar_vmin: int | float32 | float64 | None = ...,
    cbar_vmax: int | float32 | float64 | None = ...,
    cbar_tick_format: str = ...,
    title: str | None = ...,
    title_font_size: int = ...,
    output_file: str | PosixPath | None = ...,
    axes: Axes3D | None = ...,
    figure: Figure | None = ...,
) -> Figure | PlotlySurfaceFigure | None: ...
def plot_surf_contours(
    surf_mesh: InMemoryMesh | None = ...,
    roi_map: Any | None = ...,
    hemi: str | None = ...,
    axes: Axes | Axes3D | PlotlySurfaceFigure | None = ...,
    figure: Figure | PlotlySurfaceFigure | None = ...,
    levels: list[int] | None = ...,
    labels: list[str] | None = ...,
    colors: list[list[int]]
    | list[str]
    | str
    | list[list[int] | int]
    | None = ...,
    legend: bool = ...,
    cmap: str = ...,
    title: str | None = ...,
    output_file: str | None = ...,
    **kwargs,
) -> Figure: ...
def plot_surf_roi(
    surf_mesh: InMemoryMesh | PolyMesh | None = ...,
    roi_map: Any | None = ...,
    bg_map: None = ...,
    hemi: str = ...,
    view: None = ...,
    engine: str = ...,
    avg_method: str | None = ...,
    threshold: float | int = ...,
    alpha: None = ...,
    vmin: int | float | None = ...,
    vmax: float | None = ...,
    cmap: str = ...,
    cbar_tick_format: str = ...,
    bg_on_data: bool = ...,
    darkness: float | None = ...,
    title: None = ...,
    title_font_size: int = ...,
    output_file: str | None = ...,
    axes: Axes3D | None = ...,
    figure: Figure | None = ...,
    **kwargs,
) -> Figure | PlotlySurfaceFigure | None: ...
def plot_surf_stat_map(
    surf_mesh: str | InMemoryMesh | None = ...,
    stat_map: Any | None = ...,
    bg_map: str | ndarray | None = ...,
    hemi: str = ...,
    view: str | tuple[float, float] | None = ...,
    engine: str = ...,
    threshold: float | int | None = ...,
    alpha: int | float | None = ...,
    vmin: int | float32 | None = ...,
    vmax: int | float32 | None = ...,
    cmap: str = ...,
    colorbar: bool = ...,
    symmetric_cbar: bool | str = ...,
    cbar_tick_format: str = ...,
    bg_on_data: bool = ...,
    darkness: float = ...,
    title: str | None = ...,
    title_font_size: int = ...,
    output_file: None = ...,
    axes: Axes3D | None = ...,
    figure: None = ...,
    avg_method: None = ...,
    **kwargs,
) -> Figure | PlotlySurfaceFigure: ...
