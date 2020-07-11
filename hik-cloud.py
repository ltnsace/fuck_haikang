# https://www.hik-cloud.com/chain/login/index.html#/login

# 显示等待
# https://www.cnblogs.com/syayy/p/11720256.html

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
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


def init(driver):
    url = "https://www.hik-cloud.com/chain/login/index.html#/login"
    driver.get(url)
    driver.implicitly_wait(5)
    # driver.quit()
    # 输入用户名和密码
    driver.find_element_by_xpath("//input[@placeholder='请输入用户名']").send_keys("13792886247")
    driver.find_element_by_xpath("//input[@type='password']").send_keys("Buchou@0306")
    driver.find_element_by_xpath("//button").click()
    print("登录中....")
    driver.find_element_by_id("HKAppSceanPage").click()
    print("登录成功")
    # driver.find_elements_by_xpath("//span[@class='el-menu-item--text']").click()
    driver.find_element_by_css_selector(".el-menu-item--text").click()

# 方法主入口
if __name__ == '__main__':
    # 加启动配置
    driver = openChrome()
    init(driver)
