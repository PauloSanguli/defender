import schedule as cron

from time import sleep

from pathlib import Path

from customtkinter import END

from json import loads as json_decoder
from json.decoder import JSONDecodeError
from json import dumps as json_encoder

from feats import PATH

import os





class ScheduleService:
    __CRON = cron
    WIDGET = None
    COUNT_VIRUS = 0
    COMPLETE_DIR = os.path.join(PATH, "res.json")
    COMPLETE_DIR_2 = os.path.join(PATH, "delatados.json")

    @classmethod
    def start_cron(cls, widget, widget_d, widget_r) -> None:
        """start cron for fecth directorys"""
        cls.__CRON.every(1).second.do(lambda: cls.get_json(cls.COMPLETE_DIR, widget))
        cls.__CRON.every(3).seconds.do(lambda: cls.get_json(cls.COMPLETE_DIR_2, widget_d,toDelete=True, resultWidget=widget_r))

        while True:
            cls.__CRON.run_pending()
            sleep(1)

    @classmethod
    def get_json(cls, path, widget, toDelete = False, resultWidget = None) -> None:
        """get dirs from json file"""
        try:
            fileContent = Path(path).read_text()
            cls.clean_file(path)
            dirs = json_decoder(fileContent)
            count=0
            if len(dirs) >= 1:
                for dir in dirs:
                    print(f"{dir}")
                    if not toDelete:
                        widget.delete(0,"end")
                        sleep(1)
                        widget.insert(0, dir)
                        sleep(2)
                    else:
                        print("virus")
                        cls.COUNT_VIRUS += 1
                        resultWidget.delete(0, "end")
                        resultWidget.insert(0, f"{cls.COUNT_VIRUS} encontrados")
                        widget.insert("", END, values=["Vírus",dir,"Não","Indefinido"])
            else:
                count+=1
                print("Dont has directory")
                if count >= 5:
                    cls.stop_cron()
        except JSONDecodeError:
            print("Dont has an json format on file json")
            cls.stop_cron()

    @classmethod
    def clean_file(cls, path) -> None:
        """clean json file directorys"""
        with open(path, "w") as file:
            file.write(json_encoder([],indent=4))
            file.close()

    
    @classmethod
    def delete_dir(cls) -> None:
        """delete dir form json file"""
    
    @classmethod    
    def stop_cron(cls) -> None:
        """stop cron for fetch directorys"""
        cls.__CRON.clear()
