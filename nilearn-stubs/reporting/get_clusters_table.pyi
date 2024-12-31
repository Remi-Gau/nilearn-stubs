from nibabel.nifti1 import Nifti1Image
from numpy import (
    float64,
)
from pandas.core.frame import DataFrame

def get_clusters_table(
    stat_img: Nifti1Image | str,
    stat_threshold: int | float | float64,
    cluster_threshold: int | None = ...,
    two_sided: bool = ...,
    min_distance: int | float = ...,
    return_label_maps: bool = ...,
) -> tuple[DataFrame, list[Nifti1Image]] | DataFrame: ...
