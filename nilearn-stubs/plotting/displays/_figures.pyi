from pathlib import PosixPath
from typing import Any

from matplotlib.figure import Figure
from numpy import ndarray
from plotly.graph_objs._figure import Figure as PlotlyFigure

from nilearn.surface.surface import SurfaceImage

class PlotlySurfaceFigure:
    def __init__(
        self,
        figure: Figure | list[str] | str | PlotlyFigure | None = ...,
        output_file: PosixPath | None = ...,
        hemi: str = ...,
    ): ...
    @staticmethod
    def add_contours(
        self,
        roi_map: SurfaceImage | ndarray,
        levels: list[int] | None = ...,
        labels: list[str] | None = ...,
        lines: (list[dict[Any, Any]] | list[dict[str, int]] | list[dict[str, str]] | None) = ...,
        elevation: float = ...,
    ): ...
    def savefig(self, output_file: str | None = ...): ...
    def show(self, renderer: str = ...) -> PlotlyFigure: ...

class SurfaceFigure:
    def __init__(
        self,
        figure: Figure | None = ...,
        output_file: PosixPath | str | None = ...,
        hemi: str = ...,
    ): ...
    def add_contours(self): ...
    def show(self): ...
