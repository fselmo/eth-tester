from typing import (
    Any,
    Dict,
)

from eth_tester.utils.casing import (
    snake_case_to_lower_camel_case,
)


def eels_normalize_transaction(transaction: Dict[str, Any]) -> Dict[str, Any]:
    normalized = {}
    for key, value in transaction.items():
        if key == "gas":
            key = "gas_limit"
        elif key in ("to", "from", "data", "y_parity", "r", "s", "v"):
            value = value.hex()

        if isinstance(value, int):
            value = hex(value)

        if key in ("y_parity",):
            # for some reason, y_parity is not camelCased :/
            normalized[key] = value
        else:
            normalized[snake_case_to_lower_camel_case(key)] = value

    return normalized