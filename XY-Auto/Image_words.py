import tr

def img(Path):
    crnn = tr.CRNN()                                # 初始化文本行识别网络
    chars, scores = crnn.run(Path)       # 识别文本行
    return ("".join(chars))    