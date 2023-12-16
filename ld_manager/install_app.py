import subprocess
import sys
import os
from constants.constants import LDCONSOLE_PATH

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def install_app(app_package_name, name_ld):
    try:
        subprocess.call(
            [LDCONSOLE_PATH] + ["installapp"] + ["--name"] + [name_ld] + ["--packagename"] + [app_package_name],
            shell=True)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
