from customtkinter import (
    CTkLabel,CTkEntry,
    CTkButton, CTkFrame
)

import json
from pathlib import Path
from feats.SOFTWARE import modo_agrecisso

from tkinter.filedialog import askdirectory

from src.resources import Pallete as pallete

from src.components.images import LoaderImage as image




class ScreenMask:
    WIDTH_MODAL = 550
    HEIGHT_MODAL = 450
    Y_MODAL = 0.2
    X_MODAL = 0.3
    SCREEN_HOME = None

    # def __init__(self, root):
        # self.root = root
        # self.screen = CTkFrame(self.root, fg_color=pallete.GRAY.value)
        # self.screen.place(relx=0,rely=0, relwidth=1.0,relheight=1.0)
        # self.configs("modal-2.png")
        # self.select_dir()
        # self.delete_files()
        # self.delete_done()

    @classmethod
    def create_screen(self, root, modal):
        """"create the screen on root"""
        self.screen = CTkFrame(root, fg_color=pallete.GRAY.value)
        self.screen.place(relx=0,rely=0, relwidth=1.0,relheight=1.0)
        self.configs(modal)

    @classmethod
    def center_widget(self, master_w, widget_w) -> int:
        """center an widget"""
        width_center = (master_w-widget_w)//2
        return width_center

    @classmethod
    def configs(self, img: str = None) -> None:
        """config screen"""
        self.containerItems = image.load_image(self.screen,img,
            CTkLabel,(self.WIDTH_MODAL,self.HEIGHT_MODAL),pallete.GRAY.value)
        self.containerItems.place(
            rely=self.Y_MODAL,
            relx=self.X_MODAL
        )

    @classmethod
    def delete_files(self, root, widgets, modal="modal-1.png") -> None:
        """screen for delete files"""
        self.root = root
        self.screen_home = widgets[0]
        self.scan = widgets[1]
        self.fixing = widgets[2]
        self.guardian = widgets[3]
        self.create_screen(root, modal)

        self.labelHeadDelete = CTkLabel(self.screen,
            text="Eliminando vírus",fg_color=pallete.WHITE.value,
            font=("Inter", 18), text_color=pallete.BLACK.value
        )
        self.labelHeadDelete.place(rely=0.4, relx=0.34)

        self.labelDirDel = CTkEntry(self.screen,
                                    corner_radius=50,
                                    fg_color=pallete.WHITE.value,
                                    bg_color=pallete.WHITE.value,
                                    border_color=pallete.GRAY.value,
                                    border_width=1, text_color=pallete.BLACK.value)
        self.labelDirDel.place(relx=0.34,rely=0.48, relwidth=0.3,relheight=0.06)
        self.labelDirDel.insert(0, "C://users/Paulo Sanguli/Documents/")

        self.labelInfoDelete = CTkLabel(self.screen,
            text="processando...",fg_color=pallete.WHITE.value,
            font=("Inter", 16), text_color=pallete.BLACK.value
        )
        self.labelInfoDelete.place(rely=0.55, relx=0.34)

        self.labelResultDelete = CTkLabel(self.screen,
            text="( 0 ) eliminados",fg_color=pallete.WHITE.value,
            font=("Inter", 16), text_color=pallete.RED.value
        )
        self.labelResultDelete.place(rely=0.64, relx=0.34)

        self.buttonEndDel = CTkButton(self.screen,
                            text="Finalizar",
                            hover_color=pallete.GREEN_PRIMARY.value,
                            fg_color=pallete.WHITE.value,
                            bg_color=pallete.WHITE.value,
                            text_color=pallete.BLACK.value,
                            border_color=pallete.GREEN_PRIMARY.value,
                            border_width=2,
                            corner_radius=200,command=lambda: self.__go_home())
        self.buttonEndDel.place(rely=0.64,relx=0.55, relheight=0.06)

    @classmethod
    def select_dir(self, root, scan, modal = "modal.png", ScreenHome = None, widgets = None) -> None:
        """screen for select directory"""
        self.scan = scan
        self.root = root
        self.SCREEN_HOME = ScreenHome
        self.widgets = widgets
        self.create_screen(self.root, modal)

        self.labelHead = CTkLabel(self.screen,
            text="Clique no botão",fg_color=pallete.WHITE.value,
            font=("Inter", 14), text_color=pallete.BLACK.value
        )
        self.labelHead.place(rely=0.36, relx=0.34)

        self.labelHead = CTkLabel(self.screen,
            text="Escolha o directório",fg_color=pallete.WHITE.value,
            font=("Inter", 18),text_color=pallete.BLACK.name
        )
        self.labelHead.place(rely=0.4, relx=0.34)

        self.inputDir = CTkEntry(self.screen,corner_radius=50, text_color=pallete.BLACK.value,fg_color=pallete.WHITE.value,bg_color=pallete.WHITE.value)
        self.inputDir.place(relx=0.34,rely=0.48, relwidth=0.3,relheight=0.06)

        self.br = CTkButton(self.screen,
                            text="Selecionar directório",
                            command=lambda: self.__update_dir(),
                            corner_radius=100,
                            fg_color=pallete.GREEN_PRIMARY.value,
                            hover_color=pallete.GREEN_SECONDARY.value,
                            bg_color=pallete.WHITE.value,
                            text_color=pallete.BLACK.value)\
            .place(
                relx=0.34,rely=0.56, relwidth=0.3,relheight=0.06
            )

        self.buttonStartScan = CTkButton(self.screen,
                            text="Avançar",
                            hover_color=pallete.GREEN_PRIMARY.value,
                            fg_color=pallete.WHITE.value,
                            bg_color=pallete.WHITE.value,
                            text_color=pallete.BLACK.value,
                            border_color=pallete.GREEN_PRIMARY.value,
                            border_width=2,
                            corner_radius=200,command=lambda: self.__redirect(self.inputDir.get()))
        self.buttonStartScan.place(rely=0.65,relx=0.54, relheight=0.06)

    @classmethod
    def delete_done(self, root, modal="modal-2.png") -> None:
        """status for end of delete virus"""
        self.create_screen(root, modal)

        self.labelHeadDeleteDone = CTkLabel(self.screen,
            text="Vírus eliminado",fg_color=pallete.WHITE.value,
            font=("Inter", 18)
        )
        self.labelHeadDeleteDone.place(rely=0.4, relx=0.34)

        self.labelInfoDeleteDone = CTkLabel(self.screen,
            text="O seu dispositivo está limpo",fg_color=pallete.WHITE.value,
            font=("Inter", 18), text_color=pallete.BLACK.value
        )
        self.labelInfoDeleteDone.place(rely=0.55, relx=0.42)

        self.labelResultDeleteDone = CTkLabel(self.screen,
            text3="( 30 ) eliminados",fg_color=pallete.WHITE.value,
            font=("Inter", 16), text_color=pallete.RED.value
        )
        self.labelResultDeleteDone.place(rely=0.73, relx=0.34)

        self.buttonEndDelDone = CTkButton(self.screen,
                            text="Finalizar",
                            hover_color=pallete.GREEN_PRIMARY.value,
                            fg_color=pallete.WHITE.value,
                            bg_color=pallete.WHITE.value,
                            text_color=pallete.BLACK.value,
                            border_color=pallete.GREEN_PRIMARY.value,
                            border_width=2,
                            corner_radius=200,command=lambda: self.__go_home())
        self.buttonEndDelDone.place(rely=0.7,relx=0.58, relheight=0.06)

    @classmethod
    def __update_dir(self) -> None:
        """set the dir selected on screen"""
        dir = askdirectory()
        self.inputDir.delete(0, "end")
        self.inputDir.insert(0, dir)

    @classmethod
    def __redirect(self, dirGetted):
        """redict to scan screen"""
        self.destroy_widget()
        print("close screen before go to screen scan")
        # modo_agrecisso(dirGetted)
        # print(dirGetted.replace())
        Path("feats/res.json").write_text(json.dumps(["testando isso"]))
        self.scan.scan_device(self.root, dirGetted, ScreenMask, "dir", self.widgets)

    @classmethod
    def __go_home(self) -> None:
        """go to screen home"""
        self.destroy_widget()
        print(self.SCREEN_HOME)
        self.screen_home(self.root, self.scan, self.guardian, self.fixing)

    @classmethod
    def destroy_widget(self):
        """remove screen"""
        self.screen.destroy()

