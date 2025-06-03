from nibabel.nifti1 import Nifti1Image

from nilearn._utils.tests.test_masker_validation import (
    DummyEstimator,
    OwningClass,
)
from nilearn.maskers.multi_nifti_masker import MultiNiftiMasker
from nilearn.maskers.nifti_masker import NiftiMasker
from nilearn.maskers.surface_masker import SurfaceMasker
from nilearn.surface.surface import SurfaceImage

def check_compatibility_mask_and_images(
    mask_img: SurfaceImage | None, run_imgs: SurfaceImage | list[SurfaceImage] | Nifti1Image
) -> None: ...
def check_embedded_masker(
    estimator: DummyEstimator | OwningClass, masker_type: str = ..., ignore: None = ...
) -> MultiNiftiMasker | NiftiMasker | SurfaceMasker: ...
