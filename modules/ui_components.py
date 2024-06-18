import tkinter as tk
import tkinter.ttk as ttk
from modules import table

def create_ui_components(parent):
    components = {}

    mt = ['歷史筆數', '自訂組數', 'Top', '號碼-+', '交集']
    components['bet_type'] = ttk.Combobox(parent.window, value=mt, width=8, state='readonly')
    components['bet_type'].current(0)
    components['bet_type'].place(x=100, y=50)  # 示例位置

    components['up_var'] = tk.IntVar()
    components['up_checkbutton'] = tk.Checkbutton(parent.window, text='上升', variable=components['up_var'], onvalue=1, offvalue=0)
    components['up_var'].set(1)
    components['up_checkbutton'].place(x=100, y=100)  # 示例位置

    components['bet_self'] = tk.Entry(parent.window)
    components['bs'] = tk.Label(parent.window, text='自訂組數:')
    components['bet_self'].insert(0, parent.account[1].strip())
    components['bet_self'].place(x=100, y=150)  # 示例位置
    components['bs'].place(x=200, y=150)  # 示例位置

    components['x2_var'] = tk.IntVar()
    components['c1'] = tk.Checkbutton(parent.window, text='X2', variable=components['x2_var'], onvalue=1, offvalue=0)
    components['x2_var'].set(parent.account[5])
    components['c1'].place(x=100, y=200)  # 示例位置

    entries_labels = [
        ('c_error', 'crc', '連錯換單:', '3', 100, 250, 200, 250),
        ('s_error', 'src', '二次換單:', '2', 100, 300, 200, 300),
        ('profit', 'pro_p', '%', '20', 100, 350, 200, 350),
        ('loss', 'loss_p', '%', '20', 100, 400, 200, 400),
        ('bet_history', 'bh', '歷史筆數:', '24', 100, 450, 200, 450),
        ('bet_count', 'bc', '下單組數(-+):', '5', 100, 500, 200, 500),
        ('bet_time', 'bt', '次後不再下注', '2', 100, 550, 200, 550),
        ('start_amount', 'sa', '起始金額:', '10000', 300, 250, 400, 250),
        ('chips', 'cp', '每單籌碼:', '0.1', 300, 300, 400, 300),
        ('changerank', 'cr', '更新排名:', '1', 300, 350, 400, 350),
        ('hsrank', '', '', '100', 300, 400, 400, 400),
        ('hs_deduct', 'hsd', '內無則扣除:', '11', 300, 450, 400, 450),
        ('first_reduce', '', '', '3', 300, 500, 400, 500),
        ('second_hsd', '', '第二次無則扣除:', '0', 300, 550, 400, 550),
        ('second_reduce', '', '', '0', 300, 600, 400, 600),
        ('up_profit', '', '上升獲利:', '50', 500, 250, 600, 250),
        ('up_front', '', '往前:', '19', 500, 300, 600, 300),
        ('up_later', '', '往後:', '24', 500, 350, 600, 350)
    ]

    for entry, label_var, label_text, default_value, x_entry, y_entry, x_label, y_label in entries_labels:
        components[entry] = tk.Entry(parent.window)
        components[label_var] = tk.Label(parent.window, text=label_text)
        components[entry].insert(0, default_value)
        components[entry].place(x=x_entry, y=y_entry)
        components[label_var].place(x=x_label, y=y_label)

    be = ['', '1', '2', '3', '4']
    components['be1'] = tk.Label(parent.window, text='模擬器:')
    components['bet_emulator'] = ttk.Combobox(parent.window, value=be, width=8, height=5, state='readonly')
    components['bet_emulator'].current(1)
    components['be1'].place(x=500, y=400)  # 示例位置
    components['bet_emulator'].place(x=600, y=400)  # 示例位置

    button_commands = {
        '新增任務': 'add_task',
        '刪除任務': 'delete_task',
        '更新任務': 'update_task',
        '關閉adb': 'close_adb',
        '執行': 'start_bet_button',
        '測試': 'test1'
    }

    for button_name, command_name in button_commands.items():
        components[button_name] = tk.Button(parent.window, text=button_name.capitalize(),
                                            command=lambda cmd=command_name: getattr(table, cmd)(parent))
        components[button_name].place(x=10, y=100 + 50 * list(button_commands.keys()).index(button_name))  # 示例位置

    return components
