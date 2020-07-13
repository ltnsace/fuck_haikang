# 不愁养添加摄像头脚本
# 不愁养添加摄像头脚本
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
    #option.add_argument('--window-size=1920x1080')  # 设置浏览器分辨率（窗口大小）
    option.add_argument('--start-maximized')  # 最大化运行（全屏窗口）,不设置，取元素会报错

    # 打开chrome浏览器
    driver = webdriver.Chrome(options=option)
    return driver

# 授权操作
def operationAuth(driver):
    url = "http://aicam.mybuchou.com/login.do;JSESSIONID=45fe41e4-b86d-41c6-9fe7-d90d43f8f0b0"
    driver.get(url)
    # try:
    #     elem_pw = driver.find_elements_by_xpath("//input[@type='password']")
    #     for elem in elem_pw:
    #         elem.send_keys("Buchou123")
    #     # class="aui_state_highlight" class="aui_close"  placeholder="用户名"
    #     driver.find_element_by_xpath("//button[@class='aui_state_highlight']").click()
    #     driver.find_element_by_xpath("//a[class='aui_close']").click()
    # except ElementNotVisibleException:
    #     print("已注册")
    #     driver.find_element_by_xpath("//input[@type='password']").clear()
    driver.find_element_by_xpath("//input[@id='g001']").send_keys("10133")
    driver.find_element_by_xpath("//input[@id='loginName']").send_keys("admin10133")
    driver.find_element_by_xpath("//input[@id='password']").send_keys("111")
    print("请输入验证码：")
    # 手动输入验证码
    security_code = input()
    time.sleep(1)
    driver.find_element_by_xpath("//input[@name='passKey']").send_keys(security_code)
    driver.find_element_by_xpath('//button[@class="submit-btn"]').click()
    print("登陆成功")
    time.sleep(1)
def add_room(driver):
    print("开始注册栋舍")
    #driver.find_element_by_xpath('//a[@class="menu-toggler"]').click()
    driver.find_element_by_xpath('//i[@class="icon-flickr"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//li[@id="2477"]').click()
    #进入iframe
    #iframe = driver.find_element_by_xpath('//iframe[@id="iframepage"]')
    driver.switch_to.frame(1)
    time.sleep(2)
    #driver.find_elements_by_id('toolbar').click()
    driver.find_element_by_xpath('//div[@id="toolbar"]/button[1]').click()
    driver.switch_to_default_content()
    driver.switch_to.frame(2)
    time.sleep(2)
    driver.find_element_by_xpath('//input[@id="farmerName"]').click()
    driver.switch_to_default_content()
    driver.switch_to.frame('OpentreeDialog')
    time.sleep(2)
    driver.find_element_by_xpath('//input[@id="name"]').send_keys("测试")
    time.sleep(1)
    try:
        driver.find_element_by_xpath('//input[@data-index="0"]').click()
    except ElementNotVisibleException:
        print("联系管理员添加养户，开始注册下一个养户栋舍")
        return 0
    driver.switch_to_default_content()
    driver.find_element_by_xpath('//button[@class="aui_state_highlight"]').click()
    driver.switch_to.frame(2)
    time.sleep(2)
    driver.find_element_by_xpath('//input[@id="name"]').send_keys("测试")
    driver.find_element_by_xpath('//input[@id="iot1"]').send_keys("ceshi001")
    driver.find_element_by_xpath('//input[@name="save"]').click()
    driver.switch_to_default_content()
    driver.find_element_by_xpath('//button[@class="aui_state_highlight"]').click()
    time.sleep(1)
    return 1

def add_camera(driver):
    print("开始注册摄像头")
    driver.find_element_by_xpath('//i[@class="icon-eye-open"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//li[@id="2501"]').click()
    driver.switch_to.frame(1)
    time.sleep(2)
    driver.find_element_by_xpath('//div[@id="toolbar"]/button[1]').click()
    driver.switch_to_default_content()
    driver.switch_to.frame(2)
    time.sleep(2)
    driver.find_element_by_xpath('//input[@id="farmerName"]').click()
    driver.switch_to_default_content()
    driver.switch_to.frame('OpentreeDialog')
    time.sleep(2)
    driver.find_element_by_xpath('//input[@id="name"]').send_keys("测试")
    time.sleep(1)
    driver.find_element_by_xpath('//input[@data-index="0"]').click()
    driver.switch_to_default_content()
    driver.find_element_by_xpath('//button[@class="aui_state_highlight"]').click()
    driver.switch_to.frame(2)
    time.sleep(2)
    driver.find_element_by_xpath('//select[@id="farmid"]').click()
    driver.find_element_by_xpath('//option[@value="4fad63dfd12a46049f7c4061b7af1ddd"]').click()
    driver.find_element_by_xpath('//input[@id="controlposition"]').send_keys("门口")
    driver.find_element_by_xpath('//input[@id="code"]').send_keys("123")
    driver.find_element_by_xpath('//select[@id="aitype"]').click()
    driver.find_element_by_xpath('//input[@id="versioncode"]').send_keys("1.0.0")
    driver.find_element_by_xpath('//option[@value="2"]').click()
    driver.find_element_by_xpath('//select[@id="autopush"]').click()
    driver.find_element_by_xpath('//select[@id="autopush"]/option[2]').click()
    driver.find_element_by_xpath('//input[@name="save"]').click()
    driver.switch_to_default_content()
    time.sleep(1)
    driver.find_element_by_xpath('//button[@class="aui_state_highlight"]').click()
    time.sleep(1)
if __name__ == '__main__':
    # 加启动配置
    driver = openChrome()
    operationAuth(driver)
    #账号字典库
    account={"测试":['10133','admin10133','111']}
    for i in range(10):
        if add_room(driver)==0:
            break
    add_camera(driver)
