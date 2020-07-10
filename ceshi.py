# import win32gui
# import pyautogui
# # from pymouse import PyMouse
# import time
# hwnd_title = {}
#
# def get_all_hwnd(hwnd, mouse):
#     if (win32gui.IsWindow(hwnd) and
#             win32gui.IsWindowEnabled(hwnd) and
#             win32gui.IsWindowVisible(hwnd)):
#         hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
#
# win32gui.EnumWindows(get_all_hwnd, 0)
#
# # m = PyMouse()
#
# for h, t in hwnd_title.items():
#     if t:
#         print(t)
#         if t == 'WindowControl':
#             left, top, right, bottom = win32gui.GetWindowRect(h)
#             print(left, top, right, bottom)
#             from pymouse import PyMouse
#
#             # m = PyMouse()
#             #
#             # m.press(left + int(550.0 / 1814.0 * float(right - left)),
#             #                  top + int(544.0 / 1324.0 * float(bottom - top)))
#             #
#             # m.release(left + int(550.0 / 1814.0 * float(right - left))+300,
#             #                  top + int(544.0 / 1324.0 * float(bottom - top))+100)
#             pyautogui.click(left + int(501.0 / 1814.0 * float(right - left)),
#                              top + int(544.0 / 1324.0 * float(bottom - top)))
#             pyautogui.moveTo(left + int(541.0 / 1814.0 * float(right - left)),
#                              top + int(544.0 / 1324.0 * float(bottom - top)))
#             time.sleep(5)
#             pyautogui.dragTo(x=right-100, y=bottom-100,duration=2)
#             # pyautogui.click(left + int(501.0 / 1814.0 * float(right - left)),
#             #                  top + int(544.0 / 1324.0 * float(bottom - top)))
#             # pyautogui.moveTo(x=right, y=bottom)
#             # pyautogui.click(x=right, y=bottom)


import time
from ctypes import windll
import sys
import ctypes


# 管理员登录
def is_admin():
    try:
        return windll.shell32.IsUserAnAdmin()
    except:
        return False


def admin_run():
    if is_admin():

        InputPasswordUtil().dd_mo_cli(494, 502)
        time.sleep(1)
        InputPasswordUtil().type('kong199701')
        time.sleep(1)
        InputPasswordUtil().dd_mo_cli(515,586)
        time.sleep(2)
    else:
        if sys.version_info[0] == 3:
            windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


# 隐藏黑窗口
def hide_cmd():
    whnd = ctypes.windll.kernel32.GetConsoleWindow()
    if whnd != 0:
        ctypes.windll.user32.ShowWindow(whnd, 0)
        ctypes.windll.kernel32.CloseHandle(whnd)


