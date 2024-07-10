from customtkinter import (
    CTkLabel,CTkButton,
    CTkFrame
)

from src.resources import Pallete as pallete

from src.components.images import LoaderImage as image

from src.components.menu import MenuComponent as Menu





class ScreenHeader:
    menuOn = False
    
    def __init__(self, root, page_title, widgets, actual, logo = "defender-2.png"):
        self.menu = Menu(root, widgets, actual, widgets[actual])
        self.screen = CTkFrame(root,fg_color=pallete.WHITE.value)
        self.screen.place(rely=0.04, relx=0.02, relwidth=0.96, relheight=0.14)
        self.__widgets_header(page_title, logo)
    
    def __widgets_header(self, title, logo) -> None:
        """widgets for home page"""
        self.imageDefenderApp = image.load_image(self.screen, logo,
            CTkLabel, (70,70), pallete.WHITE.value)
        self.imageDefenderApp.pack()
        
        self.menuButton = image.load_image(self.screen, "menu-button.png",
            CTkButton, (40,40), pallete.WHITE.value)
        self.menuButton.configure(hover_color=pallete.WHITE.value,
                                  command=lambda: self.__show_menu())
        self.menuButton.place(rely=0.1, relx=0)
        self.labelPage = CTkLabel(self.screen,
                                  text=title,
                                  fg_color=pallete.WHITE.value,
                                  text_color=pallete.BLACK.value,
                                  font=("Inter", 18)).\
            place(rely=0.2,relx=0.08)
        
        self.imageBanners = image.load_image(self.screen, "banners-1.png",
            CTkLabel,(36,80), pallete.WHITE.value)
        self.imageBanners.place(relx=0.97, rely=0.1)
        
    def __show_menu(self):
        """show or close menu"""
        if self.menuOn:
            self.menu.destroy_widget()
        else:
            self.menu.set_widgets()
        self.menuOn = not self.menuOn

    def __destroy_screen(self) -> None:
        """delete this screen"""
        self.screen.destroy()
