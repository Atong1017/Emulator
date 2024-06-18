import os
from src import player
import tkinter as tk, tkinter.ttk as ttk
from adbutils import adb
from modules import json_utils, table
from modules.ui_components import create_ui_components
from modules.db_utils import MSSQL, read_txt


class Emulate:
    def __init__(self, window):
        self.file_path = os.path.realpath(__file__)  # 當前python執行檔的絕對路徑
        self.file_path = os.path.dirname(self.file_path)
        self.png_path = os.path.join(self.file_path, "png")
        self.data_path = os.path.join(self.file_path, "data")

        self.window = window
        self.window.geometry('668x650+420+250')
        self.window.resizable(0, 0)
        self.window.title('Emulator-Bet')

        self.emulators = []

        self.em_data = json_utils.read_json(os.path.join(self.data_path, "data"))

        eo = self.em_data["Emulator_options_cn"]

        self.select_player = ttk.Combobox(self.window, value=eo, width=5, height=5, state='readonly')
        self.select_player.current(self.em_data['emulator_current'])

        self.adb_path = player.find_dir(self.select_player.get())
        os.chdir(self.adb_path)

        self.select_player.bind("<<ComboboxSelected>>", self.updata_player)

        self.load_data()

        # task
        self.cuc = create_ui_components(self)

        self.select_player.place(x=300, y=0)

    def load_data(self):
        login_info = read_txt(self.data_path + '\\login_info')
        self.sql_server = MSSQL(login_info)
        account_info = read_txt(self.data_path + '\\account')
        self.account_name = account_info[0].strip()
        self.account_int = account_info[1].strip()
        self.account = account_info[2:]

    def updata_player(self, event=None):
        new_player = self.select_player.get()
        self.adb_path = player.find_dir(new_player)
        os.chdir(self.adb_path)

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
