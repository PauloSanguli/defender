from customtkinter import (
    CTkButton, CTkLabel,
    CTkFrame, CTkImage, CTkEntry
)

from src.components.images import LoaderImage as image

from src.resources import Pallete as pallete

from src.components.header import ScreenHeader

from src.components.mask import ScreenMask

from feats import linkValidator



class ScreenFixing:

    @classmethod
    def set_screen(self, root, widgets):
        """set up the screen for fixing"""
        self.screen = CTkFrame(widgets["root"], fg_color=pallete.WHITE.value)
        self.screen.place(rely=0,relx=0,relwidth=1.0,relheight=1.0)
        header = ScreenHeader(self.screen, "Fixing", widgets, "fixing")

        self.labelIntro = CTkLabel(self.screen, text="Insira o link a baixo", font=("Inter", 18),text_color=pallete.BLACK.value).\
            place(relx=0.058, rely=0.23)

        self.linkEntry = CTkEntry(self.screen, border_width=1,border_color=pallete.GRAY.value,text_color=pallete.BLACK.value,fg_color=pallete.WHITE.value)
        self.linkEntry.place(rely=0.3,relx=0.058,relwidth=0.6,relheight=0.06)

        self.buttonFix = CTkButton(self.screen, text="Analisar link", command=lambda: self.validate_link(),border_color=pallete.GRAY_SECONDARY.value,border_width=1, hover_color=pallete.GREEN_PRIMARY.value, fg_color=pallete.GREEN_PRIMARY.value,text_color=pallete.BLACK.value).\
            place(relheight=0.06,relwidth=0.2,relx=0.7,rely=0.3)

        self.frameResult = CTkFrame(self.screen, fg_color=pallete.WHITE.value, border_color=pallete.GRAY.value, border_width=2)
        self.frameResult.place(relx=0.058,relheight=0.4,rely=0.4, relwidth=0.85)

        self.textResultLabel = CTkLabel(self.screen, text="O resultado aparecerá aqui", font=("Inter", 18),fg_color=pallete.WHITE.value,text_color=pallete.BLACK.value)
        self.textResultLabel.place(relx=0.45,rely=0.57) 

        self.labelIntroFoot = CTkLabel(self.screen, text="Examplo de link: https://www.google.com/", font=("Inter", 18),text_color=pallete.GRAY.value).\
            place(relx=0.058, rely=0.84)
    
    @classmethod
    def validate_link(self) -> None:
        """validate the link"""
        RESPONSE_VERIFY, MSG = linkValidator(self.linkEntry.get())
        if RESPONSE_VERIFY:
            self.textResultLabel.configure(text=MSG)
            self.frameResult.configure(border_color=pallete.GRAY_SECONDARY.value)
        else:
            self.frameResult.configure(border_color=pallete.RED.value)
            self.textResultLabel.configure(text="Link inválido",text_color=pallete.RED.value)
    
    @classmethod
    def destroy_widget(self):
        self.screen.destroy()
    