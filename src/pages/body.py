import customtkinter as ctk
from src.resources import Pallete as pallete




class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.config(background=pallete.GREEN_PRIMARY.value)
        self.__Geometry()
        self.state("zoomed")
    
    def __Geometry(self) -> None:
        """scale of window"""
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")
        self.resizable(False, False)
