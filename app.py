import os
from src import player
import tkinter as tk, tkinter.ttk as ttk
from adbutils import adb
from modules import json_utils


class Emulate:
    def __init__(self, window):
        self.file_path = os.path.realpath(__file__)                             # absolute path of executable file
        self.file_path = os.path.dirname(self.file_path)
        self.png_path = os.path.join(self.file_path, "png")                     # current folder + png folder
        self.data_path = os.path.join(self.file_path, "data")                   # current folder + adb folder

        self.window = window
        self.window.geometry('668x650+420+250')                                 # window size, position
        self.window.resizable(0, 0)                                             # fixed window size
        self.window.title('Emulator-Bet')                                       # window name

        # ================================================ args ================================================
        self.emulators = []                                                     # emulator list

        # ================================================  ================================================
        self.em_data = json_utils.read_json(os.path.join(self.data_path, "data"))     # read data

        eo = self.em_data["Emulator_options_cn"]                                # Combobox list

        # Create a Combobox
        self.select_player = ttk.Combobox(self.window, value=eo, width=5, height=5, state='readonly')
        self.select_player.current(self.em_data['emulator_current'])            # default Combobox select the first item

        self.adb_path = player.find_dir(self.select_player.get())               # emulator folder
        os.chdir(self.adb_path)                                                 # change directory to specified path

        self.select_player.bind("<<ComboboxSelected>>", self.updata_player)     # bind KeyRelease event

        self.select_player.place(x=300, y=0)

    #
    def updata_player(self, event=None):
        new_player = self.select_player.get()                                   # get selection info
        self.adb_path = player.find_dir(new_player)                             # emulator folder
        os.chdir(self.adb_path)                                                 # change directory to specified path

        self.emulators = sorted(adb.device_list(), key=lambda d: d.serial)

        spc = 0
        if new_player == '雷电':
            spc = 0
        elif new_player == '夜神':
            spc = 1
        elif new_player == '逍遙':
            spc = 2

        self.em_data["emulator_current"] = spc

        json_utils.save_json(self.em_data, os.path.join(self.data_path, "data"))


if __name__ == "__main__":
    root = tk.Tk()
    app = Emulate(root)
    root.mainloop()

