import time
import Img
import config
import Image_words
import write
import keyboard
import pyautogui

def get_Com(xx,left,top):
    Img.get_XY(config.x1,config.y1,config.xx1,config.yy1,"X.png")
    Img.get_XY(config.x2,config.y2,config.xx2,config.yy2,"Y.png")

    x = int(Image_words.img("XY-Auto\\images\\X.png"))
    y = int(Image_words.img("XY-Auto\\images\\Y.png"))

    if(x>y and xx!=x):
        write.greater_(left+217,top+962)
        #pyautogui.press("A")
        print(x,">",y)
        #time.sleep(0.1)
    if(x<y and xx!=x) :
        write.less_(left+217,top+962)
       # keyboard.press('D')
        #pyautogui.press("D") # 脚本快捷键,用于BlueStacks脚本管理器，这个是大于号的
        #time.sleep(0.1)


        print(x,"<",y)
    xx = x 



    