from typing import (
    Any,
    Callable,
)

def _warn_deprecated_params(
    replacement_params: dict[str, str], end_version: str, lib_name: str, kwargs: dict[str, str]
) -> None: ...
def check_copy_header(copy_header: bool) -> None: ...
def compare_version(version_a: str, operator: str, version_b: str) -> bool: ...
def is_kaleido_installed() -> bool: ...
def is_matplotlib_installed() -> bool: ...
def is_plotly_installed() -> bool: ...
def remove_parameters(removed_params: list[str], reason: str, end_version: str = ...) -> Callable: ...
def rename_parameters(replacement_params: dict[str, str], end_version: str = ..., lib_name: str = ...) -> Callable: ...
def set_mpl_backend(message: str | None = ...): ...
def stringify_path(path: Any) -> Any: ...
def transfer_deprecated_param_vals(replacement_params: dict[str, str], kwargs: dict[str, str]) -> dict[str, str]: ...
