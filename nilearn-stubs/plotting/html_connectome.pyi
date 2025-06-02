from matplotlib.colors import LinearSegmentedColormap
from numpy import ndarray

from nilearn.plotting.html_document import HTMLDocument

class ConnectomeView(HTMLDocument):
    pass

def view_connectome(
    adjacency_matrix: ndarray,
    node_coords: ndarray,
    edge_threshold: str | None = ...,
    edge_cmap: LinearSegmentedColormap = ...,
    symmetric_cmap: bool = ...,
    linewidth: float = ...,
    node_color: str = ...,
    node_size: float | ndarray = ...,
    colorbar: bool = ...,
    colorbar_height: float = ...,
    colorbar_fontsize: int = ...,
    title: str | None = ...,
    title_fontsize: int = ...,
) -> ConnectomeView: ...
def view_markers(
    marker_coords: ndarray,
    marker_color: list[str] | str = ...,
    marker_size: float | list[int] | ndarray = ...,
    marker_labels: list[str] | None = ...,
    title: None = ...,
    title_fontsize: int = ...,
) -> ConnectomeView: ...
