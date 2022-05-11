from pathlib import Path
from enum import Enum
from typing import Final

FONTS_DIR: Final = Path(".", "text2aks", "fonts")


class Dirs(Enum):
    VAZIR_DIR = FONTS_DIR / Path("vazir")


class Fonts(Enum):
    VAZIR_BLACK = Dirs.VAZIR_DIR.value / "Vazirmatn-Black.ttf"
    VAZIR_BOLD = Dirs.VAZIR_DIR.value / "Vazirmatn-Bold.ttf"
    VAZIR_EXTRABOLD = Dirs.VAZIR_DIR.value / "Vazirmatn-ExtraBold.ttf"
    VAZIR_EXTRALIGHT = Dirs.VAZIR_DIR.value / "Vazirmatn-ExtraLight.ttf"
    VAZIR_LIGHT = Dirs.VAZIR_DIR.value / "Vazirmatn-Light.ttf"
    VAZIR_MEDIUM = Dirs.VAZIR_DIR.value / "Vazirmatn-Medium.ttf"
    VAZIR_REGULAR = Dirs.VAZIR_DIR.value / "Vazirmatn-Regular.ttf"
    VAZIR_SEMIBOLD = Dirs.VAZIR_DIR.value / "Vazirmatn-SemiBold.ttf"
    VAZIR_THIN = Dirs.VAZIR_DIR.value / "Vazirmatn-Thin.ttf"
