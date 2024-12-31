from io import BufferedWriter
from pathlib import PosixPath
from typing import (
    Any,
    Callable,
)

from matplotlib.axes._axes import Axes
from matplotlib.backends.backend_agg import RendererAgg
from matplotlib.backends.backend_mixed import MixedModeRenderer
from matplotlib.colors import (
    LinearSegmentedColormap,
    ListedColormap,
    Normalize,
)
from matplotlib.contour import QuadContourSet
from matplotlib.figure import Figure
from matplotlib.image import AxesImage
from matplotlib.transforms import Bbox
from nibabel.nifti1 import Nifti1Image
from nilearn.plotting.img_plotting import _MNI152Template
from numpy import (
    float32,
    float64,
    ndarray,
)
from numpy.ma.core import MaskedArray

def get_slicer(display_mode: str) -> Callable: ...

class BaseSlicer:
    def __init__(
        self,
        cut_coords: Any,
        axes: Axes | None = ...,
        black_bg: bool = ...,
        brain_color: tuple[float, float, float] = ...,
        **kwargs,
    ): ...
    def _map_show(
        self,
        img: _MNI152Template | Nifti1Image,
        type: str = ...,
        resampling_interpolation: str = ...,
        threshold: float64 | ndarray | float | int | None = ...,
        **kwargs,
    ) -> list[Any | AxesImage | QuadContourSet]: ...
    def _show_colorbar(
        self,
        cmap: ListedColormap | str | LinearSegmentedColormap,
        norm: Normalize,
        cbar_vmin: int | float32 | None = ...,
        cbar_vmax: int | float32 | None = ...,
        threshold: float64 | ndarray | float | int | None = ...,
    ): ...
    @classmethod
    def _threshold(
        cls,
        data: MaskedArray | ndarray,
        threshold: float | int | None = ...,
        vmin: Any | None = ...,
        vmax: Any | None = ...,
    ) -> MaskedArray | ndarray: ...
    def add_contours(
        self,
        img: Nifti1Image,
        threshold: float = ...,
        filled: bool = ...,
        **kwargs,
    ): ...
    def add_edges(self, img: Nifti1Image, color: str = ...): ...
    def add_markers(
        self,
        marker_coords: list[tuple[int, int, int]] | list[list[int]] | ndarray,
        marker_color: list[str]
        | list[tuple[float64, float64, float64, float64]]
        | str = ...,
        marker_size: int | float | list[int] | ndarray = ...,
        **kwargs,
    ): ...
    def add_overlay(
        self,
        img: _MNI152Template | Nifti1Image,
        threshold: float64 | ndarray | float | int | None = ...,
        colorbar: bool = ...,
        cbar_tick_format: str = ...,
        cbar_vmin: int | float32 | None = ...,
        cbar_vmax: int | float32 | None = ...,
        **kwargs,
    ): ...
    def annotate(
        self,
        left_right: bool = ...,
        positions: bool = ...,
        scalebar: bool = ...,
        size: int = ...,
        scale_size: float = ...,
        scale_units: str = ...,
        scale_loc: int = ...,
        decimals: int | bool = ...,
        **kwargs,
    ): ...
    @property
    def black_bg(self) -> bool: ...
    @property
    def brain_color(self) -> tuple[float, float, float]: ...
    def close(self): ...
    @classmethod
    def init_with_figure(
        cls,
        img: _MNI152Template | Nifti1Image | bool | None,
        threshold: Any | None = ...,
        cut_coords: Any | None = ...,
        figure: Figure | None = ...,
        axes: Axes | None = ...,
        black_bg: bool = ...,
        leave_space: bool = ...,
        colorbar: bool = ...,
        brain_color: tuple[float, float, float] = ...,
        **kwargs,
    ) -> BaseSlicer: ...
    def savefig(
        self, filename: BufferedWriter | PosixPath, dpi: None = ...
    ): ...
    def title(
        self,
        text: str,
        x: float = ...,
        y: float = ...,
        size: int = ...,
        color: None = ...,
        bgcolor: None = ...,
        alpha: int = ...,
        **kwargs,
    ): ...

class BaseStackedSlicer:
    def _init_axes(self, **kwargs): ...
    def _locator(
        self, axes: Axes, renderer: RendererAgg | MixedModeRenderer
    ) -> Bbox: ...
    def draw_cross(self, cut_coords: None = ..., **kwargs): ...
    @classmethod
    def find_cut_coords(
        cls,
        img: _MNI152Template | Nifti1Image | bool | None = ...,
        threshold: float64 | ndarray | float | int | None = ...,
        cut_coords: ndarray | int | list[float | int] | list[int] | None = ...,
    ) -> list[float | int] | list[float] | list[int] | ndarray: ...

class MosaicSlicer:
    @staticmethod
    def _find_cut_coords(
        img: Nifti1Image | None, cut_coords: list[int], cut_displayed: str
    ) -> dict[str, list[float] | ndarray]: ...
    def _init_axes(self, **kwargs): ...
    def _locator(self, axes: Axes, renderer: RendererAgg) -> Bbox: ...
    def draw_cross(self, cut_coords: None = ..., **kwargs): ...
    @classmethod
    def find_cut_coords(
        cls,
        img: Nifti1Image | None = ...,
        threshold: float | None = ...,
        cut_coords: tuple[int, int]
        | tuple[int, int, int, int]
        | tuple[int, int, int]
        | int
        | None = ...,
    ) -> dict[str, list[float] | ndarray]: ...

class OrthoSlicer:
    def _init_axes(self, **kwargs): ...
    def _locator(
        self, axes: Axes, renderer: RendererAgg | MixedModeRenderer
    ) -> Bbox: ...
    def draw_cross(self, cut_coords: None = ..., **kwargs): ...
    @classmethod
    def find_cut_coords(
        cls,
        img: _MNI152Template | bool | Nifti1Image | None = ...,
        threshold: float | int | None = ...,
        cut_coords: tuple[int, int]
        | tuple[int, int, int]
        | list[float]
        | list[int]
        | None = ...,
    ) -> tuple[int, int] | list[float] | list[int] | tuple[int, int, int]: ...

class TiledSlicer:
    def _adjust_width_height(
        self,
        width_dict: dict[Axes | None, int | float64],
        height_dict: dict[Axes | None, int | float64],
        rect_x0: float64,
        rect_y0: float64,
        rect_x1: float64,
        rect_y1: float64,
    ) -> tuple[dict[Axes | None, float64], dict[Axes | None, float64]]: ...
    def _find_axes_coord(
        self,
        rel_width_dict: dict[Axes | None, float64],
        rel_height_dict: dict[Axes | None, float64],
        rect_x0: float64,
        rect_y0: float64,
        rect_x1: float64,
        rect_y1: float64,
    ) -> tuple[
        dict[Axes, float64],
        dict[Axes, float64],
        dict[Axes, float64],
        dict[Axes, float64],
    ]: ...
    def _find_initial_axes_coord(self, index: int) -> list[float64]: ...
    def _init_axes(self, **kwargs): ...
    def _locator(self, axes: Axes, renderer: RendererAgg) -> Bbox: ...
    def draw_cross(self, cut_coords: None = ..., **kwargs): ...
    @classmethod
    def find_cut_coords(
        cls,
        img: _MNI152Template | Nifti1Image | None = ...,
        threshold: float | None = ...,
        cut_coords: tuple[int, int] | tuple[int, int, int] | None = ...,
    ) -> tuple[int, int] | list[float] | tuple[int, int, int]: ...
