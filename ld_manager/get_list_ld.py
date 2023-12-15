import subprocess
from constants.constants import LDPLAYER_PATH
from create_ld import open_file
import sys
import os

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

            ld_player = {
                "name": data['name'],
                "uuid": f"emulator-{5554 + (int(i) * 2)}",
                "facebook": data_fb,
                "email": data_email,
                "manufacturer": data["propertySettings.phoneManufacturer"],
                "model": data["propertySettings.phoneModel"],
                "IMEI": data["propertySettings.phoneIMEI"],
                "IMSI": data["propertySettings.phoneIMSI"],
                "androidId": data["propertySettings.phoneAndroidId"],
                "simSerial": data["propertySettings.phoneSimSerial"],
                "macAddress": data["propertySettings.macAddress"]
            }

            ld_players.append(ld_player)


    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

    return ld_players
