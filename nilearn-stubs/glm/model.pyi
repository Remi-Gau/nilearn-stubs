from numpy import float64, int64, ndarray

from nilearn.glm.regression import ARModel, OLSModel

class FContrastResults:
    def __init__(
        self,
        effect: ndarray,
        covariance: ndarray,
        F: float64 | ndarray,
        df_num: int,
        df_den: int64 | None = ...,
    ): ...

class LikelihoodModelResults:
    def Fcontrast(
        self,
        matrix: list[int] | ndarray,
        dispersion: None = ...,
        invcov: None = ...,
    ) -> FContrastResults: ...
    def Tcontrast(
        self,
        matrix: list[int] | ndarray,
        store: tuple[str] | tuple[str, str, str] | tuple[str, str] = ...,
        dispersion: None = ...,
    ) -> TContrastResults: ...
    def __init__(
        self,
        theta: ndarray,
        Y: ndarray,
        model: OLSModel | ARModel,
        cov: ndarray | None = ...,
        dispersion: float64 | ndarray = ...,
        nuisance: None = ...,
    ): ...
    def conf_int(
        self,
        alpha: float = ...,
        cols: tuple[int, int] | list[int] | None = ...,
        dispersion: None = ...,
    ) -> ndarray: ...
    def t(self, column: int | None = ...) -> float64: ...
    def vcov(
        self,
        matrix: ndarray | None = ...,
        column: int | ndarray | None = ...,
        dispersion: float | ndarray | None = ...,
        other: None = ...,
    ) -> float64 | ndarray: ...

class TContrastResults:
    def __init__(
        self,
        t: ndarray | None,
        sd: ndarray | None,
        effect: ndarray | None,
        df_den: int64 | None = ...,
    ): ...
