from pathlib import PosixPath
from typing import Callable

from numpy import ndarray
from pandas.core.frame import DataFrame
from pandas.core.indexes.base import Index
from pandas.core.indexes.range import RangeIndex

def check_design_matrix(
    design_matrix: DataFrame,
) -> (
    tuple[Index, ndarray, list[str]]
    | tuple[Index, ndarray, list[str | int]]
    | tuple[RangeIndex, ndarray, list[str]]
): ...
def make_first_level_design_matrix(
    frame_times: ndarray,
    events: str | DataFrame | PosixPath | None = ...,
    hrf_model: Callable | str = ...,
    drift_model: str | None = ...,
    high_pass: float = ...,
    drift_order: int = ...,
    fir_delays: range | list[int] | None = ...,
    add_regs: DataFrame | ndarray | None = ...,
    add_reg_names: str | list[str] | None = ...,
    min_onset: int = ...,
    oversampling: int = ...,
) -> DataFrame: ...
def make_second_level_design_matrix(
    subjects_label: list[str], confounds: DataFrame | None = ...
) -> DataFrame: ...
