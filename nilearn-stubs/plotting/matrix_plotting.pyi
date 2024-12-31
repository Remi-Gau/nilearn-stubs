from pathlib import PosixPath

from matplotlib.axes._axes import Axes
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.figure import Figure
from matplotlib.image import AxesImage
from numpy import ndarray
from pandas.core.frame import DataFrame

def plot_contrast_matrix(
    contrast_def: str | ndarray,
    design_matrix: DataFrame,
    colorbar: bool = ...,
    axes: Axes | None = ...,
    output_file: PosixPath | None = ...,
) -> Axes | None: ...
def plot_design_matrix(
    design_matrix: DataFrame | PosixPath | str,
    rescale: bool = ...,
    axes: None = ...,
    output_file: PosixPath | None = ...,
) -> Axes | None: ...
def plot_design_matrix_correlation(
    design_matrix: DataFrame | PosixPath | str,
    tri: str = ...,
    cmap: LinearSegmentedColormap | str = ...,
    output_file: PosixPath | None = ...,
    **kwargs,
) -> AxesImage: ...
def plot_event(
    model_event: list[PosixPath | str]
    | DataFrame
    | PosixPath
    | list[DataFrame],
    cmap: str | None = ...,
    output_file: PosixPath | None = ...,
    **fig_kwargs,
) -> Figure | None: ...
def plot_matrix(
    mat: ndarray,
    title: str | None = ...,
    labels: list[str] | ndarray | list[int] | None = ...,
    figure: None = ...,
    axes: None = ...,
    colorbar: bool = ...,
    cmap: LinearSegmentedColormap | str = ...,
    tri: str = ...,
    auto_fit: bool = ...,
    grid: bool = ...,
    reorder: str | bool = ...,
    **kwargs,
) -> AxesImage: ...
