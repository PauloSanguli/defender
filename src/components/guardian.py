from customtkinter import (
    CTkButton, CTkLabel,
    CTkFrame, CTkImage,
    CTkEntry, END
)

from src.resources import Pallete as pallete

from src.components.header import ScreenHeader

from src.components.images import LoaderImage as image





class ScreenGuardian:
    @classmethod
    def set_screen(self, root, widgets) -> None:
        """set the screen guardian"""
        self.screen = CTkFrame(root, fg_color=pallete.WHITE.value)
        self.screen.place(relx=0,rely=0,relwidth=1.0,relheight=1.0)
        ScreenHeader(self.screen, "Guardian",widgets, "guardian","guardian-logo-1.png")
        
        self.imageGoalsGuardian = image.load_image(self.screen, "goals-guardian.png",CTkLabel,(136, 290),pallete.WHITE.value)
        self.imageGoalsGuardian.place(relx=0.03,rely=0.28)
        
        self.imageLogoGuardian = image.load_image(self.screen, "guardian-logo-2.png",CTkLabel,(90, 90),pallete.WHITE.value)
        self.imageLogoGuardian.place(relx=0.47,rely=0.28)
        
        self.labelLine = CTkLabel(self.screen, text="Guardian é  o seu guardião que vai vigiar o sem",
                                   text_color=pallete.BLACK.value,fg_color=pallete.WHITE.value).\
                                       place(relx=0.41,rely=0.44)
        self.labelLine = CTkLabel(self.screen, text="dispositivito todos os dias enquanto activado ele funciona ",
                                   text_color=pallete.BLACK.value,fg_color=pallete.WHITE.value).\
                                       place(relx=0.39,rely=0.47)
        self.labelLine = CTkLabel(self.screen, text="em segundo plano",
                                   text_color=pallete.BLACK.value,fg_color=pallete.WHITE.value).\
                                       place(relx=0.464,rely=0.5)
        
        
        self.btnActivate = CTkButton(self.screen, text="Activar",
                                    fg_color=pallete.GREEN_PRIMARY.value,
                                    text_color=pallete.GRAY.value,
                                    corner_radius=50,
                                    font=("Inter", 18),
                                    height=40,
                                    hover_color=pallete.GREEN_SECONDARY.value).\
                                        place(relx=0.52,rely=0.56)
        self.btnDeactivate = CTkLabel(self.screen, text="Desactivar",
                                    fg_color=pallete.WHITE.value,
                                    font=("Inter", 18),
                                    height=40,
                                    text_color=pallete.GRAY.value).\
                                        place(relx=0.42,rely=0.56)
        
        self.labelHead = CTkLabel(self.screen, text="Configurações guardian", fg_color=pallete.WHITE.value,
                                  text_color=pallete.BLACK.value, font=("Inter", 18)).place(rely=0.66,relx=0.05)

        self.frameConf1 = CTkFrame(self.screen, fg_color=pallete.WHITE.value, border_width=2,border_color=pallete.GRAY_SECONDARY.value)
        self.frameConf1.place(relx=0.05,rely=0.74,relwidth=0.88,relheight=0.08)
        
        self.frameConf2 = CTkFrame(self.screen, fg_color=pallete.WHITE.value, border_width=2,border_color=pallete.GRAY_SECONDARY.value)
        self.frameConf2.place(relx=0.05,rely=0.86,relwidth=0.88,relheight=0.08)
        
        self.labelInfoConf = CTkLabel(self.frameConf1,font=("Inter", 16),text="Estado", text_color=pallete.BLACK.value,fg_color=pallete.WHITE.value)
        self.labelInfoConf.place(rely=0.12,relx=0.01)
        self.labelInfoConf = CTkLabel(self.frameConf1,font=("Inter", 14),text="Active ou desative", text_color=pallete.GRAY.value,fg_color=pallete.WHITE.value)
        self.labelInfoConf.place(rely=0.5,relx=0.01)
        
        self.labelInfoConf = CTkLabel(self.frameConf2,font=("Inter", 16),text="Exceções", text_color=pallete.BLACK.value,fg_color=pallete.WHITE.value)
        self.labelInfoConf.place(rely=0.12,relx=0.01)
        self.labelInfoConf = CTkLabel(self.frameConf2,font=("Inter", 14),text="Extensões de arquivos", text_color=pallete.GRAY.value,fg_color=pallete.WHITE.value)
        self.labelInfoConf.place(rely=0.5,relx=0.01)
        
        # self.btnOnOff = image.load_image(self.frameConf1, "on.png", CTkButton, (50,20),pallete.WHITE.value).pack()
    
    @classmethod
    def destroy_widget(self):
        self.screen.destroy()