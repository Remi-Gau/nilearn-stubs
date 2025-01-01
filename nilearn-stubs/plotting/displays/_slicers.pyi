from io import BufferedWriter
from pathlib import PosixPath
from typing import Any, Callable

from matplotlib.axes._axes import Axes
from matplotlib.figure import Figure
from nibabel.nifti1 import Nifti1Image
from nilearn.plotting.img_plotting import _MNI152Template
from numpy import float32, float64, ndarray

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
        marker_color: (
            list[tuple[float64, float64, float64, float64]] | list[str] | str
        ) = ...,
        marker_size: int | float | list[int] | ndarray = ...,
        **kwargs,
    ): ...
    def add_overlay(
        self,
        img: _MNI152Template | Nifti1Image,
        threshold: float64 | ndarray | float | None = ...,
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
        img: bool | _MNI152Template | Nifti1Image | None,
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
    def draw_cross(self, cut_coords: None = ..., **kwargs): ...
    @classmethod
    def find_cut_coords(
        cls,
        img: bool | _MNI152Template | Nifti1Image | None = ...,
        threshold: float64 | ndarray | float | None = ...,
        cut_coords: ndarray | int | list[float] | list[int] | None = ...,
    ) -> list[float] | list[float] | list[int] | ndarray: ...

class MosaicSlicer:
    def draw_cross(self, cut_coords: None = ..., **kwargs): ...
    @classmethod
    def find_cut_coords(
        cls,
        img: Nifti1Image | None = ...,
        threshold: float | None = ...,
        cut_coords: (
            tuple[int, int]
            | tuple[int, int, int, int]
            | tuple[int, int, int]
            | int
            | None
        ) = ...,
    ) -> dict[str, ndarray | list[float]]: ...

class OrthoSlicer:
    def draw_cross(self, cut_coords: None = ..., **kwargs): ...
    @classmethod
    def find_cut_coords(
        cls,
        img: _MNI152Template | Nifti1Image | bool | None = ...,
        threshold: float | None = ...,
        cut_coords: (
            tuple[int, int]
            | tuple[int, int, int]
            | list[float]
            | list[int]
            | None
        ) = ...,
    ) -> tuple[int, int] | list[float] | list[int] | tuple[int, int, int]: ...

class TiledSlicer:
    def draw_cross(self, cut_coords: None = ..., **kwargs): ...
    @classmethod
    def find_cut_coords(
        cls,
        img: _MNI152Template | Nifti1Image | None = ...,
        threshold: float | None = ...,
        cut_coords: tuple[int, int] | tuple[int, int, int] | None = ...,
    ) -> tuple[int, int] | list[float] | tuple[int, int, int]: ...

class XSlicer(BaseStackedSlicer): ...
class YSlicer(BaseStackedSlicer): ...
class ZSlicer(BaseStackedSlicer): ...
class XZSlicer(OrthoSlicer): ...
class YXSlicer(OrthoSlicer): ...
class YZSlicer(OrthoSlicer): ...