# 驱动级键盘鼠标操作
class InputPasswordUtil():
    """
        模拟键盘输入密码内容
    """

    def __init__(self):
        self.vk = {
            '5': 205, 'c': 503, 'n': 506, 'z': 501, '3': 203, '1': 201, 'd': 403, '0': 210, 'l': 409, '8': 208,
            'w': 302, 'u': 307, '4': 204, 'e': 303, '[': 311, 'f': 404, 'y': 306, 'x': 502, 'g': 405, 'v': 504,
            'r': 304, 'i': 308, 'a': 401, 'm': 507, 'h': 406, '.': 509, ',': 508, ']': 312, '/': 510, '6': 206,
            '2': 202, 'b': 505, 'k': 408, '7': 207, 'q': 301, "'": 411, '\\': 313, 'j': 407, '`': 200, '9': 209,
            'p': 310, 'o': 309, 't': 305, '-': 211, '=': 212, 's': 402, ';': 410
        }

        # 需要组合shift的按键。
        self.vk2 = {
            '"': "'", '#': '3', ')': '0', '^': '6', '?': '/', '>': '.', '<': ',', '+': '=', '*': '8', '&': '7',
            '{': '[', '_': '-', '|': '\\', '~': '`', ':': ';', '$': '4', '}': ']', '%': '5', '@': '2', '!': '1',
            '(': '9'
        }

        self.dd_dll = windll.LoadLibrary("DD94687.64.dll")

    def down_up(self, code):
        print("简码:", code, self.vk[code])
        self.dd_dll.DD_key(self.vk[code], 1)
        # time.sleep(0.5)
        self.dd_dll.DD_key(self.vk[code], 2)

    def dd(self, key):
        if key.isupper():
            # 按下 500是shift键码
            self.dd_dll.DD_key(500, 1)
            self.down_up(key.lower())
            self.dd_dll.DD_key(500, 2)

        elif key in r'~!@#$%^&*()_+{}|:"<>?':
            self.dd_dll.DD_key(500, 1)
            self.down_up(self.vk2[key])
            self.dd_dll.DD_key(500, 2)
        else:
            self.down_up(key)

    def type(self, password):
        # 依次输入密码字符
        for key in password:
            # print(key)
            self.dd(str(key))
            time.sleep(0.5)

    def dd_mo_cli(self, x, y):
        self.dd_dll.DD_mov(x, y)
        self.dd_dll.DD_btn(1)
        self.dd_dll.DD_btn(2)

    def t_str(self):
        # self.dd_dll.DD_str("ddd")
        self.dd_dll.DD_key(0x30, 1)
        self.dd_dll.DD_key(0x30, 2)


if __name__ == '__main__':

    if is_admin():
        hide_cmd()
        InputPasswordUtil().dd_mo_cli(583, 460)
        time.sleep(1)
        InputPasswordUtil().type('kong199701')
        time.sleep(1)
        # InputPasswordUtil().dd_mo_cli(518, 562)
        # time.sleep(2)
    else:
        if sys.version_info[0] == 3:
            windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)


# 1. DD_btn(参数)
# 功能： 模拟鼠标点击
# 参数： 1 =左键按下 ，2 =左键放开
# 4 =右键按下 ，8 =右键放开
# 16 =中键按下 ，32 =中键放开
# 64 =4键按下 ，128 =4键放开
# 256 =5键按下 ，512 =5键放开
# 例子：模拟鼠标右键 只需要连写(中间可添加延迟) dd_btn(4); dd_btn(8);
#
#
# 2. DD_mov(参数x,参数y)
# 功能： 模拟鼠标结对移动
# 参数： 参数x , 参数y 以屏幕左上角为原点。
# 例子： 把鼠标移动到分辨率1920*1080 的屏幕正中间，
# int x = 1920/2 ; int y = 1080/2;
# DD_mov(x,y) ;1234567890
#
#
#
# 3. DD_movR(参数dx,参数dy)
# 功能： 模拟鼠标相对移动
# 参数： 参数dx , 参数dy 以当前坐标为原点。
# 例子： 把鼠标向左移动10像素
# DD_movR(-10,0) ;
#
#
#
# 4. DD_whl(参数)
# 功能: 模拟鼠标滚轮
# 参数: 1=前 , 2 = 后
# 例子: 向前滚一格, DD_whl(1)
#
#
#
# 5. DD_key(参数1，参数2)
# 功能： 模拟键盘按键
# 参数： 参数1 ，请查看[DD虚拟键盘码表]。
# 参数2，1=按下，2=放开
# 例子： 模拟单键WIN，
# DD_key(601, 1);DD_key(601, 2);
#     组合键：ctrl+alt+del
#     DD_key(600,1);
#     DD_key(602,1);
#     DD_key(706,1);
#     DD_key(706,2);
#     DD_key(602,2);
#     DD_key(600,2);
#
#
#
# 6. DD_str(参数)
# 功能： 直接输入键盘上可见字符和空格
# 参数： 字符串, (注意，这个参数不是int32 类型)
# 例子： DD_str("MyEmail@aa.bb.cc !@#$")