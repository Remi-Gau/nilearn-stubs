from collections.abc import Iterator
from pathlib import PosixPath
from re import RegexFlag
from typing import (
    Any,
    Callable,
)

from numpy import (
    int64,
    ndarray,
)
from requests.sessions import Session
from sklearn.utils._bunch import Bunch

def _add_absolute_paths(
    root_dir: PosixPath,
    metadata: dict[str, int | bool | str | float | PosixPath],
    force: bool = ...,
) -> dict[str, int | bool | str | float | PosixPath]: ...
def _append_filters_to_query(
    query: str, filters: dict[str, int] | None
) -> str: ...
def _check_has_words(file_name: PosixPath): ...
def _download_collection(
    collection: dict[str, int] | None, download_params: dict[str, Any]
) -> dict[str, int | str | PosixPath]: ...
def _download_image(
    image_info: dict[str, int | bool | str | float] | None,
    download_params: dict[str, Any],
) -> dict[str, int | bool | str | float | PosixPath]: ...
def _download_image_nii_file(
    image_info: dict[str, int | bool | str | float],
    collection: dict[str, int | str | PosixPath],
    download_params: dict[str, Any],
) -> (
    tuple[
        dict[str, int | bool | str | float | PosixPath],
        dict[str, int | str | PosixPath],
    ]
    | tuple[
        dict[str, int | bool | str | float | PosixPath],
        dict[str, int | PosixPath],
    ]
): ...
def _download_image_terms(
    image_info: dict[str, int | bool | str | float | PosixPath],
    collection: dict[str, int | str | PosixPath],
    download_params: dict[str, Any],
) -> (
    tuple[dict[str, str | PosixPath], dict[str, str | PosixPath]]
    | tuple[
        dict[str, int | bool | str | float | PosixPath],
        dict[str, int | str | PosixPath],
    ]
    | tuple[
        dict[str, int | bool | str | float | PosixPath],
        dict[str, int | PosixPath],
    ]
): ...
def _empty_filter(result: dict[str, Any]): ...
def _fetch_collection_for_image(
    image_info: dict[str, int | bool | str | float | PosixPath],
    download_params: dict[str, Any],
) -> dict[str, int | str | PosixPath]: ...
def _fetch_neurovault_implementation(
    max_images: int = ...,
    collection_terms: dict[str, NotNull] | None = ...,
    collection_filter: Callable = ...,
    image_terms: dict[str, bool | NotIn | NotEqual] | None = ...,
    image_filter: Callable = ...,
    collection_ids: list[int64] | tuple[()] | None = ...,
    image_ids: list[int64] | tuple[()] | ndarray | None = ...,
    mode: str = ...,
    data_dir: PosixPath | None = ...,
    fetch_neurosynth_words: bool = ...,
    resample: bool = ...,
    interpolation: str = ...,
    vectorize_words: bool = ...,
    verbose: int = ...,
    **kwarg_image_filters,
) -> Bunch: ...
def _get_batch(
    query: str, prefix_msg: str = ..., timeout: float = ..., verbose: int = ...
) -> dict[
    str, int | list[dict[str, int | bool | str | float]] | list[dict[str, int]]
]: ...
def _json_add_collection_dir(
    file_name: PosixPath, force: bool = ...
) -> dict[str, int | PosixPath]: ...
def _json_add_im_files_paths(
    file_name: PosixPath, force: bool = ...
) -> dict[str, int | bool | str | float | PosixPath]: ...
def _json_from_file(
    file_name: PosixPath,
) -> dict[str, int | bool | str | float]: ...
def _move_col_id(
    im_terms: dict[str, int | bool | NotIn | NotEqual],
    col_terms: dict[str, int | NotNull],
) -> (
    tuple[dict[str, int | bool], dict[str, int]]
    | tuple[dict[str, bool | NotIn | NotEqual], dict[str, NotNull]]
    | tuple[dict[str, bool], dict[str, int]]
): ...
def _move_unknown_terms_to_local_filter(
    terms: dict[str, bool | NotIn | NotEqual | int | NotNull],
    local_filter: ResultFilter | Callable,
    available_on_server: tuple[()] | tuple[str, str, str, str] | tuple[str],
) -> (
    tuple[dict[Any, Any], ResultFilter] | tuple[dict[str, int], ResultFilter]
): ...
def _prepare_download_params(
    download_params: dict[str, Any],
) -> dict[str, Any]: ...
def _prepare_explicit_ids_download_params(
    download_params: dict[str, Any],
) -> dict[str, Any]: ...
def _prepare_filtered_download_params(
    download_params: dict[str, Any],
) -> dict[str, Any]: ...
def _print_progress(
    found: int, download_params: dict[str, Any], level: int = ...
): ...
def _read_download_params(
    data_dir: PosixPath,
    download_mode: str = ...,
    collection_terms: dict[str, NotNull] | None = ...,
    collection_filter: Callable = ...,
    image_terms: dict[str, bool | NotIn | NotEqual] | None = ...,
    image_filter: Callable = ...,
    wanted_collection_ids: list[int64] | tuple[()] | None = ...,
    wanted_image_ids: list[int64] | tuple[()] | ndarray | None = ...,
    max_images: int | None = ...,
    max_consecutive_fails: int = ...,
    max_fails_in_collection: int = ...,
    resample: bool = ...,
    interpolation: str = ...,
    batch_size: None = ...,
    verbose: int = ...,
    fetch_neurosynth_words: bool = ...,
    vectorize_words: bool = ...,
) -> dict[str, Any]: ...
def _remove_none_strings(
    metadata: dict[str, int | bool | str | float | None],
) -> dict[str, int | bool | str | float | None]: ...
def _requests_session() -> Session: ...
def _result_list_to_bunch(
    result_list: list[
        tuple[
            dict[str, int | bool | str | float | PosixPath],
            dict[str, int | PosixPath],
        ]
        | Any
        | tuple[
            dict[str, int | bool | str | float | PosixPath],
            dict[str, int | str | PosixPath],
        ]
    ],
    download_params: dict[str, Any],
) -> Bunch: ...
def _scroll(
    download_params: dict[str, Any],
) -> Iterator[
    tuple[
        dict[str, int | bool | str | float | PosixPath],
        dict[str, int | str | PosixPath],
    ]
    | tuple[
        dict[str, int | bool | str | float | PosixPath],
        dict[str, int | PosixPath],
    ]
]: ...
def _scroll_collection(
    collection: dict[str, int | str | PosixPath] | None,
    download_params: dict[str, Any],
) -> Iterator[dict[str, int | bool | str | float | PosixPath] | None]: ...
def _scroll_collection_ids(
    download_params: dict[str, Any],
) -> Iterator[
    tuple[
        dict[str, int | bool | str | float | PosixPath],
        dict[str, int | str | PosixPath],
    ]
]: ...
def _scroll_explicit(
    download_params: dict[str, Any],
) -> Iterator[
    tuple[
        dict[str, int | bool | str | float | PosixPath],
        dict[str, int | str | PosixPath],
    ]
    | tuple[
        dict[str, int | bool | str | float | PosixPath],
        dict[str, int | PosixPath],
    ]
]: ...
def _scroll_image_ids(
    download_params: dict[str, Any],
) -> Iterator[
    tuple[
        dict[str, int | bool | str | float | PosixPath],
        dict[str, int | PosixPath],
    ]
]: ...
def _scroll_local(
    download_params: dict[str, Any],
) -> Iterator[
    tuple[
        dict[str, int | bool | str | float | PosixPath],
        dict[str, int | PosixPath],
    ]
]: ...
def _scroll_server_results(
    url: str,
    local_filter: ResultFilter | Callable = ...,
    query_terms: None = ...,
    max_results: int | None = ...,
    batch_size: int | None = ...,
    prefix_msg: str = ...,
    verbose: int = ...,
) -> Iterator[dict[str, int | bool | str | float]]: ...
def _simple_download(
    url: str, target_file: PosixPath, temp_dir: PosixPath, verbose: int = ...
) -> PosixPath: ...
def _split_terms(
    terms: dict[str, Any],
    available_on_server: tuple[()] | tuple[str, str, str, str] | tuple[str],
) -> (
    tuple[dict[str, NotNull | str], dict[str, str]]
    | tuple[dict[str, int], dict[str, int]]
    | tuple[dict[str, bool | NotIn | NotEqual], dict[Any, Any]]
    | tuple[dict[str, NotNull], dict[Any, Any]]
): ...
def _update(
    image_info: dict[str, int | bool | str | float | PosixPath],
    collection: dict[str, int | PosixPath],
    download_params: dict[str, Any],
) -> tuple[
    dict[str, int | bool | str | float | PosixPath], dict[str, int | PosixPath]
]: ...
def _update_image(
    image_info: dict[str, int | bool | str | float | PosixPath],
    download_params: dict[str, Any],
) -> dict[str, int | bool | str | float | PosixPath]: ...
def _write_metadata(
    metadata: dict[str, int | bool | str | float | PosixPath],
    file_name: PosixPath,
): ...
def _yield_from_url_list(
    url_list: list[Any | str], verbose: int = ...
) -> Iterator[dict[str, int | bool | str | float]]: ...
def basic_collection_terms() -> dict[str, NotNull]: ...
def basic_image_terms() -> dict[str, bool | NotIn | NotEqual]: ...
def fetch_neurovault(
    max_images: int = ...,
    collection_terms: None = ...,
    collection_filter: Callable = ...,
    image_terms: None = ...,
    image_filter: Callable = ...,
    mode: str = ...,
    data_dir: PosixPath | None = ...,
    fetch_neurosynth_words: bool = ...,
    resample: bool = ...,
    vectorize_words: bool = ...,
    verbose: int = ...,
    **kwarg_image_filters,
) -> Bunch: ...
def fetch_neurovault_ids(
    collection_ids: list[int64] | tuple[()] = ...,
    image_ids: list[int64] | tuple[()] | ndarray = ...,
    mode: str = ...,
    data_dir: PosixPath | None = ...,
    fetch_neurosynth_words: bool = ...,
    resample: bool = ...,
    vectorize_words: bool = ...,
    verbose: int = ...,
) -> Bunch: ...
def neurosynth_words_vectorized(
    word_files: list[PosixPath] | list[str] | tuple[tuple[PosixPath, str]],
    verbose: int = ...,
    **kwargs,
) -> tuple[ndarray, ndarray]: ...

