from pathlib import PosixPath

from nibabel.nifti1 import Nifti1Image
from numpy import ndarray

from nilearn.glm.regression import RegressionResults, SimpleRegressionResults
from nilearn.maskers.surface_masker import SurfaceMasker
from nilearn.surface.surface import SurfaceImage

def compute_contrast(
    labels: ndarray,
    regression_result: (
        dict[str, RegressionResults]
        | dict[float, RegressionResults]
        | dict[float, SimpleRegressionResults]
        | dict[str, SimpleRegressionResults]
    ),
    con_val: list[int] | ndarray,
    stat_type: str | None = ...,
) -> Contrast: ...
def compute_fixed_effect_contrast(
    labels: list[ndarray],
    results: list[dict[float, RegressionResults] | dict[str, RegressionResults] | dict[str, SimpleRegressionResults]],
    con_vals: list[ndarray],
    stat_type: str | None = ...,
) -> Contrast: ...
def compute_fixed_effects(
    contrast_imgs: list[Nifti1Image | SurfaceImage],
    variance_imgs: list[Nifti1Image | SurfaceImage],
    mask: SurfaceMasker | PosixPath | SurfaceImage | None = ...,
    precision_weighted: bool = ...,
    dofs: list[int] | None = ...,
    return_z_score: bool = ...,
) -> (
    tuple[SurfaceImage, SurfaceImage, SurfaceImage]
    | tuple[Nifti1Image, Nifti1Image, Nifti1Image, Nifti1Image]
    | tuple[Nifti1Image, Nifti1Image, Nifti1Image]
): ...
def expression_to_contrast_vector(expression: str, design_columns: list[str]) -> ndarray: ...

class Contrast:
    def __add__(self, other: Contrast) -> Contrast: ...
    def __init__(
        self,
        effect: ndarray,
        variance: ndarray,
        dim: int | None = ...,
        dof: float = ...,
        stat_type: str = ...,
        tiny: float = ...,
        dofmax: float = ...,
    ): ...
    def __rmul__(self, scalar: int | float) -> Contrast: ...
    @property
    def contrast_type(self) -> str: ...
    def effect_size(self) -> ndarray: ...
    def effect_variance(self) -> ndarray: ...
    def one_minus_pvalue(self, baseline: float = ...) -> ndarray: ...
    def p_value(self, baseline: float = ...) -> ndarray: ...
    def stat(self, baseline: float = ...) -> ndarray: ...
    def z_score(self, baseline: float = ...) -> ndarray: ...
