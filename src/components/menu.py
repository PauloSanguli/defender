from customtkinter import CTkFrame, CTkButton

from src.resources import Pallete as pallete

from src.components.images import LoaderImage as loader_image




class MenuComponent:
    def __init__(self, root, funcs, actual, to_delete):
        print(f"ROOT: {root}")
        self.root = root
        self.to_delete = to_delete
        self.actual_screen = actual
        self.fixing = funcs["fixing"]
        self.home = funcs["home"]
        self.widgets = funcs
    
    def clean_windows(self, clicked):
        """destroy all widgets from root"""
        if self.actual_screen == clicked:
            ...
        else:
            try:
                self.to_delete.destroy_widget()
            except:
                self.to_delete.redirect_screen("fixing")
            if clicked == "home":
                self.home.set_screen(self.widgets["root"], self.widgets["scan"], self.widgets["guardian"], self.fixing)
            elif clicked == "fixing":
                self.fixing.set_screen(self.widgets["root"], self.widgets)
            
    
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
