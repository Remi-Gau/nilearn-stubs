from pathlib import PosixPath
from typing import Any

from nibabel.nifti1 import Nifti1Image
from numpy import float64, ndarray

def load_surf_data(surf_data: str | ndarray | PosixPath) -> ndarray: ...
def load_surf_mesh(surf_mesh: Any) -> InMemoryMesh: ...
def vol_to_surf(
    img: Nifti1Image,
    surf_mesh: tuple[ndarray, ndarray] | FileMesh | InMemoryMesh | str,
    radius: float = ...,
    interpolation: str = ...,
    kind: str = ...,
    n_samples: None = ...,
    mask_img: Nifti1Image | None = ...,
    inner_mesh: str | FileMesh | InMemoryMesh | None = ...,
    depth: list[float] | None = ...,
) -> ndarray: ...

class FileMesh:
    def __init__(self, file_path: PosixPath | str): ...
    @property
    def coordinates(self) -> ndarray: ...
    @property
    def faces(self) -> ndarray: ...
    def loaded(self) -> InMemoryMesh: ...

class InMemoryMesh:
    def __getitem__(self, index: int) -> ndarray: ...
    def __init__(self, coordinates: ndarray, faces: ndarray | None): ...

class PolyData:
    def __init__(
        self,
        left: str | ndarray | PosixPath | None = ...,
        right: str | ndarray | PosixPath | None = ...,
    ): ...
    def __repr__(self) -> str: ...
    def _check_ndims(self, dim: int, var_name: str = ...): ...
    def _check_parts(self): ...
    def _get_min_max(self) -> tuple[float64, float64]: ...
    @property
    def shape(self) -> tuple[int, int] | tuple[int]: ...
    def to_filename(self, filename: str | PosixPath): ...

class PolyMesh:
    def __init__(
        self,
        left: InMemoryMesh | str | FileMesh | PosixPath | None = ...,
        right: InMemoryMesh | str | FileMesh | PosixPath | None = ...,
    ) -> None: ...
    def to_filename(self, filename: PosixPath | str): ...

class SurfaceImage:
    def __init__(
        self,
        mesh: (
            dict[str, InMemoryMesh]
            | dict[str, str]
            | PolyMesh
            | dict[str, PosixPath]
        ),
        data: (
            dict[str, str]
            | dict[str, PosixPath]
            | int
            | dict[str, ndarray]
            | PolyData
        ),
    ): ...
    def __repr__(self) -> str: ...
    @classmethod
    def from_volume(
        cls,
        mesh: PolyMesh,
        volume_img: Nifti1Image | str | PosixPath,
        inner_mesh: PolyMesh | None = ...,
        **vol_to_surf_kwargs,
    ) -> SurfaceImage: ...
    @property
    def shape(self) -> tuple[int, int] | tuple[int]: ...

class SurfaceMesh:
    def __repr__(self) -> str: ...
    def to_gifti(self, gifti_file: PosixPath): ...
