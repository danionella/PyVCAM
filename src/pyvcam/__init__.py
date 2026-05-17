"""Local fork deprecation notice for PyVCAM."""

from warnings import warn


warn(
    "This fork of PyVCAM is deprecated. Install the maintained "
    "Photometrics release from PyPI instead.",
    DeprecationWarning,
    stacklevel=2,
)
