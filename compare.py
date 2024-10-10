import Img
import config
import Image_words


def get_Com():
    Img.get_XY(config.x1,config.y1,config.xx1,config.yy1,"X.png")
    Img.get_XY(config.x2,config.y2,config.xx2,config.yy2,"Y.png")
    x = int(Image_words.img("XY-Auto\\images\\X.png"))
    y = int(Image_words.img("XY-Auto\\images\\Y.png"))
    list = [x,y]
    #print(list)
    return list    