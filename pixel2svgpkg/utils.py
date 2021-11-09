from pathlib import Path
from typing import Union

import svgwrite
from PIL import Image

from .constants import DEFAULT_SQUARE_SIZE, RGBImage


# Source: https://stackoverflow.com/a/58541858
def open_image(input_path: Union[str, Path]) -> RGBImage:
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

    return RGBImage(width, height, rgb_values)


def prepare_svg(input_path: Union[str, Path], image: RGBImage) -> svgwrite.Drawing:
    # More info:
    # - https://svgwrite.readthedocs.io/en/latest/classes/drawing.html#svgwrite.drawing.Drawing
    filename = Path(input_path).resolve(strict=True).with_suffix(".svg")

    svg = svgwrite.Drawing(
        filename=filename,
        size=(
            f"{image.width * DEFAULT_SQUARE_SIZE}px",
            f"{image.height * DEFAULT_SQUARE_SIZE}px",
        ),
    )

    row_count = 0
    while row_count < image.height:
        col_count = 0

        while col_count < image.width:
            col_count += 1

        row_count += 1

    return svg
