from pathlib import Path
from typing import Union

import svgwrite
from PIL import Image

from .constants import DEFAULT_SQUARE_SIZE, RGBImage


# Source: https://stackoverflow.com/a/58541858
def open_image(input_path: Union[str, Path]) -> RGBImage:
    # More info:
    # - https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open
    # - https://pillow.readthedocs.io/en/stable/reference/Image.html#open-rotate-and-display-an-image-using-the-default-viewer  # noqa: E501
    # - https://pillow.readthedocs.io/en/stable/handbook/concepts.html#modes
    # - https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.convert  # noqa: E501
    # - https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.getdata  # noqa: E501
    with Image.open(input_path) as im:
        # print(im.mode)
        im = im.convert("RGBA")

        (width, height) = im.size
        # print(width, height, type(width), type(height))

        rgb_values = list(im.getdata())

    return RGBImage(width, height, rgb_values)


def prepare_svg(input_path: Union[str, Path], image: RGBImage) -> svgwrite.Drawing:
    # More info: https://svgwrite.readthedocs.io/en/latest/classes/drawing.html#svgwrite.drawing.Drawing  # noqa: E501
    filename = Path(input_path).resolve(strict=True).with_suffix(".svg")

    svg = svgwrite.Drawing(
        filename=filename,
        size=(
            f"{image.width * DEFAULT_SQUARE_SIZE}px",
            f"{image.height * DEFAULT_SQUARE_SIZE}px",
        ),
    )

    rect_size = (f"{DEFAULT_SQUARE_SIZE}px", f"{DEFAULT_SQUARE_SIZE}px")

    row_count = 0
    while row_count < image.height:
        col_count = 0

        while col_count < image.width:
            rgb_tuple_index = row_count * image.height + col_count
            # print(rgb_tuple_index)
            rgb_tuple = image.values[rgb_tuple_index]

            # Ignore transparent pixels.
            if rgb_tuple[3] > 0:
                rect_pos = (
                    f"{col_count * DEFAULT_SQUARE_SIZE}px",
                    f"{row_count * DEFAULT_SQUARE_SIZE}px",
                )

                rect_fill = svgwrite.rgb(rgb_tuple[0], rgb_tuple[1], rgb_tuple[2])
                alpha = rgb_tuple[3]

                # Source: https://github.com/cyChop/pixel2svg-fork/blob/master/pixel2svg.py#L102  # noqa: E501
                if alpha == 255:
                    svg.add(
                        svg.rect(
                            insert=rect_pos,
                            size=rect_size,
                            fill=rect_fill,
                        )
                    )
                else:
                    svg.add(
                        svg.rect(
                            insert=rect_pos,
                            size=rect_size,
                            fill=rect_fill,
                            opacity=alpha / 255.0,
                        )
                    )

            col_count += 1

        row_count += 1

    return svg


def save_svg(
    svg: svgwrite.Drawing, output_pretty: bool = False, output_indent: int = 2
) -> None:
    svg.save(pretty=output_pretty, indent=output_indent)
