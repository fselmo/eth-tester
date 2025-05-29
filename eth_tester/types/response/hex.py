from typing import (
    Any,
    Callable,
)

from eth_typing import (
    HexStr,
)
from eth_utils import (
    to_hex,
)
from pydantic import (
    RootModel,
    field_validator,
)
from pydantic_core import (
    core_schema,
)


class HexStrResponse(RootModel[HexStr]):
    """
    Hex string response model.

    Validates a hex string and normalizes it to a hex string.

    Args:
        root (HexStr): The hex string.

    Returns:
        HexStr: The validated hex string.
    """

    @field_validator("root", mode="before")
    @classmethod
    def validate_and_normalize_hex_str(cls, v: Any) -> HexStr:
        return to_hex(v)
