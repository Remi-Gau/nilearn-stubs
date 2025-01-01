from pathlib import PosixPath
from typing import (
    Any,
)

from sklearn.utils._bunch import Bunch

def fetch_abide_pcp(
    data_dir: PosixPath | None = ...,
    n_subjects: None = ...,
    pipeline: str = ...,
    band_pass_filtering: bool = ...,
    global_signal_regression: bool = ...,
    derivatives: str | None = ...,
    quality_checked: bool = ...,
    url: None = ...,
    verbose: int = ...,
    **kwargs,
) -> Bunch: ...
def fetch_adhd(
    n_subjects: int | None = ...,
    data_dir: PosixPath | None = ...,
    url: None = ...,
    resume: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_bids_langloc_dataset(
    data_dir: PosixPath | None = ..., verbose: int = ...
) -> tuple[str, list[Any]]: ...
def fetch_development_fmri(
    n_subjects: int | None = ...,
    reduce_confounds: bool = ...,
    data_dir: PosixPath | None = ...,
    resume: bool = ...,
    verbose: int = ...,
    age_group: str = ...,
) -> Bunch: ...
def fetch_ds000030_urls(
    data_dir: PosixPath | str | None = ..., verbose: int = ...
) -> tuple[str, list[str]]: ...
def fetch_fiac_first_level(
    data_dir: PosixPath | None = ..., verbose: int = ...
) -> Bunch: ...
def fetch_haxby(
    data_dir: PosixPath | None = ...,
    subjects: int | list[int] | list[str] | None = ...,
    fetch_stimuli: bool = ...,
    url: None = ...,
    resume: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_language_localizer_demo_dataset(
    data_dir: PosixPath | None = ...,
    verbose: int = ...,
    legacy_output: bool = ...,
) -> Bunch | tuple[str, list[str]]: ...
def fetch_localizer_button_task(
    data_dir: PosixPath | None = ..., verbose: int = ...
) -> Bunch: ...
def fetch_localizer_calculation_task(
    n_subjects: int = ..., data_dir: PosixPath | None = ..., verbose: int = ...
) -> Bunch: ...
def fetch_localizer_contrasts(
    contrasts: list[str] | str,
    n_subjects: int | list[int] | None = ...,
    get_tmaps: bool = ...,
    get_masks: bool = ...,
    get_anats: bool = ...,
    data_dir: PosixPath | None = ...,
    resume: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_localizer_first_level(
    data_dir: PosixPath | None = ..., verbose: int = ...
) -> Bunch: ...
def fetch_megatrawls_netmats(
    dimensionality: int = ...,
    timeseries: str = ...,
    matrices: str = ...,
    data_dir: PosixPath | None = ...,
    resume: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_mixed_gambles(
    n_subjects: int = ...,
    data_dir: PosixPath | None = ...,
    url: None = ...,
    resume: bool = ...,
    return_raw_data: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_miyawaki2008(
    data_dir: PosixPath | None = ...,
    url: None = ...,
    resume: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_openneuro_dataset(
    urls: list[str] | None = ...,
    data_dir: PosixPath | None = ...,
    dataset_version: str = ...,
    verbose: int = ...,
) -> tuple[str, list[str]]: ...
def fetch_spm_auditory(
    data_dir: PosixPath | None = ...,
    data_name: str = ...,
    subject_id: None = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_spm_multimodal_fmri(
    data_dir: PosixPath | None = ...,
    data_name: str = ...,
    subject_id: str = ...,
    verbose: int = ...,
) -> Bunch: ...
def fetch_surf_nki_enhanced(
    n_subjects: int = ...,
    data_dir: PosixPath | None = ...,
    url: None = ...,
    resume: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def load_nki(
    mesh: str = ...,
    mesh_type: str = ...,
    n_subjects: int = ...,
    data_dir: None = ...,
    url: None = ...,
    resume: bool = ...,
    verbose: int = ...,
): ...
def load_sample_motor_activation_image() -> str: ...
def patch_openneuro_dataset(file_list: list[str]): ...
def select_from_index(
    urls: list[str],
    inclusion_filters: list[str] | None = ...,
    exclusion_filters: list[str] | None = ...,
    n_subjects: int | None = ...,
) -> list[str]: ...