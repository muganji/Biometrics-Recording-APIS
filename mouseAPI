# -*- customized recording API -*-
import mouse
import keyboard
import json
import sys

##class_by_name = {
##	'ButtonEvent': mouse.ButtonEvent,
##	'WheelEvent': mouse.WheelEvent,
##	'MoveEvent': mouse.MoveEvent,
##}
MouseDynamics = []
'''
Records every event from a user
'''
def record_events(event):
	# Could use json.dumps(event.__dict__()), but this way we guarantee semantic order.
	d = event._asdict()
	d['event_class'] = event.__class__.__name__
	MouseDynamics.append(json.dumps(d))
	sys.stdout.flush()
'''
Hooks all keyboard events
'''
def hook_events():
    mouse.hook(record_events)
    keyboard.wait('esc')
    mouse.unhook_all()

'''
Returns all captured events
'''
def get_data():
    return MouseDynamics



#mouse.play(load(line) for line in fileinput.input())
