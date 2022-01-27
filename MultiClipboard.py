import sys
import clipboard
import json

from enum import Enum
class modeEnum(Enum):
    DINGUS = 0
    SAVE = 1
    PASTE = 2
    LIST = 3

mode = modeEnum.DINGUS

if len(sys.argv) == 2:
    cmnd = sys.argv[1]

    if cmnd[0] in ['s', 'S', 'save', 'Save']:
        mode = modeEnum.SAVE
    elif cmnd[0] in ['p', 'P', 'paste', 'Paste']:
        mode = modeEnum.PASTE
    elif cmnd[0] in ['l', 'L', 'list', 'List']:
        mode = modeEnum.LIST

if mode is modeEnum.DINGUS: raise ValueError("Not a valid mode [save, paste, list]")
print("helloWorld ya dingus")