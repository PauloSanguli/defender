from src.pages.body import App
from src.components.initial import ScreenInitial
from src.components.scan import ScreenScan
from src.components.mask import ScreenMask
from src.components.fixing import ScreenFixing
from src.components.guardian import ScreenGuardian





if __name__ == "__main__":
    app = App()
    scanFrame = ScreenScan()
    fixingFrame = ScreenFixing()
    guardianFrame = ScreenGuardian()
    print("...")
    frameInitial = ScreenInitial(app, scanFrame, guardianFrame, fixingFrame)
    app.mainloop()
    print("111")