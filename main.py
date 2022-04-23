from multiprocessing.connection import Listener
from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
"""from pynput import keyboard

class MyException(Exception): pass

def on_press(key):
    if key == keyboard.Key.esc:
        raise MyException(key)

# Collect events until released
with keyboard.Listener(
        on_press=on_press) as listener:
    try:
        listener.join()
    except MyException as e:
        print('{0} was pressed'.format(e.args[0]))"""

"""from pynput import mouse

# The event listener will be running in this block
with mouse.Events() as events:
    # Block at most one second
    event = events.get(1.0)
    if event is None:
        print('You did not interact with the mouse within one second')
    else:
        print('Received event {}'.format(event))



# The event listener will be running in this block
with mouse.Events() as events:
    for event in events:
        if event.button == mouse.Button.right:
            break
        else:
            print('Received event {}'.format(event))

from pynput import mouse

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()

from pynput import mouse

def on_click(x, y,button,pressed):
    if pressed:
        print(str(button)+" pressed("+str(x)+", "+str(y)+")")
    else:
        print(str(button)+" released at ("+str(x)+", "+str(y)+")")

with mouse.Listener(
    on_click=on_click
) as Listener:
listener.join()   

from pynput import mouse

def on_click(x, y,button,pressed):
    if pressed:
        print(str(button)+" pressed("+str(x)+", "+str(y)+")")
    else:
        print(str(button)+" released at ("+str(x)+", "+str(y)+")")

with mouse.Listener(
    on_click=on_click) as listener:

    listener.join()


listener = mouse.Listener(
    #on_press=on_press,
    #on_release=on_release
    on_click=on_click)
listener.start()"""

