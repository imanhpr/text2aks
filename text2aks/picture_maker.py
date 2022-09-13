import textwrap
from typing import Literal

from PIL import Image, ImageDraw, ImageFont

from .fonts_data import Fonts
from .interfaces import Text2Image


class Text2Aks(Text2Image):
    Stroke = (0, 0, 0)

    def __init__(self, image: Image.Image, font: Fonts, font_size=int) -> None:
        self._image = image.resize((1080, 1080))
        font_path = font.value.absolute()
        self._font = ImageFont.truetype(str(font_path), font_size, encoding="utf-8")

    @property
    def image(self):
        return self._image

    @property
    def text(self):
        return self._text

    def genrate(
        self,
        text: str,
        writer: str,
        dir: Literal["rtl", "ltr"] = "rtl",
        wraper_wid: int = 45,
        line_space : int = 5
    ):
        draw = ImageDraw.Draw(self._image)
        image_w, image_h = self._image.size
        raw_text = textwrap.wrap(text, wraper_wid)
        if len(raw_text) == 1:
            text_w, text_h = draw.textsize(
                text, self._font, direction=dir, stroke_width=3
            )
            draw.text(
                xy=((image_w - text_w) / 2, (image_h - text_h) / 2),
                font=self._font,
                text=text,
                stroke_fill="black",
                stroke_width=3,
                direction=dir,
                align="center",
            )
        else:
            paragraph = "\n".join(raw_text)
            text_w, text_h = draw.textsize(
                paragraph, self._font, direction=dir, stroke_width=3
            )
            if isinstance(line_space , int):
                text_h += line_space
            draw.multiline_text(
                xy=((image_w - text_w) / 2, (image_h - text_h) / 2),
                font=self._font,
                text=paragraph,
                stroke_fill="black",
                stroke_width=3,
                direction=dir,
                align="center",
                spacing=line_space
            )
        writer_w, _ = draw.textsize(
                writer, self._font, direction=dir, stroke_width=3
            )
        draw.text(
                xy=((image_w - writer_w) / 2, 950),
                font=self._font,
                text=writer,
                stroke_fill="black",
                stroke_width=3,
                direction=dir,
                align="center",
            )

    def resault(self):
        return self._image
