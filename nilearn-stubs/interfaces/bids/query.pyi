from pathlib import PosixPath

def get_bids_files(
    main_path: PosixPath,
    file_tag: str = ...,
    file_type: str = ...,
    sub_label: str = ...,
    modality_folder: str = ...,
    filters: list[tuple[str, str]] | None = ...,
    sub_folder: bool = ...,
) -> list[str]: ...
def parse_bids_filename(
    img_path: PosixPath | str,
) -> dict[str, PosixPath | str | list[str]]: ...
