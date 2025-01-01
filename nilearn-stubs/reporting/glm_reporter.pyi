from nilearn.glm.first_level.first_level import FirstLevelModel
from nilearn.glm.second_level.second_level import SecondLevelModel
from nilearn.reporting.html_report import HTMLReport
from numpy import ndarray

def make_glm_report(
    model: FirstLevelModel | SecondLevelModel,
    contrasts: dict[str, str] | dict[str, ndarray] | ndarray | str,
    title: None = ...,
    bg_img: str = ...,
    threshold: float | int = ...,
    alpha: float = ...,
    cluster_threshold: int = ...,
    height_control: str | None = ...,
    two_sided: bool = ...,
    min_distance: float | int = ...,
    plot_type: str = ...,
    cut_coords: None = ...,
    display_mode: None = ...,
    report_dims: tuple[int, int] = ...,
) -> HTMLReport: ...
