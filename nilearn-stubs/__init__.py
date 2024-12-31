try:
    from ._version import __version__
except ImportError:
    __version__ = "0+unknown"

# list all submodules available in nilearn and version
__all__ = [
    "__version__",
    "connectome",
    "datasets",
    "decoding",
    "decomposition",
    "image",
    "interfaces",
    "maskers",
    "masking",
    "mass_univariate",
    "plotting",
    "regions",
    "signal",
    "surface",
]
