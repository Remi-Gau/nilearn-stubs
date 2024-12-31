from pathlib import PosixPath

from nilearn.plotting.html_connectome import ConnectomeView
from nilearn.plotting.html_surface import SurfaceView
from numpy import float64

class HTMLDocument:
    def __init__(
        self, html: str, width: int = ..., height: int | float64 = ...
    ): ...
    def __str__(self) -> str: ...
    def _check_n_open(self): ...
    def _repr_html_(self) -> str: ...
    def _repr_mimebundle_(
        self, include: None = ..., exclude: None = ...
    ) -> dict[str, str]: ...
    def get_iframe(
        self, width: int | None = ..., height: int | None = ...
    ) -> str: ...
    def get_standalone(self) -> str: ...
    def open_in_browser(
        self,
        file_name: str | None = ...,
        temp_file_lifetime: float | str = ...,
    ): ...
    def resize(
        self, width: int, height: int
    ) -> ConnectomeView | SurfaceView: ...
    def save_as_html(self, file_name: PosixPath | str): ...
