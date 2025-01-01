"""Helper functions to download NeuroImaging datasets."""

from nilearn.datasets.atlas import (
    fetch_atlas_aal,
    fetch_atlas_allen_2011,
    fetch_atlas_basc_multiscale_2015,
    fetch_atlas_craddock_2012,
    fetch_atlas_destrieux_2009,
    fetch_atlas_difumo,
    fetch_atlas_harvard_oxford,
    fetch_atlas_juelich,
    fetch_atlas_msdl,
    fetch_atlas_pauli_2017,
    fetch_atlas_schaefer_2018,
    fetch_atlas_smith_2009,
    fetch_atlas_surf_destrieux,
    fetch_atlas_talairach,
    fetch_atlas_yeo_2011,
    fetch_coords_dosenbach_2010,
    fetch_coords_power_2011,
    fetch_coords_seitzman_2018,
)
from nilearn.datasets.func import (
    fetch_abide_pcp,
    fetch_adhd,
    fetch_bids_langloc_dataset,
    fetch_development_fmri,
    fetch_ds000030_urls,
    fetch_fiac_first_level,
    fetch_haxby,
    fetch_language_localizer_demo_dataset,
    fetch_localizer_button_task,
    fetch_localizer_calculation_task,
    fetch_localizer_contrasts,
    fetch_localizer_first_level,
    fetch_megatrawls_netmats,
    fetch_mixed_gambles,
    fetch_miyawaki2008,
    fetch_openneuro_dataset,
    fetch_spm_auditory,
    fetch_spm_multimodal_fmri,
    fetch_surf_nki_enhanced,
    load_nki,
    load_sample_motor_activation_image,
    patch_openneuro_dataset,
    select_from_index,
)
from nilearn.datasets.neurovault import (
    fetch_neurovault,
    fetch_neurovault_auditory_computation_task,
    fetch_neurovault_ids,
    fetch_neurovault_motor_task,
)
from nilearn.datasets.struct import (
    GM_MNI152_FILE_PATH,
    MNI152_FILE_PATH,
    WM_MNI152_FILE_PATH,
    fetch_icbm152_2009,
    fetch_icbm152_brain_gm_mask,
    fetch_oasis_vbm,
    fetch_surf_fsaverage,
    load_fsaverage,
    load_fsaverage_data,
    load_mni152_brain_mask,
    load_mni152_gm_mask,
    load_mni152_gm_template,
    load_mni152_template,
    load_mni152_wm_mask,
    load_mni152_wm_template,
)
from nilearn.datasets.utils import get_data_dirs

__all__ = [
    "GM_MNI152_FILE_PATH",
    "MNI152_FILE_PATH",
    "WM_MNI152_FILE_PATH",
    "fetch_abide_pcp",
    "fetch_adhd",
    "fetch_atlas_aal",
    "fetch_atlas_allen_2011",
    "fetch_atlas_basc_multiscale_2015",
    "fetch_atlas_craddock_2012",
    "fetch_atlas_destrieux_2009",
    "fetch_atlas_difumo",
    "fetch_atlas_harvard_oxford",
    "fetch_atlas_juelich",
    "fetch_atlas_msdl",
    "fetch_atlas_pauli_2017",
    "fetch_atlas_schaefer_2018",
    "fetch_atlas_smith_2009",
    "fetch_atlas_surf_destrieux",
    "fetch_atlas_talairach",
    "fetch_atlas_yeo_2011",
    "fetch_bids_langloc_dataset",
    "fetch_coords_dosenbach_2010",
    "fetch_coords_power_2011",
    "fetch_coords_seitzman_2018",
    "fetch_development_fmri",
    "fetch_ds000030_urls",
    "fetch_fiac_first_level",
    "fetch_haxby",
    "fetch_icbm152_2009",
    "fetch_icbm152_brain_gm_mask",
    "fetch_language_localizer_demo_dataset",
    "fetch_localizer_button_task",
    "fetch_localizer_calculation_task",
    "fetch_localizer_contrasts",
    "fetch_localizer_first_level",
    "fetch_megatrawls_netmats",
    "fetch_mixed_gambles",
    "fetch_miyawaki2008",
    "fetch_neurovault",
    "fetch_neurovault_auditory_computation_task",
    "fetch_neurovault_ids",
    "fetch_neurovault_motor_task",
    "fetch_oasis_vbm",
    "fetch_openneuro_dataset",
    "fetch_spm_auditory",
    "fetch_spm_multimodal_fmri",
    "fetch_surf_fsaverage",
    "fetch_surf_nki_enhanced",
    "get_data_dirs",
    "load_fsaverage",
    "load_fsaverage_data",
    "load_mni152_brain_mask",
    "load_mni152_gm_mask",
    "load_mni152_gm_template",
    "load_mni152_template",
    "load_mni152_wm_mask",
    "load_mni152_wm_template",
    "load_nki",
    "load_sample_motor_activation_image",
    "patch_openneuro_dataset",
    "select_from_index",
]
