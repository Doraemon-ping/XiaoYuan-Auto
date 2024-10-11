import Image_words
import Img
import pygetwindow as gw
import config
import compare
import write
import keyboard
import time
import adb

xx = 0

#比大小
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
    global xx
    compare.get_Com(xx,left=left,top=top)
    print("解题完成！")

def company():
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

    Img.get_XY(left+50,top+300,left+450,top+510,'com.png')
             
    s = Image_words.img("XY-Auto\\images\\com.png")
    s = s.replace('×','*')
    s = s.replace('=','')
    print (s)
    res = eval(s)

    print("计算结果：",res)

    adb.draw_decimal(res,x=left+40,y=top+800)



print(1)

while True:
    if(keyboard.is_pressed('space')):
        break
    try:
        start()
        #adb.swipe_screen('<',base_resolution=(720,1280))
        
    except Exception as e :
        print(e)
        time.sleep(0.1)
        write.click(config.shouxia_x,config.shouxia_y)
        write.click(config.jixu_x,config.jixu_y)
        write.click(config.zilai_x,config.zilai_y)
    finally:
        continue