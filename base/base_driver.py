from appium import webdriver


def init_driver():
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'  # 系统名
    desired_caps['platformVersion'] = '5.1'  # 版本名
    desired_caps['deviceName'] = '192.168.56.101:5555'  # 设备名
    # app信息
    desired_caps['appPackage'] = 'com.android.settings'  # 包名
    desired_caps['appActivity'] = '.Settings'  # 启动名
    # 下两条是获取中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True

    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
