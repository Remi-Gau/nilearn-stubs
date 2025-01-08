import os
from typing import TypeAlias

from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from pandas.core.frame import DataFrame

NiimgLike: TypeAlias = str | os.PathLike[str] | Nifti1Image | Nifti2Image

def get_clusters_table(
    stat_img: NiimgLike,
    stat_threshold: float,
    cluster_threshold: int | None = ...,
    two_sided: bool = ...,
    min_distance: float = ...,
    return_label_maps: bool = ...,
) -> tuple[DataFrame, list[Nifti1Image]] | DataFrame: ...
