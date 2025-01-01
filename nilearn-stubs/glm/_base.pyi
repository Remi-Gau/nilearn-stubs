from nilearn.reporting.html_report import HTMLReport
from numpy import ndarray

class BaseGLM:
    def generate_report(
        self,
        contrasts: dict[str, ndarray] | str | dict[str, str] | ndarray,
        title: None = ...,
        bg_img: str = ...,
        threshold: float = ...,
        alpha: float = ...,
        cluster_threshold: int = ...,
        height_control: str | None = ...,
        min_distance: float = ...,
        plot_type: str = ...,
        display_mode: None = ...,
        report_dims: tuple[int, int] = ...,
    ) -> HTMLReport: ...
