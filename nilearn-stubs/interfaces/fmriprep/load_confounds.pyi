from typing import Literal

from numpy import ndarray
from pandas.core.frame import DataFrame

def load_confounds(
    img_files: str | list[str],
    strategy: tuple[
        Literal[
            "motion",
            "high_pass",
            "wm_csf",
            "global_signal",
            "compcor",
            "ica_aroma",
            "scrub",
            "non_steady_state",
        ],
        ...,
    ] = ...,
    motion: Literal["basic", "power2", "derivatives", "full"] = ...,
    scrub: int = ...,
    fd_threshold: float = ...,
    std_dvars_threshold: int = ...,
    wm_csf: Literal["basic", "power2", "derivatives", "full"] = ...,
    global_signal: Literal["basic", "power2", "derivatives", "full"] = ...,
    compcor: Literal[
        "anat_combined",
        "anat_separated",
        "temporal",
        "temporal_anat_combined",
        "temporal_anat_separated",
    ] = ...,
    n_compcor: int | Literal["all"] = ...,
    ica_aroma: Literal["basic", "full"] = ...,
    demean: bool = ...,
) -> tuple[
    DataFrame | list[DataFrame], None | ndarray | list[ndarray, None]
]: ...
