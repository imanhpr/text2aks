![license](https://img.shields.io/github/license/imanhpr/text2aks?style=for-the-badge) ![enter image description here](https://img.shields.io/github/commit-activity/m/imanhpr/text2aks?style=for-the-badge)

# Text2Aks
**This project is under active development and anything can change in the future**

### What is text2aks ?
**Text2Aks** is a simple library that can generate simple pictures with text input.
### How dose it work ?
***You have to have [Pillow](https://pillow.readthedocs.io/en/stable/) installed on your system.***
In the below example I will show you how can you genrate image with text2aks
```python
from text2aks import Text2Aks, Fonts
from text2aks.elements import make_darker
from PIL import Image

my_image = 'path to my image'
text : str = "Nothing is more difficult, and therefore more precious, than to be able to decide"
wrtier_of_text : str = 'Napoleon Bonaparte'

with Image.open(my_image) as raw_image :
    darker_image = make_darker(raw_image)
    image_maker = Text2Aks(darker_image , Fonts.VAZIR_BOLD , font_size=50)
    image_maker.genrate(text , wrtier_of_text , 'ltr') # left ro right (ltr) | right to left (rtl)
    result : Image.Image = image_maker.resault()
    # If you want to save it in your file system you can use save method of Image class
    # or if you want just takes a look at it you can use show method.
    # result.save('name of new image , 'JPEG')
    # result.show()
```
![Result image](https://user-images.githubusercontent.com/56130647/168424164-0c3089cc-5793-4093-8675-a3315fdd9eea.jpg)
![enter image description here](https://user-images.githubusercontent.com/56130647/168424324-95aa680b-40a6-4c67-b8f7-a7a6012d0201.jpg)

You can find all available fonts for this project in the ```fonts_data``` moduel
***The only available font in this version of the project, is [Vazir](https://github.com/rastikerdar/vazirmatn) font. it's an open-source and free font that you can use it in your projects.***

You can use different weights of it in this project :
```python
from text2aks.fonts_data import  Fonts

Fonts.VAZIR_BLACK  # "Vazirmatn-Black.ttf"
Fonts.VAZIR_BOLD  # "Vazirmatn-Bold.ttf"
Fonts.VAZIR_EXTRABOLD  # "Vazirmatn-ExtraBold.ttf"
Fonts.VAZIR_EXTRALIGHT  # "Vazirmatn-ExtraLight.ttf"
Fonts.VAZIR_LIGHT  # "Vazirmatn-Light.ttf"
Fonts.VAZIR_MEDIUM  # "Vazirmatn-Medium.ttf"
Fonts.VAZIR_REGULAR  # "Vazirmatn-Regular.ttf"
Fonts.VAZIR_SEMIBOLD  # "Vazirmatn-SemiBold.ttf"
Fonts.VAZIR_THIN  # "Vazirmatn-Thin.ttf"

```

## LICENSE
```
MIT License

Copyright (c) 2022 Iman Hosseini Pour

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```