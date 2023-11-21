import gzip
import base64
import json
from tkinter import Tk
import sys

try:
    jsond = json.loads(Tk().clipboard_get().replace(";", ":"))
except:
    print("Please click on the Copy text")
    sys.exit(1)
data = jsond["code"]

b = base64.b64decode(data)
r = json.loads(gzip.decompress(b).decode())

indents = 0
for i in r["blocks"]:
    isBlock = i["id"]
    ind = "\t" * indents
    if isBlock == "block":
        block = i["block"]
        if block in {"func", "process"}: # 2nd time i've used a set in any language
            btype = i["data"]
        else:
            btype = i["action"]
            print(f"\n{ind}{block}: {btype}", end=" ")
    else:
        if i["direct"] == "open":
            print(" {", end=" ")
            indents += 1
        else:
            indents -= 1
            ind = "\t" * indents
            print(f"\n{ind}}}", end="")