import os
from src import player
import tkinter as tk, tkinter.ttk as ttk
from adbutils import adb
from modules import json_utils, task
from modules.ui_components import create_ui_components
from modules.db_utils import MSSQL, read_txt


class Emulate:
    def __init__(self, window):
        self.file_path = os.path.realpath(__file__)                                 # 當前python執行檔的絕對路徑
        self.file_path = os.path.dirname(self.file_path)                            # 當前資料夾
        self.png_path = os.path.join(self.file_path, "png")                         # 當前資料夾 + png資料夾
        self.data_path = os.path.join(self.file_path, "data")                       # 當前資料夾 + data資料夾

        self.window = window
        self.window.geometry('668x650+420+250')                                     # 視窗大小+固定開啟位置
        self.window.resizable(0, 0)                                                 # 固定視窗大小
        self.window.title('Emulator-Bet')                                           # 視窗名稱

        self.emulators = []                                                         # 模擬器列表預設值

        self.load_data()

        # task
        self.cuc = create_ui_components(self)

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
