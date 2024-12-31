from pathlib import PosixPath

from pandas.core.frame import DataFrame

def get_design_from_fslmat(
    fsl_design_matrix_path: PosixPath, column_names: None = ...
) -> DataFrame: ...
