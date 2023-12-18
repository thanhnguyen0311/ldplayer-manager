import subprocess
import sys
import os
from constants.constants import LDCONSOLE_PATH
from ld_manager.get_list_ld import get_list_ld

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def remove_ld(device_name):
    try:
        subprocess.run([LDCONSOLE_PATH] + ["remove", "--name", device_name], shell=True)
        return True

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False


def remove_all_ld():
    ld_list = get_list_ld()

    for device in ld_list:
        try:
            subprocess.run([LDCONSOLE_PATH] + ["remove", "--name", device.name], shell=True)

        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            return False

    return True
