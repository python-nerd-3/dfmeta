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
        elif block == "else":
            print(f"\n{ind} else", end="")
        else:
            btype = i["action"]
            allItems = i["args"]["items"]
            items = list(filter((lambda j: j["item"]["id"] != "bl_tag"), allItems))
            tags = list(filter((lambda j: j["item"]["id"] == "bl_tag"), allItems))
            items.sort(key=(lambda j: j["slot"]))
            tags.sort(key=(lambda j: j["slot"]))
            # below is the longest lambda known to man
            itemDisps = list(map((lambda j: j["item"]["id"] + " | " +  (j["item"]["data"]["name"] if j["item"]["id"] != "item" else j["item"]["data"]["item"][(j["item"]["data"]["item"].find("id:") + 3):j["item"]["data"]["item"].find(",tag")])), items))
            tagDisps = list(map(lambda j: j["item"]["data"]["tag"] + ": " + j["item"]["data"]["option"], tags))
            itemDisps = str(itemDisps).replace("'", "")
            if len(tagDisps) == 0:
                tagDisps = ""
            else: 
                tagDisps = str(tagDisps).replace("'", "")
            print(f"\n{ind}{block}: {btype} {itemDisps} {tagDisps}", end=" ")
    else:
        if i["direct"] == "open":
            print(" {", end=" ")
            indents += 1
        else:
            indents -= 1
            ind = "\t" * indents
            print(f"\n{ind}}}", end="")