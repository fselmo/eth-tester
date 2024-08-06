from importlib.metadata import (
    version as __version,
)

from .backends.eels.utils import (
    is_eels_available,
)

if is_eels_available():
    from .backends.eels.main import (
        EELSBackend,
    )

from .backends import (
    MockBackend,
    PyEVMBackend,
)
from .main import (
    EthereumTester,
)

__version__ = __version("eth-tester")
