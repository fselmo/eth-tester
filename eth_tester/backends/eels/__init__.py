from .utils import (
    is_eels_available,
)

if is_eels_available():
    from .main import (
        EELSBackend,
    )
