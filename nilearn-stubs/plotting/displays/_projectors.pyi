from typing import Any, Callable

from matplotlib.colors import LinearSegmentedColormap
from nibabel.nifti1 import Nifti1Image
from numpy import int64, ndarray
from numpy.ma.core import MaskedArray
from scipy.sparse._coo import coo_matrix

def get_projector(display_mode: str) -> Callable: ...

class OrthoProjector:
    def _check_inputs_add_graph(
        self,
        adjacency_matrix: MaskedArray | ndarray,
        node_coords: ndarray,
        node_color: list[str] | ndarray | str,
        node_kwargs: dict[str, int | str],
    ): ...
    def add_graph(
        self,
        adjacency_matrix: coo_matrix | MaskedArray | ndarray,
        node_coords: list[list[float]]
        | list[tuple[int64, int64, int64]]
        | ndarray,
        node_color: list[str] | ndarray | str = ...,
        node_size: int | list[int] = ...,
        edge_cmap: LinearSegmentedColormap | str = ...,
        edge_vmin: None = ...,
        edge_vmax: None = ...,
        edge_threshold: float | object | str | None = ...,
        edge_kwargs: dict[str, int] | None = ...,
        node_kwargs: dict[str, str] | dict[str, int] | None = ...,
        colorbar: bool = ...,
    ): ...
    def draw_cross(self, cut_coords: None = ..., **kwargs): ...
    @classmethod
    def find_cut_coords(
        cls,
        img: Nifti1Image | None = ...,
        threshold: Any | None = ...,
        cut_coords: None = ...,
    ) -> (
        tuple[None, None, None, None]
        | tuple[None, None]
        | tuple[None]
        | tuple[None, None, None]
    ): ...

class LYRProjector(OrthoProjector): ...
class LYRZProjector(OrthoProjector): ...
class LZRProjector(OrthoProjector): ...
class LZRYProjector(OrthoProjector): ...
class LProjector(OrthoProjector): ...
class LRProjector(OrthoProjector): ...
class RProjector(OrthoProjector): ...
class XProjector(OrthoProjector): ...
class XZProjector(OrthoProjector): ...
class YProjector(OrthoProjector): ...
class YXProjector(OrthoProjector): ...
class YZProjector(OrthoProjector): ...
class ZProjector(OrthoProjector): ...
