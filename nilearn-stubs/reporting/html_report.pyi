from string import Template

class HTMLReport:
    def __init__(
        self,
        head_tpl: Template,
        body: str,
        head_values: dict[str, str] | None = ...,
    ): ...
    def __str__(self) -> str: ...
    def _repr_html_(self) -> str: ...
