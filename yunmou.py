
# encoding=utf8
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

# 前台开启浏览器模式


def yunmou():

    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')

    # 打开chrome浏览器
    driver = webdriver.Chrome(chrome_options=option)
    url ="https://www.hik-cloud.com/chain/login/index.html#/login"
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_xpath('//input[@placeholder="请输入用户名"]').send_keys("13792886247")
    driver.find_element_by_xpath('//input[@placeholder="请输入密码"]').send_keys("Buchou@0306")
    driver.find_element_by_xpath('//div[@class="login-btn-div"]').click()
    time.sleep(3)
    try:
        driver.find_element_by_xpath('//button[@class="el-button el-button--default el-button--primary "]').click()
    except Exception :
        print("未获取到")
        driver.find_element_by_xpath('//div[@class="login-btn-div"]').click()
    time.sleep(5)
    url='https://www.hik-cloud.com/chainX/index.html#/system/equipment/management'
    driver.get(url)
    title='玖瑞'

    driver.find_element_by_xpath('//i[@class="h-icon-add"]').click()
    input()


# 方法主入口
if __name__ == '__main__':
    yunmou()