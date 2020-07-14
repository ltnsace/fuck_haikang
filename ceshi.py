import win32gui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import win32gui
import sys
hwnd_title = {}
def get_all_hwnd(hwnd, mouse):
    if (win32gui.IsWindow(hwnd) and
            win32gui.IsWindowEnabled(hwnd) and
            win32gui.IsWindowVisible(hwnd)):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


win32gui.EnumWindows(get_all_hwnd, 0)

for h, t in hwnd_title.items():
    if t:
        print(h, t)
        if t == '雷电模拟器':
            left, top, right, bottom = win32gui.GetWindowRect(h)
            print(left, top, right, bottom)

hwnd = win32gui.FindWindow(None, '雷电模拟器')
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
img = screen.grabWindow(hwnd).toImage()
img.save("screenshotxxx.jpg")