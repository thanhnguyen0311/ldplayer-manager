import subprocess
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from constants.constants import LDCONSOLE_PATH

def quit_all():
    try:
        subprocess.run([LDCONSOLE_PATH] + ["quitall"], shell=True)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def quit_ld(device):
    try:
        subprocess.run([LDCONSOLE_PATH] + ["quit","--name",device], shell=True)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
