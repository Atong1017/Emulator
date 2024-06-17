import os
from adbutils import adb


def find_dir(playname="nox", possible_dirs=None):
    if possible_dirs is None:
        # Define possible installation directories
        possible_dirs = [
            "C:\\",
            "C:\\Program Files\\",
            "C:\\Program Files (x86)\\",
            "D:\\",
            "D:\\Program Files\\",
            "D:\\Program Files (x86)\\",
            # Set the current user's home directory =>  /home/username/
            os.path.expanduser("~")
        ]

        # folder names for emulators
        if playname.lower() in "memu, 逍遙, 逍遙":
            player_folders = ["Microvirt\\MEmu"]
        elif playname.lower() in "nox, 夜神, 夜神":
            player_folders = ["Nox\\bin"]
        elif playname.lower() in "ldplayer, 雷電, 雷电":
            player_folders = ["LDPlayer\\LDPlayer9"]

        # Search catalog
        for base_dir in possible_dirs:
            for folder in player_folders:
                search_path = os.path.join(base_dir, folder)
                if os.path.exists(search_path):

                    return search_path

        return None

    else:

        return possible_dirs


def get_connected_devices(playername="nox"):
    # Find all devices
    connected_devices = [a.serial for a in adb.device_list()]

    if playername.lower() not in "ldplayer, 雷電, 雷电":
        connected_devices = connected_devices[::-1]

    return connected_devices


if __name__ == "__main__":
    memu_path = find_dir("ldplayer")
    if memu_path:
        print(f"Emulator installation directory: {memu_path}")
    else:
        print("The installation directory of the emulator was not found!")
