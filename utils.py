import os
import subprocess
from subprocess import PIPE

def coloredString(message):
    if ':allowed to' in message:
        ReturnStr = '```diff\n+ {}\n```'.format(message)
    if ':denied to' in message:
        ReturnStr = '```diff\n- {}\n```'.format(message)
    if 'Did not receive' in message:
        ReturnStr = '```diff\n- {}\n```'.format(message)
    return ReturnStr

def commandWho():
    result = (subprocess.Popen(
        'who',
        stdout=subprocess.PIPE,
        shell=True
        ).communicate()[0]).decode('utf-8')
    if not result:
        return 'None'
    else:
        return result

def commandCheckAuth():
    result = (subprocess.run(
        "sh sshlogin_notify.sh",
        shell=True,
        stdout=PIPE,
        stderr=PIPE,
        universal_newlines=True
        )).stdout
    return result

def findFile(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            print(True)
            return True
        else:
            return False
    else:
        return False
