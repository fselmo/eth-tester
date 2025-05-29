from typing import (
    Any,
    Callable,
)

from eth_utils import (
    to_canonical_address,
)
from pydantic_core import (
    core_schema,
)

from eth_tester.validation.inbound import (
    validate_account,
)


class CanonicalAddress(bytes):
    """
    Canonical address type.

    This type is used to validate and normalize canonical addresses.

    Canonical addresses are the raw bytes of an address.

    Args:
        address (ChecksumAddress): The hex string representation of an address.

    Returns:
        CanonicalAddress: The validated canonical address.
    """

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source_type: Any, handler: Callable[[Any], bytes]
    ) -> core_schema.CoreSchema:
        def validate_and_normalize_address(v: bytes) -> bytes:
            validate_account(v)
            return to_canonical_address(v)

        return core_schema.no_info_plain_validator_function(
            validate_and_normalize_address
        )
