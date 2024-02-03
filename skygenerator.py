import gzip
import base64

r = b"""{'blocks': [{'id': 'block', 'block': 'event', 'args': {'items': []}, 'action': 'BreakBlock'}, {'id': 'block', 'block': 'if_player', 'args': {'items': [{'item': {'id': 'item', 'data': {'item': '{Count:1b,DF_NBT:3578,id:"minecraft:oak_log"}'}}, 'slot': 0}, {'item': {'id': 'bl_tag', 'data': {'option': 'Ignore fluids', 'tag': 'Fluid Mode', 'action': 'IsLookingAt', 'block': 'if_player'}}, 'slot': 26}]}, 'action': 'IsLookingAt'}, {'id': 'bracket', 'direct': 'open', 'type': 'norm'}, {'id': 'block', 'block': 'player_action', 'args': {'items': [{'item': {'id': 'item', 'data': {'item': '{Count:1b,DF_NBT:3578,id:"minecraft:oak_log"}'}}, 'slot': 0}]}, 'action': 'GiveItems'}, {'id': 'bracket', 'direct': 'close', 'type': 'norm'}]}"""

encrypted = gzip.compress(r)
encrypted = base64.b64encode(r).decode()
i = len(encrypted)
l = len(encrypted)
ind = 0
print("@startinput \n")
while i >= 0:
    ind += 1 
    s = l - i
    e = s + 255
    print(f"{ind}:")
    print("@" + encrypted[s:e])
    i -= 255
print("\n @endinput")