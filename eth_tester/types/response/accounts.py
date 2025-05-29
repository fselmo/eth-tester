from typing import (
    List,
)

from eth_typing import (
    ChecksumAddress,
)
from eth_utils import (
    to_checksum_address,
)
from pydantic import (
    RootModel,
    field_validator,
)

from eth_tester.validation.outbound import (
    validate_accounts,
)


class ChecksumAddressesResponse(RootModel[List[ChecksumAddress]]):
    """
    Checksum addresses response model.

    Validates a list of canonical addresses and normalizes them to checksum addresses.

    Args:
        root: (List[ChecksumAddress]): The list of canonical addresses.

    Returns:
        List[ChecksumAddress]: The list of validated checksum addresses.
    """

    @field_validator("root", mode="before")
    @classmethod
    def validate_and_normalize_addresses(cls, v: List[bytes]) -> List[ChecksumAddress]:
        validate_accounts(v)
        return [to_checksum_address(address) for address in v]
