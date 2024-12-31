"""Analyzing fMRI data using GLMs."""

from nilearn_stubs.glm import first_level, second_level
from nilearn_stubs.glm.contrasts import (
    Contrast,
    compute_contrast,
    compute_fixed_effects,
    expression_to_contrast_vector,
)
from nilearn_stubs.glm.model import (
    FContrastResults,
    LikelihoodModelResults,
    TContrastResults,
)
from nilearn_stubs.glm.regression import (
    ARModel,
    OLSModel,
    RegressionResults,
    SimpleRegressionResults,
)
from nilearn_stubs.glm.thresholding import (
    cluster_level_inference,
    fdr_threshold,
    threshold_stats_img,
)

__all__ = [
    "ARModel",
    "Contrast",
    "FContrastResults",
    "LikelihoodModelResults",
    "OLSModel",
    "RegressionResults",
    "SimpleRegressionResults",
    "TContrastResults",
    "cluster_level_inference",
    "compute_contrast",
    "compute_fixed_effects",
    "expression_to_contrast_vector",
    "fdr_threshold",
    "first_level",
    "second_level",
    "threshold_stats_img",
]
