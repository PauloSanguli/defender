from customtkinter import CTkFrame, CTkButton

from src.resources import Pallete as pallete

from src.components.images import LoaderImage as loader_image




class MenuComponent:
    def __init__(self, root, funcs, actual, fixing):
        self.root = root
        self.fixing = fixing
        self.scanDevice = ...
        self.scanDevice = ...
        self.scanDevice = ...
        self.home = funcs[0]
        self.widgets = funcs
        # self.actualScreen = {
        #     "scan-dir": 2,
        #     "scan-device": 3,
        #     "scan-usb": 4,
        #     "guardian": 5,
        #     "home": 0,
        #     "fixing": 1
        # }[actual]
        self.funcs = [
            funcs[0],
            funcs[4],funcs[1]
            ,funcs[1],funcs[3]]
        # self.widgets_images = [
        #     "scan_dir_ico.png","scan_device_ico.png",
        #     "scan_usb_ico.png", "guardian-logo-1.png"
        # ]
    
    def clean_windows(self, ty):
        """destroy all widgets from root"""
        for index,widget in enumerate(self.funcs):
                try:
                    widget.destroy_widget()
                except:
                    print(index)
        if ty =="fixing":
            self.fixing.set_screen(self.root, self.widgets)
        elif ty == "home":
            self.home(self.root, self.funcs[1], self.funcs[3], self.fixing)
    
    def set_widgets(self):
        """set widgets on screen"""
        self.screen = CTkFrame(self.root, fg_color=pallete.BLUE.value)
        self.screen.place(
            rely=0,relx=0,
            relwidth=0.03,relheight=1.0
        )
        
        y = 0.2
        count = 0
        self.itemButton = loader_image.load_image(
            root=self.screen,
            name="home.png",
            widget=CTkButton,
            scale=(30,30),
            color=pallete.BLUE.value
        )
        self.itemButton.configure(hover_color=pallete.BLUE.value, command=lambda: self.clean_windows("home"))
        self.itemButton.place(rely=y,relx=0,relwidth=1.0)

        # for commmand, image_name in zip(self.funcs, self.widgets_images):
        #     self.itemButton = loader_image.load_image(
        #         root=self.screen,
        #         name=image_name,
        #         widget=CTkButton,
        #         scale=(30,30),
        #         color=pallete.BLUE.value
        #     )
        #     self.itemButton.configure(hover_color=pallete.BLUE.value)
        #     self.itemButton.place(rely=y,relx=0,relwidth=1.0)
            
        #     count+=1
        y+=0.08
        self.itemButton = loader_image.load_image(
                root=self.screen,
                name="link.png",
                widget=CTkButton,
                scale=(30,30),
                color=pallete.BLUE.value
            )
        self.itemButton.configure(hover_color=pallete.BLUE.value, command=lambda: self.clean_windows("fixing"))
        self.itemButton.place(rely=y,relx=0,relwidth=1.0)
        
        y+=0.08
            
    def destroy_widget(self):
        """remove screen from root"""
        self.screen.destroy()