class Contains:
    def __eq__(self, other: int | list[str | int] | str) -> bool: ...
    def __init__(self, *must_be_contained): ...
    def __repr__(self) -> str: ...

class GreaterOrEqual:
    def _eq_impl(self, other: float | str) -> bool: ...

class GreaterThan:
    def _eq_impl(self, other: float | str) -> bool: ...

class IsIn:
    def __eq__(self, other: int | str) -> bool: ...
    def __init__(self, *accepted): ...
    def __repr__(self) -> str: ...

class IsNull:
    def __eq__(self, other: int | str | None) -> bool: ...

class LessOrEqual:
    def _eq_impl(self, other: float) -> bool: ...

class LessThan:
    def _eq_impl(self, other: float | int) -> bool: ...

class NotContains:
    def __eq__(self, other: str) -> bool: ...
    def __init__(self, *must_not_be_contained): ...
    def __repr__(self) -> str: ...

class NotEqual:
    def __eq__(self, other: int | str | NotEqual) -> bool: ...
    def __init__(self, negated: int | str): ...

class NotIn:
    def __eq__(self, other: int | NotIn | str) -> bool: ...
    def __init__(self, *rejected): ...
    def __repr__(self) -> str: ...

class NotNull:
    def __eq__(self, other: int | NotNull | str | None) -> bool: ...

