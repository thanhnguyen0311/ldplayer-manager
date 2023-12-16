import subprocess
import sys
import os
from constants.constants import LDCONSOLE_PATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

def reboot_ld(device):
    try:
        subprocess.call([LDCONSOLE_PATH] + ["reboot"] + ["--name"] + [device], shell=True)
        return True

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
