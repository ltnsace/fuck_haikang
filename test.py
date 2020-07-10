# encoding=utf8

from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

# 前台开启浏览器模式
def openChrome():
    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    option.add_argument('--window-size=1920x1080')  # 设置浏览器分辨率（窗口大小）
    # option.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错

    # 打开chrome浏览器
    driver = webdriver.Chrome(chrome_options=option)
    return driver

# 授权操作
def operationAuth(driver):
    url = "http://192.168.1.64/"
    driver.get(url)

    try:
        elem_pw = driver.find_elements_by_xpath("//input[@type='password']")
        for elem in elem_pw:
            elem.send_keys("Buchou123")
        # class="aui_state_highlight" class="aui_close"  placeholder="用户名"
        driver.find_element_by_xpath("//button[@class='aui_state_highlight']").click()
        driver.find_element_by_xpath("//a[class='aui_close']").click()
    except ElementNotVisibleException:
        print("已注册")
        driver.find_element_by_xpath("//input[@type='password']").clear()
    driver.find_element_by_xpath("//input[@type='password']").send_keys("Buchou123")
    driver.find_element_by_xpath("//input[@placeholder='用户名']").send_keys("admin")
    driver.find_element_by_xpath("//button").click()
    print("登陆成功")
    time.sleep(5)
    driver.find_element_by_xpath("//a[@ng-bind='oLan.config']").click()
    # yingshiyun(driver)
    region_cover(driver)
def advanced_setting(driver):

    driver.find_element_by_xpath("//span[@class='menu-icon network-icon']").click()
    driver.find_element_by_xpath("//span[@ng-bind='oMenuLan.advancedSettings']").click()
    time.sleep(2)
    print("选中高级设置")
    driver.find_element_by_xpath("//a[@id = 'ui-id-14']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//select[@ng-model='oParams.szAccessType']").click()
    driver.find_element_by_xpath("//option[@value='ezviz']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@ng-model='oParams.bEnableEzviz']").click()
    time.sleep(2)
    driver.find_elements_by_xpath("//input")[0].send_keys('12341234q')
    driver.find_elements_by_xpath("//input")[1].send_keys('12341234q')
    driver.find_element_by_xpath("//button[@class='aui_state_highlight']").click()
    driver.find_element_by_xpath("//button[@class='btn btn-primary btn-save']").click()
    # driver.find_element_by_xpath("")
    print("萤石云配置成功")


def region_cover(driver):
    driver.find_element_by_xpath("//span[@class='menu-icon image-icon']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//a[@ng-bind='oImageLan.privacyMask']").click()
    time.sleep(2)
    print("选中图像")
    driver.find_element_by_xpath('//input[@id="enableTemper"]').click()
    driver.find_element_by_xpath('//button[@ng-click="draw()"]').click()


    import win32gui
    import win32api
    import pyautogui
    # from pymouse import PyMouse
    hwnd_title = {}

    def get_all_hwnd(hwnd, mouse):
        if (win32gui.IsWindow(hwnd) and
                win32gui.IsWindowEnabled(hwnd) and
                win32gui.IsWindowVisible(hwnd)):
            hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

    win32gui.EnumWindows(get_all_hwnd, 0)

    # m = PyMouse()

    for h, t in hwnd_title.items():
        if t:
            print(h, t)
            if t == '配 置 - Google Chrome':
                left, top, right, bottom = win32gui.GetWindowRect(h)
                print(left, top, right, bottom)
                # 501.0/1814.0,544.0 / 1324.0
                # pyautogui.click(left + 450, top + 350)
                pyautogui.moveTo(left + int(501.0 / 1814.0 * float(right - left)),
                                 top + int(544.0 / 1324.0 * float(bottom - top)))
                time.sleep(1)
                pyautogui.dragTo(x=right, y=bottom)

# 方法主入口
if __name__ == '__main__':
    # 加启动配置
    driver = openChrome()
    operationAuth(driver)
