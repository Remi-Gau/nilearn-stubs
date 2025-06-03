from pathlib import PosixPath
from typing import (
    Any,
)

from numpy import ndarray

def as_ndarray(arr: Any, copy: bool = ..., dtype: Any | None = ..., order: str | None = ...) -> ndarray: ...
def csv_to_array(csv_path: str | PosixPath, delimiters: str = ..., **kwargs) -> ndarray: ...