class Pattern:
    def __eq__(self, other: str) -> bool: ...
    def __init__(self, pattern: str, flags: int | RegexFlag = ...): ...
    def __repr__(self) -> str: ...

class ResultFilter:
    def AND(self, other_filter: ResultFilter | Callable) -> ResultFilter: ...
    def NOT(self) -> ResultFilter: ...
    def OR(self, other_filter: ResultFilter) -> ResultFilter: ...
    def XOR(self, other_filter: ResultFilter) -> ResultFilter: ...
    def __call__(self, candidate: dict[str, Any]) -> bool: ...
    def __delitem__(self, item: str): ...
    def __getitem__(self, item: str) -> int: ...
    def __init__(
        self,
        query_terms: Any | None = ...,
        callable_filter: Callable = ...,
        **kwargs,
    ): ...
    def __setitem__(self, item: str, value: IsIn | NotNull | NotIn): ...
    def __str__(self) -> str: ...
    def add_filter(self, callable_filter: Callable): ...

class _OrderComp:
    def __eq__(self, other: float | int | str) -> bool: ...
    def __init__(self, bound: float | int | str): ...

class _SpecialValue:
    def __ne__(self, other: float | int | list[str | int] | str) -> bool: ...
    def __repr__(self) -> str: ...

class _TemporaryDirectory:
    def __enter__(self) -> PosixPath: ...
    def __exit__(self, *args): ...
    def __init__(self): ...
