from numpy import ndarray
from pandas.core.frame import DataFrame

def load_confounds_strategy(
    img_files: str, denoise_strategy: str = ..., **kwargs
) -> tuple[DataFrame, ndarray]: ...
