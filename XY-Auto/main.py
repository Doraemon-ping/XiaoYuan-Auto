import Image_words
import Img
import pygetwindow as gw
import config
import compare
import write
import keyboard
import time
xx = None


def start():

    target_window_title = 'BlueStacks'
    target_window = gw.getWindowsWithTitle(target_window_title)[0]
    window = target_window

#获取截图
    Img.take_screenshot(target_window)

#当前游戏坐标
    left = window.left
    top = window.top
    width = window.width
    height = window.height
    li = compare.get_Com()

    x = li[0]
    y = li[1]

    print("x:",x,"y:",y)

    if(x>y): write.draw_greater_than(left+200,top+600,25)
    if(x<y): write.draw_less_than(left+200,top+600,25)


while True:

    if(keyboard.is_pressed('space')):
        print('结束 ')
        break
    try:
            start()
            time.sleep(0.09)
    except Exception as e :
        print(...)
    finally:
        continue







