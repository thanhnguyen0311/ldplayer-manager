import subprocess
import shutil
import sys
import os
import json
from constants.constants import LDPLAYER_PATH, LDCONSOLE_PATH, CLONE_LD_DATA

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

config_path = os.path.join(LDPLAYER_PATH, "vms", "config")


def open_file(filename, folder):
    # Get the full path to the file
    path = os.path.join(os.path.expanduser('~'), folder, filename)
    # Open the file and read its contents
    with open(path, 'r') as f:
        contents = json.load(f)
    # Return the contents of the file
    return contents


def save_json_file(data, filename, folder):
    path = os.path.join(os.path.expanduser('~'), folder, filename)
    with open(path, 'w') as file:
        json.dump(data, file, indent=2)


def create_ld(number):
    new_ldplayers = []
    for i in range(number):
        try:
            id_list = []
            file_list = os.listdir(config_path)

            for file in file_list:
                if file[7:-7].isdigit():
                    id_list.append(file[7:-7])
                else:
                    continue

            id_list = sorted(id_list, key=lambda x: int(x))
            i = 0

            while str(i) in id_list:
                i = i + 1

            subprocess.call([LDCONSOLE_PATH] + ["add"], shell=True)

            contents = open_file(f'leidian{i}.config', config_path)

            source_data = os.path.join(LDPLAYER_PATH, "vms", "data.vmdk")
            destination_data = os.path.join(LDPLAYER_PATH, "vms", f'leidian{i}')
            if CLONE_LD_DATA:
                shutil.copy(source_data, destination_data)

            name_ld = f"LDPlayer-{i}"
            if int(i) == 0:
                name_ld = "LDPlayer"

            new_LDPlayer = {
                "name": name_ld,
                "uuid": f"emulator-{5554 + (i * 2)}",
                "manufacturer": contents["propertySettings.phoneManufacturer"],
                "model": contents["propertySettings.phoneModel"],
                "IMEI": contents["propertySettings.phoneIMEI"],
                "IMSI": contents["propertySettings.phoneIMSI"],
                "androidId": contents["propertySettings.phoneAndroidId"],
                "simSerial": contents["propertySettings.phoneSimSerial"],
                "macAddress": contents["propertySettings.macAddress"]
            }

            config = {
                "name": name_ld,
                "uuid": f"emulator-{5554 + (i * 2)}",
                "facebook": False,
                "email": False,
                "basicSettings.rootMode": True,
                "basicSettings.adbDebug": 2,
                "advancedSettings.resolution": {
                    "width": 720,
                    "height": 1280
                },
                "advancedSettings.resolutionDpi": 320,
                "basicSettings.HDRQuality": 0,
                "advancedSettings.cpuCount": 1,
                "advancedSettings.memorySize": 1024
            }

            # Merge 2 json data
            contents = {**contents, **config}
            save_json_file(contents, f'leidian{i}.config', config_path)
            new_ldplayers.append(new_LDPlayer)

        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            return None

    return new_ldplayers


def clone_ld(data):
    try:
        id_list = []
        file_list = os.listdir(config_path)

        for file in file_list:
            if file[7:-7].isdigit():
                id_list.append(file[7:-7])
            else:
                continue

        id_list = sorted(id_list, key=lambda x: int(x))
        i = 0

        while str(i) in id_list:
            i = i + 1

        subprocess.call([LDCONSOLE_PATH] + ["add"], shell=True)

        name_ld = f"LDPlayer-{i}"
        if int(i) == 0:
            name_ld = "LDPlayer"

        contents = {
            "propertySettings.phoneIMEI": data["IMEI"],
            "propertySettings.phoneIMSI": data["IMSI"],
            "propertySettings.phoneSimSerial": data["simSerial"],
            "propertySettings.phoneAndroidId": data["androidId"],
            "propertySettings.phoneModel": data["model"],
            "propertySettings.phoneManufacturer": data["manufacturer"],
            "propertySettings.macAddress": data["macAddress"]
        }

        config = {
            "name": name_ld,
            "uuid": f"emulator-{5554 + (i * 2)}",
            "facebook": "",
            "email": "",
            "basicSettings.rootMode": True,
            "basicSettings.adbDebug": 2,
            "advancedSettings.resolution": {
                "width": 720,
                "height": 1280
            },
            "advancedSettings.resolutionDpi": 320,
            "basicSettings.HDRQuality": 0,
            "advancedSettings.cpuCount": 1,
            "advancedSettings.memorySize": 1024
        }

        new_LDPlayer = {
            "name": name_ld,
            "uuid": f"emulator-{5554 + (i * 2)}",
            "manufacturer": contents["propertySettings.phoneManufacturer"],
            "model": contents["propertySettings.phoneModel"],
            "IMEI": contents["propertySettings.phoneIMEI"],
            "IMSI": contents["propertySettings.phoneIMSI"],
            "androidId": contents["propertySettings.phoneAndroidId"],
            "simSerial": contents["propertySettings.phoneSimSerial"],
            "macAddress": contents["propertySettings.macAddress"]
        }

        # Merge 2 json data
        contents = {**contents, **config}
        save_json_file(contents, f'leidian{i}.config', config_path)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

    return new_LDPlayer
