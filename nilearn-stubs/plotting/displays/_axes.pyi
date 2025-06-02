from matplotlib.axes._axes import Axes
from matplotlib.contour import QuadContourSet
from matplotlib.image import AxesImage
from numpy import float64, ma, ndarray
from numpy.ma.core import MaskedArray

class BaseAxes:
    def __init__(
        self,
        ax: Axes | None,
        direction: str | None,
        coord: int | float | None,
        radiological: bool = ...,
    ): ...
    def add_object_bounds(self, bounds: tuple[float64, float64, float64, float64]): ...
    def draw_2d(
        self,
        data_2d: ndarray | ma.MaskedArray | None,
        data_bounds: list[tuple[float64, float64]] | None,
        bounding_box: (
            list[tuple[float64, float64]]
            | tuple[
                tuple[float64, float64],
                tuple[float64, float64],
                tuple[float64, float64],
            ]
            | None
        ),
        type: str = ...,
        **kwargs,
    ) -> AxesImage | QuadContourSet: ...
    def draw_left_right(self, size: int, bg_color: str, **kwargs): ...
    def draw_position(self, size: None, bg_color: None, **kwargs): ...
    def draw_scale_bar(
        self,
        bg_color: str,
        size: float = ...,
        units: str = ...,
        fontproperties: None = ...,
        frameon: bool = ...,
        loc: int = ...,
        pad: float = ...,
        borderpad: float = ...,
        sep: int = ...,
        size_vertical: int = ...,
        label_top: bool = ...,
        color: str = ...,
        fontsize: int | None = ...,
        **kwargs,
    ): ...
    def get_object_bounds(
        self,
    ) -> tuple[float64, float64, float64, float64]: ...
    def transform_to_2d(self, data: None, affine: None): ...

class CutAxes:
    def draw_position(self, size: int, bg_color: str, decimals: int | bool = ..., **kwargs): ...
    def transform_to_2d(self, data: MaskedArray | ndarray | None, affine: ndarray) -> MaskedArray | ndarray: ...

class GlassBrainAxes:
    def __init__(
        self,
        ax: Axes | None,
        direction: str | None,
        coord: int | None,
        plot_abs: bool = ...,
        radiological: bool = ...,
        **kwargs,
    ): ...
    def draw_position(self, size: int, bg_color: str, **kwargs): ...
    def transform_to_2d(self, data: MaskedArray, affine: ndarray) -> MaskedArray: ...
