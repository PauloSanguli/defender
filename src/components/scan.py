from customtkinter import (
    CTkButton, CTkLabel,
    CTkFrame, CTkImage,
    CTkEntry, END
)

from threading import Thread

from tkinter.ttk import Treeview, Scrollbar

from src.components.images import LoaderImage as image

from src.resources import Pallete as pallete

from src.components.header import ScreenHeader

from src.services.schedule import ScheduleService as sched

from time import sleep

from src.resources.json import PATH

from feats import (
    scanDir,
    scanDevice,
    scanUSB
)





class ScreenScan:
    SCANING = True
    WIDGET = None
    
    @classmethod
    def start_scan(self, typeScan: str, dir = None) -> None:
        """select type of scan"""
        scanJob = ...
        if typeScan == "dir": 
            dir = dir.replace("/", "\\")
            scanJob = Thread(target=lambda: scanDir(dir), daemon=True)
            self.startScan = True
        elif typeScan == "device":
            scanJob = Thread(target=lambda: scanDevice(), daemon=True)
            self.startScan = True
        else:
            self.NOT_DRIVE_AVAILABLE = scanUSB(True)
            if not self.NOT_DRIVE_AVAILABLE: self.go_home()
            scanJob = Thread(target=lambda: scanUSB(), daemon=True)
            self.startScan = True
        scanJob.start()

        
    
    @classmethod
    def scan_device(self, root, dir="C://users/Paulo Sanguli/", mask=None, typeScan="device", widgets=None):
        print(f"SCREEN: {root}")
        self.cron = sched()
        self.root = root
        self.mask = mask
        self.widgets = widgets
        self.screen = CTkFrame(self.root, fg_color=pallete.WHITE.value)
        self.screen.pack(fill="both", expand=True)
        self.root.config(background=pallete.WHITE.value)
        self.header = ScreenHeader(self.screen,"Scanear dispositivo", self.widgets, "scan")
        
        self.labelHead = CTkLabel(self.screen,
                                  text="Scan device",
                                  text_color=pallete.GRAY.value,
                                  fg_color=pallete.WHITE.value,
                                  bg_color=pallete.WHITE.value,
                                  font=("Inter", 16))
        self.labelHead.place(relx=0.05, rely=0.26)
        
        self.labelHead = CTkLabel(self.screen,
                                  text="Progresso",
                                  text_color=pallete.BLACK.value,
                                  fg_color=pallete.WHITE.value,
                                  bg_color=pallete.WHITE.value
                                  ,font=("Inter", 20))
        self.labelHead.place(relx=0.05, rely=0.3)

        self.imageRay = image.load_image(self.screen, "ray.png", CTkLabel
            ,(80, 50), pallete.WHITE.value)
        self.imageRay.place(relx=0.131, rely=0.26)
        
        self.labelDir = CTkLabel(self.screen,
                                 text="directório a ser analisado",
                                 text_color=pallete.GRAY.value,
                                 fg_color=pallete.WHITE.value,
                                 bg_color=pallete.WHITE.value,
                                 font=("Inter", 16)).place(relx=0.82, rely=0.22)
        
        self.dirAnalisyng = CTkEntry(self.screen,
                                 text_color=pallete.BLACK.value,
                                 fg_color=pallete.GREEN_SECONDARY.value,
                                 border_color=pallete.GREEN_PRIMARY.value,
                                 corner_radius=50,
                                 bg_color=pallete.WHITE.value,
                                 font=("Inter", 16))
        self.dirAnalisyng.place(relwidth=0.2,relheight=0.05,relx=0.755, rely=0.269)
        self.dirAnalisyng.insert(0, dir)
        
        self.labelHead = CTkLabel(self.screen,
                                  text="Resultado",
                                  text_color=pallete.BLACK.value,
                                  fg_color=pallete.WHITE.value,
                                  bg_color=pallete.WHITE.value
                                  ,font=("Inter", 16))
        self.labelHead.place(relx=0.05, rely=0.52)
        
        self.labelDir = CTkLabel(self.screen,
                                 text="limpe para proteger",
                                 text_color=pallete.BLACK.value,
                                 fg_color=pallete.WHITE.value,
                                 bg_color=pallete.WHITE.value,
                                 font=("Inter", 16)).place(relx=0.82, rely=0.52)
        
        self.tableDirs = CTkFrame(self.screen,
                                  fg_color=pallete.WHITE.value,
                                  bg_color=pallete.WHITE.value,
                                  border_color=pallete.GRAY.value,
                                  corner_radius=0,
                                  border_width=1)
        self.tableDirs.place(relwidth=1.0,relheight=0.3,relx=0,rely=0.6)
        
        self.treeview = Treeview(self.tableDirs, columns=("col1","col2","col3","col4"))
        self.treeview.heading("#0",text="")
        self.treeview.heading("#1",text="NOME")
        self.treeview.heading("#2",text="LOCALIZAÇÃO")
        self.treeview.heading("#3",text="DESCRIÇÃO")
        self.treeview.heading("#4",text="LIMPO")

        self.treeview.column("#0",width=0)
        self.treeview.column("#1",width=100)
        self.treeview.column("#2",width=100)
        self.treeview.column("#3",width=100)
        self.treeview.column("#4",width=100)
        
        self.treeview.place(relwidth=1.0,relx=0,rely=0,relheight=1.0)

        self.scrollTreeview = Scrollbar(self.tableDirs,orient="vertical",command=self.treeview.yview)
        self.scrollTreeview.pack(side="right",fill="y")
        self.treeview.configure(yscrollcommand=self.scrollTreeview.set)
            # place(relx=0.97,rely=0.1, relheight=0.8)
            
        self.labelResultScanEntry = CTkEntry(self.screen,
                                  text_color=pallete.RED.value,
                                  fg_color=pallete.RED_SECONDARY.value,
                                  bg_color=pallete.WHITE.value,
                                  corner_radius=50,
                                  border_width=1,
                                  border_color=pallete.RED.value,
                                  font=("Inter", 14))
        self.labelResultScanEntry.place(relx=0.05, rely=0.92, relwidth=0.1,relheight=0.05)
        self.labelResultScanEntry.insert(0, "0 encontrados")
        
        self.labelResultScan = CTkButton(self.screen,
                                    text="Deletar todos",
                                    text_color=pallete.WHITE.value,
                                    fg_color=pallete.RED.value,
                                    bg_color=pallete.WHITE.value,
                                    corner_radius=170,
                                    border_width=1,
                                    hover_color=pallete.RED_SECONDARY.value,
                                    border_color=pallete.RED.value,
                                    font=("Inter", 14),
                                    command=lambda: self.__redirect_screen())
        self.labelResultScan.place(relx=0.16, rely=0.92, relwidth=0.1,relheight=0.05)
        
        cronJob = Thread(target=lambda: self.cron.start_cron(self.dirAnalisyng, self.treeview, self.labelResultScanEntry), daemon=True)
        progressJob = Thread(target=lambda: self.progress(), daemon=True)
        
        cronJob.start()
        self.start_scan(typeScan, dir)
        progressJob.start()
    
    @classmethod
    def progress(self, count = 0) -> None:
        """update progressbar"""
        orgImage = "progress.png"
        if count >= 1:
            orgImage = "progress-y.png".replace("y",str(count))
        self.imageProgress = image.load_image(self.screen,
                                            name=orgImage,
                                            widget=CTkLabel,
                                            scale=(1400,46),
                                            color=pallete.WHITE.value)
        self.imageProgress.pack(pady=320)
        sleep(10)
        count+=1
        if count <= 11:
            self.imageProgress.destroy()
            progressJob = Thread(target=lambda: self.progress(count), daemon=True)
            progressJob.start()
   
    @classmethod
    def set_cols_table(self, fields: list) -> None:
        """set fields on the front"""
        for field in fields:
            self.treeview.insert("", END, values=field)
    
    @classmethod
    def __redirect_screen(self) -> None:
        """redirect screen"""
        self.screen.destroy()
        
        self.cron.stop_cron()
        self.mask.delete_files(self.root, self.widgets, "modal-1.png")

    @classmethod
    def go_home(self) -> None:
        """go to the screen home"""
        self.destroy_widget()
        self.widgets["home"].set_screen(self.root, self.widgets["scan"], self.widgets["guardian"], self.widgets["fixing"])
    
    @classmethod
    def destroy_widget(self):
        """destroy screen"""
        self.screen.destroy()
                                                
                                                