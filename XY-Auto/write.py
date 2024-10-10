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


def draw_greater(x, y):
    # 等待几秒以便你可以切换到绘图窗口

    # 移动到起始位置并点击
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()

    # 绘制大于号形状
    pyautogui.move(20, 0)    # 向右
    pyautogui.move(20, 20)   # 向下右
    pyautogui.move(0, 20)    # 向下
    pyautogui.move(-20, 20)  # 向左下
    pyautogui.move(-20, 0)   # 向左
    pyautogui.move(0, -20)   # 向上左
    pyautogui.move(20, -20)  # 向上右

    # 释放鼠标
    pyautogui.mouseUp()


def draw_less(x, y):
    # 等待几秒以便你可以切换到绘图窗口
    # 移动到起始位置并点击
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()

    # 绘制小于号形状
    pyautogui.move(-20, 0)    # 向左
    pyautogui.move(-20, 20)   # 向下左
    pyautogui.move(0, 20)      # 向下
    pyautogui.move(20, 20)     # 向右下
    pyautogui.move(20, 0)      # 向右
    pyautogui.move(0, -20)     # 向上右
    pyautogui.move(-20, -20)   # 向上左

    # 释放鼠标
    pyautogui.mouseUp()

# 调用函数并传入坐标