from pynput.mouse import Button, Listener, Controller
mouse = Controller()

def on_click(x, y, button, pressed):
    try:
        if pressed and button == Button.button9:
            mouse.click(Button.right, 1)
    except Exception as e:
        print('Error occurred:', e)
try:
    with Listener(on_click=on_click) as listener:
        listener.join()
except Exception as e:
    print('Error occurred:', e)