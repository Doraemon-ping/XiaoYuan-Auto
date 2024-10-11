import pyautogui

def draw_greater_than(origin_x, origin_y, size):
    pyautogui.mouseDown(origin_x, origin_y)
    pyautogui.moveTo(origin_x + size, origin_y + size, duration=0.02)
    pyautogui.moveTo(origin_x, origin_y + size, duration=0.02)
    pyautogui.mouseUp()

def draw_less_than(origin_x, origin_y, size):
    pyautogui.mouseDown(origin_x + size, origin_y)
    pyautogui.moveTo(origin_x, origin_y + size, duration=0.02)
    pyautogui.moveTo(origin_x + size, origin_y + size, duration=0.02)
    pyautogui.mouseUp()

def greater_(x,y):
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    pyautogui.moveRel(10, 10, duration=0.05)
    pyautogui.mouseDown()
    pyautogui.moveRel(-10, 10, duration=0.05)
    pyautogui.mouseUp()

def less_(x,y):
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    pyautogui.moveRel(-10, 10, duration=0.05)
    pyautogui.mouseDown()
    pyautogui.moveRel(10, 10, duration=0.05)
    pyautogui.mouseUp()

def click(x,y):
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
