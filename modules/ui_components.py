import tkinter as tk
import tkinter.ttk as ttk
from modules import task, json_utils
import os
from src import player


def create_ui_components(parent):
    components = {}

    parent.em_data = json_utils.read_json(os.path.join(parent.data_path, "data"))  # 模擬器相關數據
    eo = parent.em_data["Emulator_options_cn"]  # 選擇語言

    # 下拉選單列表
    comboboxs = [
        (['歷史筆數', '自訂組數', 'Top', '號碼-+', '交集'], 'bet_type', 'readonly', 0, 8, 5, 10, 10),
        (eo, 'select_player', 'readonly', parent.em_data['emulator_current'], 5, 5, 278, 70),
        (['', '1', '2', '3', '4'], 'bet_emulator', None, 1, 2, 5, 341, 70)
    ]
    for combo, box_name, state, current, box_width, box_height, box_x, box_y in comboboxs:
        components[box_name] = ttk.Combobox(parent.window, value=combo, width=box_width, height=box_height, state=state)
        components[box_name].current(current)
        components[box_name].place(x=box_x, y=box_y)

    #
    parent.adb_path = player.find_dir(components['select_player'].get())
    os.chdir(parent.adb_path)

    components['select_player'].bind("<<ComboboxSelected>>", parent.updata_player)

    # 確認表單列表
    checks = [
        ('上升', 'up_check_var', 'up_checkbutton', 1, 90, 10),
        ('X2', 'x2_var', 'x2_checkbutton', 0, 138, 10)
    ]
    for name, var, button, value, x, y in checks:
        components[var] = tk.IntVar()
        components[button] = tk.Checkbutton(parent.window, text=name, variable=components[var], onvalue=1, offvalue=0)  # 建立勾選
        components[var].set(value)  # 預設值:會員內容
        components[button].place(x=x, y=y)  # 示例位置

    components['be1'] = tk.Label(parent.window, text='模擬器:')

    # 輸入、說明表單列表
    entries_labels = [
        ('bet_self', parent.account[1].strip(), 'bs', '自訂組數:', 238, 10, 180, 10),
        ('c_error', '3', 'crc', '連錯換單:', 418, 10, 358, 10),
        ('s_error', '2', 'src', '二次換單:', 418, 40, 358, 40),
        ('profit', '20', 'pro_p', '%', 478, 10, 508, 10),
        ('loss', '20', 'loss_p', '%', 478, 40, 508, 40),
        ('bet_history', '24', 'bh', '歷史筆數:', 72, 40, 10, 40),
        ('bet_count', '5', 'bc', '下單組數(-+):', 192, 40, 110, 40),
        ('bet_time', '2', 'bt', '次後不再下注', 232, 40, 268, 40),
        ('start_amount', '10000', 'sa', '起始金額:', 72, 70, 10, 70),
        ('chips', '0.1', 'cp', '每單籌碼:', 182, 70, 123, 70),
        ('changerank', '1', 'cr', '更新排名:', 462, 70, 400, 70),
        ('hsrank', '100', '', '', 512, 70, 0, 0),
        ('hs_deduct', '11', 'hsd', '內無則扣除:', 10, 100, 40, 100),
        ('first_reduce', '3', '', '', 110, 100, 0, 0),
        ('second_hsd', '0', 'second_reduce', '第二次無則扣除:', 235, 100, 140, 100),
        ('up_profit', '50', 'up_profit_label', '上升獲利:', 325, 100, 265, 100),
        ('up_front', '19', 'up_front_label', '往前:', 390, 100, 355, 100),
        ('up_later', '24', 'up_later_label', '往後:', 455, 100, 420, 100)
    ]

    for entry, default_value, label_var, label_text, x_entry, y_entry, x_label, y_label in entries_labels:
        components[entry] = tk.Entry(parent.window)
        components[label_var] = tk.Label(parent.window, text=label_text)
        components[entry].insert(0, default_value)

        if entry == 'bet_self':
            components[entry].place(x=x_entry, y=y_entry, width=120, height=23)
        elif entry in ['start_amount', 'chips']:
            components[entry].place(x=x_entry, y=y_entry, width=50, height=23)
        else:
            components[entry].place(x=x_entry, y=y_entry, width=30, height=23)
        if label_var != '':
            components[label_var].place(x=x_label, y=y_label)

    button_commands = {
        '新增任務': ['add_task', 548, 10],
        '刪除任務': ['delete_task', 548, 40],
        '更新任務': ['update_task', 548, 70],
        '關閉adb': ['close_adb', 548, 100],
        '執行': ['start_bet_button', 618, 100],
        '測試': ['test1', 618, 10]
    }

    for button_name, command_name in button_commands.items():
        components[button_name] = tk.Button(parent.window, text=button_name.capitalize(), command=lambda cmd=command_name[0]: getattr(task, cmd)(parent))
        components[button_name].place(x=command_name[1], y=command_name[2])  # 示例位置

    return components, parent.em_data
