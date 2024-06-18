
# class AA:
#     def __init__(self, *args):
#         self.args = args

# 新增任務
def add_task(parent, *args):

    selected_value = parent.select_player.get()
    print(f"Selected value: {selected_value}")

def delete_task(parent):
    print(222222222)

def update_task(parent):
    print(3333333333)

def close_adb(parent):
    print(4444444444)

def start_bet_button(parent):
    print(55555555)

def test1(parent):
    print(666666666)


# from operator import attrgetter
# from adbutils import adb
#
# # 定义AdbDevice类
# class AdbDevice:
#     def __init__(self, serial):
#         self.serial = serial
#
#     def __repr__(self):
#         return f"AdbDevice(serial={self.serial})"
#
# # 初始化AdbDevice对象列表
# devices = [
#     AdbDevice(serial='127.0.0.1:62001'),
#     AdbDevice(serial='127.0.0.1:62005'),
#     AdbDevice(serial='127.0.0.1:62003')
# ]
#
# adblist = adb.device_list()
#
# print(adblist)
#
# # 使用sorted()对对象列表按端口号排序
# sorted_devices = sorted(devices, key=lambda d: int(d.serial.split(':')[-1]))
#
# # 输出排序后的结果
# print(sorted_devices[0].serial)
