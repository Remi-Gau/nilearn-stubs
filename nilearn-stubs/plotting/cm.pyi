from matplotlib.colors import LinearSegmentedColormap
from numpy import ndarray

def alpha_cmap(
    color: tuple[int, int, int] | ndarray,
    name: str = ...,
    alpha_min: float = ...,
    alpha_max: float = ...,
) -> LinearSegmentedColormap: ...
def dim_cmap(cmap: LinearSegmentedColormap, factor: float = ..., to_white: bool = ...) -> LinearSegmentedColormap: ...
def mix_colormaps(fg: ndarray, bg: ndarray) -> ndarray: ...
def replace_inside(
    outer_cmap: LinearSegmentedColormap,
    inner_cmap: LinearSegmentedColormap,
    vmin: float,
    vmax: float,
) -> LinearSegmentedColormap: ...
