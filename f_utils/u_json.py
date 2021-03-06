import json


def to_dict(str_json):
    """
    ============================================================================
     Description: Convert JSON-str into Dictionary.
    ============================================================================
     Arguments:
    ----------------------------------------------------------------------------
        1: str_json : str
    ============================================================================
     Return: dict
    ============================================================================
    """
    return json.loads(str_json)