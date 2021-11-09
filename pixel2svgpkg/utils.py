from pathlib import Path
from typing import List, Tuple, Union

import svgwrite
from PIL import Image

from .constants import DEFAULT_SQUARE_SIZE


# Source: https://stackoverflow.com/a/58541858
def open_image(
    input_path: Union[str, Path]
) -> Tuple[int, int, List[Tuple[int, int, int]]]:
    # More info:
    # - https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open
    # - https://pillow.readthedocs.io/en/stable/reference/Image.html#open-rotate-and-display-an-image-using-the-default-viewer
    # - https://pillow.readthedocs.io/en/stable/handbook/concepts.html#modes
    # - https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.convert
    # - https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.getdata
    with Image.open(input_path) as im:
        # print(im.mode)
        im = im.convert("RGBA")

        (width, height) = im.size
        # print(width, height, type(width), type(height))

        rgb_values = list(im.getdata())

    return width, height, rgb_values


def prepare_svg(input_path, width, height, rgb_values):
    # More info:
    # - https://svgwrite.readthedocs.io/en/latest/classes/drawing.html#svgwrite.drawing.Drawing
    filename = "TODO.svg"

    svg = svgwrite.Drawing(
        filename=filename,
        size=(f"{width * DEFAULT_SQUARE_SIZE}px", f"{height * DEFAULT_SQUARE_SIZE}px"),
    )

    return svg
