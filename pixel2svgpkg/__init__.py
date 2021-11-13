import sys
from pathlib import Path
from typing import Union

from .utils import open_image, prepare_svg, save_svg

if sys.version_info[:2] >= (3, 8):
    import importlib.metadata as importlib_metadata
else:
    import importlib_metadata

__version__ = importlib_metadata.version(__name__)


def get_svg(
    input_path: Union[str, Path], output_pretty: bool = False, output_indent: int = 2
) -> None:
    save_svg(
        prepare_svg(input_path, open_image(input_path)),
        output_pretty=output_pretty,
        output_indent=output_indent,
    )
