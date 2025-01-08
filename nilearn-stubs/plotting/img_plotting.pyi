from io import BufferedWriter
from pathlib import PosixPath
from typing import Any, Literal, TypeAlias

from matplotlib.axes._axes import Axes
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
from matplotlib.figure import Figure
from nibabel.nifti1 import Nifti1Image
from nilearn.maskers.nifti_masker import NiftiMasker
from nilearn.plotting.displays._projectors import (
    LYRZProjector,
    OrthoProjector,
    XProjector,
)
from nilearn.plotting.displays._slicers import (
    MosaicSlicer,
    OrthoSlicer,
    TiledSlicer,
    XSlicer,
    ZSlicer,
)
from numpy import float64, int64, ndarray
from numpy.ma.core import MaskedArray
from scipy.sparse._coo import coo_matrix

DisplayMode: TypeAlias = Literal[
    "ortho", "tiled", "mosaic", "x", "y", "z", "yx", "xz", "yz"
]

def plot_anat(
    anat_img: Nifti1Image | _MNI152Template | bool = ...,
    cut_coords: int | tuple[int, int] | tuple[int, int, int] | None = ...,
    output_file: PosixPath | None = ...,
    display_mode: DisplayMode = ...,
    figure: None = ...,
    axes: None = ...,
    title: str | None = ...,
    annotate: bool = ...,
    threshold: None = ...,
    draw_cross: bool = ...,
    black_bg: str = ...,
    dim: str = ...,
    cmap: LinearSegmentedColormap = ...,
    colorbar: bool = ...,
    cbar_tick_format: str = ...,
    radiological: bool = ...,
    vmin: None = ...,
    vmax: None = ...,
    **kwargs,
) -> MosaicSlicer | ZSlicer | OrthoSlicer | TiledSlicer | None: ...
def plot_carpet(
    img: Nifti1Image,
    mask_img: Nifti1Image | None = ...,
    mask_labels: dict[str, int] | None = ...,
    t_r: float | None = ...,
    detrend: bool = ...,
    output_file: PosixPath | None = ...,
    figure: Figure | None = ...,
    axes: Axes | None = ...,
    vmin: None = ...,
    vmax: None = ...,
    title: str | None = ...,
    cmap: str = ...,
    cmap_labels: LinearSegmentedColormap = ...,
    standardize: str | bool = ...,
) -> Figure | None: ...
def plot_connectome(
    adjacency_matrix: coo_matrix | MaskedArray | ndarray,
    node_coords: list[tuple[int64, int64, int64]] | ndarray,
    node_color: str | list[str] | ndarray = ...,
    node_size: int | list[int] = ...,
    edge_cmap: LinearSegmentedColormap | str = ...,
    edge_vmin: None = ...,
    edge_vmax: None = ...,
    edge_threshold: float | object | str | None = ...,
    output_file: PosixPath | None = ...,
    display_mode: str = ...,
    figure: None = ...,
    axes: None = ...,
    title: str | None = ...,
    annotate: bool = ...,
    black_bg: bool = ...,
    alpha: float = ...,
    edge_kwargs: dict[str, int] | None = ...,
    node_kwargs: dict[str, int] | dict[str, str] | None = ...,
    colorbar: bool = ...,
    radiological: bool = ...,
) -> Any: ...
def plot_epi(
    epi_img: Nifti1Image | None = ...,
    cut_coords: int | tuple[int, int] | tuple[int, int, int] | None = ...,
    output_file: PosixPath | None = ...,
    display_mode: DisplayMode = ...,
    figure: None = ...,
    axes: None = ...,
    title: str | None = ...,
    annotate: bool = ...,
    draw_cross: bool = ...,
    black_bg: bool = ...,
    colorbar: bool = ...,
    cbar_tick_format: str = ...,
    cmap: LinearSegmentedColormap = ...,
    vmin: None = ...,
    vmax: None = ...,
    radiological: bool = ...,
    **kwargs,
) -> MosaicSlicer | OrthoSlicer | None: ...
def plot_glass_brain(
    stat_map_img: Nifti1Image | None,
    output_file: PosixPath | None = ...,
    display_mode: str = ...,
    colorbar: bool = ...,
    cbar_tick_format: str = ...,
    figure: None = ...,
    axes: Axes | None = ...,
    title: str | None = ...,
    threshold: ndarray | float | str | float64 | int = ...,
    annotate: bool = ...,
    black_bg: bool = ...,
    cmap: str | None = ...,
    alpha: float = ...,
    vmin: int | None = ...,
    vmax: int | None = ...,
    plot_abs: bool = ...,
    symmetric_cbar: bool | str = ...,
    resampling_interpolation: str = ...,
    radiological: bool = ...,
    **kwargs,
) -> Any: ...
def plot_img(
    img: Nifti1Image | _MNI152Template | bool,
    cut_coords: Any | None = ...,
    output_file: PosixPath | None = ...,
    display_mode: DisplayMode = ...,
    figure: Figure | None = ...,
    axes: Axes | None = ...,
    title: str | None = ...,
    threshold: int | float | None = ...,
    annotate: bool = ...,
    draw_cross: bool = ...,
    black_bg: bool = ...,
    colorbar: bool = ...,
    cbar_tick_format: str = ...,
    resampling_interpolation: str = ...,
    bg_img: None = ...,
    vmin: float64 | None = ...,
    vmax: float64 | int | None = ...,
    radiological: bool = ...,
    decimals: bool = ...,
    cmap: LinearSegmentedColormap | str = ...,
    **kwargs,
) -> Any: ...
def plot_img_comparison(
    ref_imgs: list[Nifti1Image],
    src_imgs: list[Nifti1Image],
    masker: NiftiMasker,
    plot_hist: bool = ...,
    log: bool = ...,
    ref_label: str = ...,
    src_label: str = ...,
    output_dir: None = ...,
    axes: ndarray | None = ...,
) -> list[float64]: ...
def plot_markers(
    node_values: list[str] | list[int] | tuple[int, int, int, int] | ndarray,
    node_coords: list[tuple[int64, int64, int64]] | list[list[int]] | ndarray,
    node_size: ndarray | float | str | int | list[int] = ...,
    node_cmap: ListedColormap | LinearSegmentedColormap | str = ...,
    node_vmin: int | None = ...,
    node_vmax: int | None = ...,
    node_threshold: float | None = ...,
    alpha: float = ...,
    output_file: PosixPath | None = ...,
    display_mode: str = ...,
    figure: None = ...,
    axes: None = ...,
    title: None = ...,
    annotate: bool = ...,
    black_bg: bool = ...,
    node_kwargs: dict[str, str] | None = ...,
    colorbar: bool = ...,
    radiological: bool = ...,
) -> OrthoProjector | XProjector | LYRZProjector | None: ...
def plot_prob_atlas(
    maps_img: Nifti1Image,
    bg_img: Nifti1Image | _MNI152Template = ...,
    view_type: str = ...,
    threshold: float | str | None = ...,
    linewidths: float = ...,
    cut_coords: None = ...,
    output_file: PosixPath | None = ...,
    display_mode: DisplayMode = ...,
    figure: None = ...,
    axes: None = ...,
    title: None = ...,
    annotate: bool = ...,
    draw_cross: bool = ...,
    black_bg: str = ...,
    dim: str = ...,
    colorbar: bool = ...,
    cmap: LinearSegmentedColormap = ...,
    vmin: None = ...,
    vmax: None = ...,
    alpha: float = ...,
    radiological: bool = ...,
    **kwargs,
) -> OrthoSlicer | None: ...
def plot_roi(
    roi_img: Nifti1Image | PosixPath,
    bg_img: Nifti1Image | _MNI152Template = ...,
    cut_coords: tuple[int, int]
    | tuple[int, int, int]
    | int
    | list[float]
    | None = ...,
    output_file: PosixPath | BufferedWriter | None = ...,
    display_mode: DisplayMode = ...,
    figure: None = ...,
    axes: None = ...,
    title: str | None = ...,
    annotate: bool = ...,
    draw_cross: bool = ...,
    black_bg: str | bool = ...,
    threshold: float = ...,
    alpha: float = ...,
    cmap: ListedColormap | LinearSegmentedColormap | str = ...,
    dim: str = ...,
    colorbar: bool = ...,
    cbar_tick_format: str = ...,
    vmin: None = ...,
    vmax: None = ...,
    resampling_interpolation: str = ...,
    view_type: str = ...,
    linewidths: float = ...,
    radiological: bool = ...,
    **kwargs,
) -> MosaicSlicer | ZSlicer | OrthoSlicer | XSlicer | None: ...
def plot_stat_map(
    stat_map_img: Nifti1Image,
    bg_img: Nifti1Image | _MNI152Template | None = ...,
    cut_coords: Any | None = ...,
    output_file: PosixPath | None = ...,
    display_mode: DisplayMode = ...,
    colorbar: bool = ...,
    cbar_tick_format: str = ...,
    figure: None = ...,
    axes: Axes | None = ...,
    title: str | None = ...,
    threshold: float | float64 | ndarray = ...,
    annotate: bool = ...,
    draw_cross: bool = ...,
    black_bg: str = ...,
    cmap: LinearSegmentedColormap | str = ...,
    symmetric_cbar: str | bool = ...,
    dim: str = ...,
    vmin: None = ...,
    vmax: int | float | None = ...,
    radiological: bool = ...,
    resampling_interpolation: str = ...,
    **kwargs,
) -> Any: ...

class _MNI152Template:
    def __init__(
        self,
        data: MaskedArray | ndarray | None = ...,
        affine: ndarray | None = ...,
        header: None = ...,
    ): ...
    @property
    def affine(self) -> ndarray: ...
    def load(self): ...
    @property
    def shape(self) -> tuple[int, int, int]: ...
