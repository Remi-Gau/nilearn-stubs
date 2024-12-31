from pathlib import PosixPath
from typing import (
    Any,
)

from matplotlib.figure import Figure
from nilearn.surface.surface import SurfaceImage
from numpy import (
    bool_,
    float64,
    ndarray,
)
from plotly.graph_objs._figure import Figure as PlotlyFigure

class PlotlySurfaceFigure:
    def __init__(
        self,
        figure: Figure | list[str] | str | PlotlyFigure | None = ...,
        output_file: PosixPath | None = ...,
        hemi: str = ...,
    ): ...
    @property
    def _coords(self) -> ndarray: ...
    @staticmethod
    def _do_segs_intersect(
        x1: float64 | int,
        y1: float64 | int,
        x2: float64 | int,
        y2: float64 | int,
        x3: float64 | int,
        y3: float64 | int,
        x4: float64 | int,
        y4: float64 | int,
    ) -> bool_: ...
    @property
    def _faces(self) -> ndarray: ...
    def _get_faces_on_edge(self, parc_idx: list[int] | ndarray) -> ndarray: ...
    def _get_sorted_edge_centroids(
        self, parc_idx: ndarray, elevation: float = ...
    ) -> ndarray: ...
    @staticmethod
    def _project_above_face(
        point: ndarray,
        t0: ndarray,
        t1: ndarray,
        t2: ndarray,
        elevation: float = ...,
    ) -> ndarray: ...
    @staticmethod
    def _transform_coord_to_plane(
        v: ndarray, t0: ndarray, t1: ndarray, t2: ndarray
    ) -> tuple[float64, float64]: ...
    def add_contours(
        self,
        roi_map: SurfaceImage | ndarray,
        levels: list[int] | None = ...,
        labels: list[str] | None = ...,
        lines: list[dict[Any, Any]]
        | list[dict[str, int]]
        | list[dict[str, str]]
        | None = ...,
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
    def _check_output_file(self, output_file: str | None = ...): ...
    def add_contours(self): ...
    def show(self): ...
