from dataclasses import fields, is_dataclass, MISSING
from typing import Any

def to_filtered_dict(obj: Any, skip_none: bool = True, skip_defaults: bool = True) -> Any:
    """
    Convert a dataclass object (or nested list/dict) to a dict,
    excluding fields that are None or match their declared default.
    """
    # If it's a list/tuple, recursively process each element
    if isinstance(obj, (list, tuple)):
        return [to_filtered_dict(item, skip_none, skip_defaults) for item in obj if item is not None or not skip_none]

    # If it's a dict, recursively process each value
    if isinstance(obj, dict):
        result = {}
        for k, v in obj.items():
            if v is None and skip_none:
                continue
            result[k] = to_filtered_dict(v, skip_none, skip_defaults)
        return result

    # If it's another dataclass, handle its fields
    if is_dataclass(obj):
        result = {}
        for field_ in fields(obj):
            value = getattr(obj, field_.name)

            # If skip_none=True and the value is None, ignore this field.
            if skip_none and value is None:
                continue

            # If skip_defaults=True, skip the field if it matches its default value.
            # (Note: If default is MISSING, it means no default was specified.)
            # This also means we skip fields that haven’t been set to anything but their default.
            has_default = field_.default is not MISSING or field_.default_factory is not MISSING
            if skip_defaults and has_default:
                default_val = field_.default
                # If there's a default_factory instead of a default, 
                # we can call it to see what it returns, though that’s optional.
                # field_.default_factory is also not MISSING if we had a factory.
                if field_.default_factory is not MISSING:
                    default_val = field_.default_factory()

                if value == default_val:
                    continue

            # Recursively convert the value
            result[field_.name] = to_filtered_dict(value, skip_none, skip_defaults)
        return result

    # The base case -> If it's just a primitive (str, float, bool, etc.), return as-is
    return obj