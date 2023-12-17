import subprocess
from constants.constants import LDPLAYER_PATH
import sys
import os

from ld_manager.create_ld import open_file
from models.device import Device

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def get_list_ld():
    ld_players = []
    vms_path = os.path.join(LDPLAYER_PATH, "vms")
    config_path = os.path.join(LDPLAYER_PATH, "vms", "config")
    try:
        id_list = []
        file_list = os.listdir(vms_path)
        for file in file_list:
            if file[:7] == "leidian":
                id_list.append(file[7:])
            else:
                continue

        for i in id_list:
            data = open_file(f'leidian{i}.config', config_path)
            data_fb = data.get('facebook')
            data_email = data.get('email')

            if data_fb is None or data_email is None:
                data_fb = False
                data_email = False

            name_ld = f"LDPlayer-{i}"
            if int(i) == 0:
                name_ld = "LDPlayer"

            device = Device(i,
                            name_ld,
                            data["propertySettings.phoneIMEI"],
                            f"emulator-{5554 + (int(i) * 2)}",
                            data["propertySettings.phoneManufacturer"],
                            data["propertySettings.phoneModel"],
                            data["propertySettings.phoneIMSI"],
                            data["propertySettings.phoneAndroidId"],
                            data["propertySettings.phoneSimSerial"],
                            data["propertySettings.macAddress"],
                            data_fb)

            ld_players.append(device)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

    return ld_players
