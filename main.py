import json
from typing import Union

import requests

import docstring

INDENT = 4


def main():
    """Описание"""
    print(print_json_string([1, 2, 3]))


def print_json_string(obj: Union[list, dict]) -> str:
    """Описание"""
    return json.dumps(obj, indent=INDENT)


if __name__ == '__main__':
    main()
    print(main.__name__)
    print(main.__doc__)
