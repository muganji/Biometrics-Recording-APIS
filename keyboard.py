# -*- customized recording API -*-
import keyboard
import json
import sys


keystrokesDynamics = []
'''
Records every event from a user
'''
def record_events(event):
    keystrokesDynamics.append(event.to_json(ensure_ascii=sys.stdout.encoding != 'utf-8'))
    sys.stdout.flush()
'''
Hooks all keyboard events
'''
def hook_events():
    keyboard.hook(record_events)
    keyboard.wait('esc')
    keyboard.unhook_all()

'''
Returns all captured events
'''
def get_data():
    return keystrokesDynamics


hook_events()



