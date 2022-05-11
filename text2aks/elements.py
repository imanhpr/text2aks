from PIL import Image, ImageEnhance

def make_darker(image: Image.Image , value : float = 0.5) -> Image.Image:
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(value)