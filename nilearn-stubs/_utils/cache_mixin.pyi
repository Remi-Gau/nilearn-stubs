from typing import (
    Callable,
)

from joblib.memory import (
    MemorizedFunc,
    MemorizedResult,
    Memory,
    NotMemorizedFunc,
)

from nilearn.maskers.nifti_masker import _ExtractionFunctor

def cache(
    func: _ExtractionFunctor | Callable,
    memory: Memory | None,
    func_memory_level: int | None = ...,
    memory_level: int | None = ...,
    shelve: bool = ...,
    **kwargs,
) -> _ShelvedFunc | NotMemorizedFunc | MemorizedFunc: ...
def check_memory(memory: Memory | str | None, verbose: int = ...) -> Memory: ...

class CacheMixin:
    def _cache(
        self, func: Callable, func_memory_level: int = ..., shelve: bool = ..., **kwargs
    ) -> NotMemorizedFunc | MemorizedFunc: ...

class _ShelvedFunc:
    def __call__(self, *args, **kwargs) -> MemorizedResult: ...
    def __init__(self, func: MemorizedFunc) -> None: ...
