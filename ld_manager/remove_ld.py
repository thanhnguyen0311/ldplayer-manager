import subprocess
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from constants.constants import LDCONSOLE_PATH
from get_list_ld import get_list_ld

def remove_ld(device_name):
    try:
        subprocess.run([LDCONSOLE_PATH] + ["remove","--name",device_name], shell=True)
        return True 

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
    
def remove_all_ld():
    ld_list = get_list_ld()

    for i in ld_list: 
        try:
            subprocess.run([LDCONSOLE_PATH] + ["remove","--name",i['name']], shell=True)

        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            return False
        
    return True
        
