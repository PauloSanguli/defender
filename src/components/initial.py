from customtkinter import (
    CTkFrame,CTkLabel, CTkButton
)

from src.components.images import LoaderImage as image

from src.resources import Pallete as pallete

from src.components.home import ScreenHome


class ScreenInitial:
    def __init__(self, root, scan, guardian, fixing):
        self.root = root
        self.scan = scan
        self.fixing = fixing
        self.guardian = guardian
        self.screen = CTkFrame(root)
        self.__position_frame()
        self.__widgets_inital()
    
    
    def __position_frame(self) -> None:
        """set position of frame"""
        self.screen.pack(fill="both", expand=True)
    
    
    def __widgets_inital(self) -> None:
        """"widgets for frame initial"""
        self.imageLogoButton = image.load_image(self.screen,"defender-1.png", CTkButton, (110,110), pallete.GREEN_PRIMARY.value)
        self.imageLogoButton.configure(hover_color=pallete.GREEN_PRIMARY.value,
            command=self.destroy_screen)
        self.imageLogoButton.pack(fill="both", expand=True, padx=1, pady=0)
        
        self.imageWave = image.load_image(
            self.screen,"wave-1.png",
            CTkLabel,(self.root.winfo_screenwidth(), 100), pallete.GREEN_PRIMARY.value)
        self.imageWave.pack()
        
        self.screen.after(5000, self.destroy_screen)


    def destroy_screen(self):
        """deatroy the frame"""
        self.screen.destroy()
        homePage = ScreenHome(self.root, self.scan, self.guardian, self.fixing)
