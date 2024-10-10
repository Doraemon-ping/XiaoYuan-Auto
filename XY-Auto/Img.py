import pygetwindow as gw
from PIL import ImageGrab
from PIL import Image
import pyautogui


#截屏任意位置
def take_screenshot(window):
    # 窗口边界
    left = window.left
    top = window.top
    width = window.width
    height = window.height

    # 截图
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    # 保存截图
    save_screenshot(screenshot,"1.png")
    print("截图已保存为 window_screenshot.png")


# 打开指定窗口
def open_window(window_name):
    window = gw.getWindowsWithTitle(window_name)[0]
    window.activate()

# 截取窗口截屏
def capture_screen():
    screenshot = ImageGrab.grab()
    return screenshot

# 保存截屏图片
def save_screenshot(image, file_name):
    path = 'XY-Auto\\images\\'
    image.save(path+file_name)

# 测试代码
def get():
    Window_name = 'BlueStacks'
    open_window(window_name=Window_name)
# 截取窗口截屏
    screenshot = capture_screen()
    #裁剪
    screenshot=screenshot.crop((0,0,826,1433))
    # 保存截屏图片
    save_screenshot(screenshot, "1.png")

def get_XY(x1,y1,x2,y2,name):
    img = Image.open('XY-Auto\\images\\1.png')
    imgc = img.crop((x1,y1,x2,y2))
    save_screenshot(imgc,name)
    