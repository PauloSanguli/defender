from customtkinter import (
    CTkButton, CTkLabel,
    CTkFrame, CTkImage
)

from src.components.images import LoaderImage as image

from src.resources import Pallete as pallete

from src.components.header import ScreenHeader

from src.components.mask import ScreenMask

# from src.components.guardian import ScreenGuardian


class ScreenHome:
    # def __init__(self, root, scan, guardian, fixing):
    @classmethod
    def set_screen(self, root, scan, guardian, fixing):
        self.root = root
        self.scan = scan
        self.mask = ScreenMask()
        self.fixing = fixing
        self.guardian = guardian
        # self.root.configure(background="white")
        self.screen = CTkFrame(root, fg_color=pallete.WHITE.value)
        self.__position_frame()
        self.__widgets_home()
        
    @classmethod
    def __position_frame(self) -> None:
        """set position of frame"""
        self.screen.pack(fill="both", expand=True)
    
    @classmethod
    def __widgets_home(self):
        """"widgets for frame initial"""
        self.migrate_widgets()
        self.scan.WIDGETS = self.widgets_migration
        header = ScreenHeader(self.screen, "Home", self.widgets_migration, "home")
        # self.frameInfo = CTkFrame(self.screen,fg_color=pallete.RED.value)
        # self.frameInfo.place(rely=0.3, relx=0.02, relwidth=0.96, relheight=0.14)

        self.labelMinInfo = image.load_image(self.screen, "label-info-1.png",
            CTkLabel, (90, 28), pallete.WHITE.value)
        self.labelMinInfo.place(relx=0.05, rely=0.2)
        
        self.labelSecondInfo = CTkLabel(self.screen, text="Selecione a sua opção",
            fg_color=pallete.WHITE.value, font=("Inter", 18),text_color=pallete.BLACK.value)
        self.labelSecondInfo.place(relx=0.05, rely=0.25)
        self.imageRay = image.load_image(self.screen, "ray.png", CTkLabel
            ,(80, 50), pallete.WHITE.value)
        self.imageRay.place(relx=0.2, rely=0.23)
        
        self.ImageCardsActions = image.load_image(self.screen,"cards.png",
            CTkLabel, (660, 180), pallete.WHITE.value)
        self.ImageCardsActions.place(rely=0.36,relx=0.05)
        
        self.ImageGoals = image.load_image(self.screen,"goals.png",
            CTkLabel, (136, 290), pallete.WHITE.value)
        self.ImageGoals.place(rely=0.28,relx=0.8)
        
        self.buttonScanComputer = CTkButton(self.screen,
            text="Scanear computador",fg_color=pallete.GREEN_PRIMARY.value,
            corner_radius=50, text_color=pallete.BLACK.value, width=150, hover_color=pallete.GREEN_SECONDARY.value,
            command=lambda: self.redirect_screen("device"))
        self.buttonScanComputer.place(rely=0.54, relx=0.07)
        
        self.buttonScanDirectory = CTkButton(self.screen,
            text="Scanear directório",fg_color=pallete.GREEN_PRIMARY.value,
            corner_radius=50, text_color=pallete.BLACK.value, width=150, hover_color=pallete.GREEN_SECONDARY.value,
            command=lambda: self.redirect_screen())
        self.buttonScanDirectory.place(rely=0.56, relx=0.22)
        
        self.buttonScanUSB = CTkButton(self.screen,
            text="Scanear USB",fg_color=pallete.GREEN_PRIMARY.value,
            corner_radius=50, text_color=pallete.BLACK.value, width=150, hover_color=pallete.GREEN_SECONDARY.value,
            command=lambda: self.redirect_screen("usb"))
        self.buttonScanUSB.place(rely=0.54, relx=0.36)
        
        self.imageWave = image.load_image(self.screen, "wave-2.png", CTkLabel,
            (self.root.winfo_screenwidth(), 100), pallete.WHITE.value)
        self.imageWave.place(rely=0.86,relx=0)
        
        self.labelInfoGuardian = CTkLabel(self.screen, text="Podes activar o Guardian",
            fg_color=pallete.WHITE.value, font=("Inter", 18, "normal"),text_color=pallete.BLACK.value)
        self.labelInfoGuardian.place(relx=0.05, rely=0.66)
        
        self.buttonAtivateGuardian = CTkButton(self.screen,
            text="Activar agora",fg_color=pallete.GREEN_PRIMARY.value,
            corner_radius=50, text_color=pallete.BLACK.value, hover_color=pallete.GREEN_SECONDARY.value,
            width=140, height=30, command=lambda: self.redirect_screen("guardian"))
        self.buttonAtivateGuardian.place(rely=0.82, relx=0.05)
        
        self.labelInfoGuardianText = CTkLabel(self.screen, text="Guardian é uma ferramenta que serve para monitorar o computador",
            fg_color=pallete.WHITE.value, width=50,font=("Inter", 13, "normal"),text_color=pallete.BLACK.value)
        self.labelInfoGuardianText.place(relx=0.05, rely=0.7)
        
        self.labelInfoGuardianText = CTkLabel(self.screen, text="Melhore a segurança e integridade dos seus dados com o GUardian",
            fg_color=pallete.WHITE.value, width=50,font=("Inter", 13, "normal"),text_color=pallete.BLACK.value)
        self.labelInfoGuardianText.place(relx=0.05, rely=0.73)
        
        self.labelInfoGuardianTextSecond = CTkLabel(self.screen, text="para proteger de ameaças ao sistema",
            fg_color=pallete.WHITE.value, width=50,font=("Inter", 13, "normal"),text_color=pallete.BLACK.value)
        self.labelInfoGuardianTextSecond.place(relx=0.05, rely=0.76)
        
        # goals 
        self.labelInfoGoals = CTkLabel(self.screen, text="Os seus registros",
            fg_color=pallete.WHITE.value, width=50,font=("Inter", 18),text_color=pallete.BLACK.value)
        self.labelInfoGoals.place(relx=0.8, rely=0.2)
        
        self.labelInfoGoalsComputer = CTkLabel(self.screen, text="Computador",
            fg_color=pallete.WHITE.value, width=50,font=("Inter", 13, "normal"), height=10,text_color=pallete.BLACK.value)
        self.labelInfoGoalsComputer.place(relx=0.89, rely=0.3)
        self.labelInfoGoalsComputerNum = CTkLabel(self.screen, text="120 recentes",
            fg_color=pallete.WHITE.value, width=50,font=("Inter", 10, "normal"), height=10,text_color=pallete.BLACK.value)
        self.labelInfoGoalsComputerNum.place(relx=0.89, rely=0.324)
        
        self.labelInfoGoalsDir = CTkLabel(self.screen, text="Directório",
            fg_color=pallete.WHITE.value, width=50,font=("Inter", 13, "normal"), height=10,text_color=pallete.BLACK.value)
        self.labelInfoGoalsDir.place(relx=0.9, rely=0.44)
        self.labelInfoGoalsDirNum = CTkLabel(self.screen, text="120 recentes",
            fg_color=pallete.WHITE.value, width=50,font=("Inter", 10, "normal"), height=10,text_color=pallete.BLACK.value)
        self.labelInfoGoalsDirNum.place(relx=0.9, rely=0.462)
        
        self.labelInfoGoalsUSB = CTkLabel(self.screen, text="USB",
            fg_color=pallete.WHITE.value, width=50,font=("Inter", 13, "normal"), height=10,text_color=pallete.BLACK.value)
        self.labelInfoGoalsUSB.place(relx=0.78, rely=0.58)
        self.labelInfoGoalsUSBNum = CTkLabel(self.screen, text="120 recentes",
            fg_color=pallete.WHITE.value, width=50,font=("Inter", 10, "normal"), height=10,text_color=pallete.BLACK.value)
        self.labelInfoGoalsUSBNum.place(relx=0.77, rely=0.6)
        
        self.imageRocket = image.load_image(self.screen, "rocket.png", CTkLabel, (120, 120), pallete.WHITE.value)
        self.imageRocket.place(relx=0.84, rely=0.72)
        
    @classmethod
    def redirect_screen(self, type_event="dir") -> None:
        """destroy this screen"""
        self.screen.destroy()
        if type_event == "dir":
            self.mask.select_dir(self.root, self.scan, ScreenHome=ScreenHome, widgets=self.widgets_migration)
        elif type_event == "device":
            self.scan.scan_device(
                root=self.root,
                mask=self.mask,
                widgets=self.widgets_migration
            )
        elif type_event == "usb":
            self.scan.scan_device(
                root=self.root,
                mask=self.mask,
                typeScan="usb",
                widgets=self.widgets_migration
            )
        elif type_event == "guardian":
            self.guardian.set_screen(self.root, self.widgets_migration)
        elif type_event == "fixing":
            self.fixing.set_screen(self.root, self.widgets_migration)

    @classmethod
    def migrate_widgets(self):
        """set widgets to an list and migrate"""
        home = ScreenHome()
        self.widgets_migration = {
            "home": home,
            "fixing": self.fixing,
            "scan": self.scan,
            "guardian": self.guardian,
            "mask": self.mask,
            "screen": self.screen,
            "root": self.root
            # "home-instance": ScreenHome
        }
    
    @classmethod
    def destroy_widget(self):
        self.screen.destroy_widget()