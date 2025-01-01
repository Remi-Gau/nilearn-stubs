import os
from collections.abc import Sequence
from pathlib import PosixPath
from typing import Literal

from nibabel.nifti1 import Nifti1Image
from nibabel.nifti2 import Nifti2Image
from numpy import ndarray
from typing_extensions import TypeAlias

FilePath: TypeAlias = str | os.PathLike[str]
NiimgLike: TypeAlias = FilePath | Nifti1Image | Nifti2Image

def load_surf_data(surf_data: FilePath | ndarray) -> ndarray: ...
def load_surf_mesh(
    surf_mesh: FilePath | ndarray | InMemoryMesh,
) -> InMemoryMesh: ...
def vol_to_surf(
    img: NiimgLike,
    surf_mesh: ndarray | InMemoryMesh | FilePath,
    radius: float = ...,
    interpolation: Literal["linear", "nearest"] = ...,
    kind: Literal["auto", "depth", "line", "ball"] = ...,
    n_samples: int | None = ...,
    mask_img: NiimgLike | None = ...,
    inner_mesh: FilePath | SurfaceMesh | None | ndarray = ...,
    depth: Sequence[float] | None = ...,
) -> ndarray: ...

class FileMesh:
    def __init__(self, file_path: FilePath): ...
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
        left: FilePath | ndarray | None = ...,
        right: FilePath | ndarray | None = ...,
    ): ...
    def __repr__(self) -> str: ...
    @property
    def shape(self) -> tuple[int, int] | tuple[int]: ...
    def to_filename(self, filename: FilePath) -> None: ...

class PolyMesh:
    def __init__(
        self,
        left: FilePath | SurfaceMesh | None = ...,
        right: FilePath | SurfaceMesh | None = ...,
    ) -> None: ...
    def to_filename(self, filename: FilePath) -> None: ...

class SurfaceImage:
    def __init__(
        self,
        mesh: (dict[str, SurfaceMesh] | dict[str, FilePath] | PolyMesh),
        data: (dict[str, FilePath] | dict[str, ndarray] | PolyData),
    ): ...
    def __repr__(self) -> str: ...
    @classmethod
    def from_volume(
        cls,
        mesh: PolyMesh,
        volume_img: NiimgLike,
        inner_mesh: (
            dict[str, SurfaceMesh] | dict[str, FilePath] | PolyMesh | None
        ) = ...,
        **vol_to_surf_kwargs,
    ) -> SurfaceImage: ...
    @property
    def shape(self) -> tuple[int, int] | tuple[int]: ...

class SurfaceMesh:
    def __repr__(self) -> str: ...
    def to_gifti(self, gifti_file: PosixPath): ...
