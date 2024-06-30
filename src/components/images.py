
from PIL import Image

from assets import PATH as pathImages

import os

from customtkinter import CTkImage

from src.resources import Pallete as pallete



class LoaderImage:
    @staticmethod
    def load_image(root: any, name: str, widget: any, scale: tuple, color: str) -> any:
        """load an image file"""
        imageLogo = CTkImage(light_image=Image.open(os.path.join(pathImages, name)), dark_image=Image.open(os.path.join(pathImages, name)),size=scale)
        imageWidget = widget(
            root,image=imageLogo,
            fg_color=color,text="")
        return imageWidget