from typing import Callable

from numpy import ndarray

def compute_regressor(
    exp_condition: (
        tuple[ndarray, ndarray, ndarray]
        | tuple[list[int | float], list[int], list[int]]
    ),
    hrf_model: Callable | str,
    frame_times: ndarray,
    con_id: str = ...,
    oversampling: float = ...,
    fir_delays: range | list[int] | ndarray | None = ...,
    min_onset: int = ...,
) -> tuple[ndarray, list[str]]: ...
def glover_dispersion_derivative(
    t_r: float,
    oversampling: int = ...,
    time_length: float = ...,
    onset: float = ...,
) -> ndarray: ...
def glover_hrf(
    t_r: float,
    oversampling: int = ...,
    time_length: float = ...,
    onset: float = ...,
) -> ndarray: ...
def glover_time_derivative(
    t_r: float,
    oversampling: int = ...,
    time_length: float = ...,
    onset: float = ...,
) -> ndarray: ...
def spm_dispersion_derivative(
    t_r: float,
    oversampling: int = ...,
    time_length: float = ...,
    onset: float = ...,
) -> ndarray: ...
def spm_hrf(
    t_r: float,
    oversampling: int = ...,
    time_length: float = ...,
    onset: float = ...,
) -> ndarray: ...
def spm_time_derivative(
    t_r: float,
    oversampling: int = ...,
    time_length: float = ...,
    onset: float = ...,
) -> ndarray: ...
