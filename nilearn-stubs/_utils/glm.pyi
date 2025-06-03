from typing import (
    Any,
)

from numpy import ndarray
from pandas.core.frame import DataFrame

def _read_events_table(table_path: str): ...
def check_and_load_tables(tables_to_check: list[str | DataFrame], var_name: str): ...
def coerce_to_dict(input_arg: Any) -> dict[str, ndarray] | dict[str, list[int]] | dict[str, str] | None: ...
