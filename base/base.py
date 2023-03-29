# from selenium import webdriver 是否可以不用待确认，导入到get_driver.py
import time
from selenium.webdriver.support.wait import WebDriverWait
from tool.get_log import GetLogger

log = GetLogger().get_logger()


class Base:
    # 初始化
    def __init__(self, driver):
        log.info("初始化driver：{}".format(driver))
        self.driver = driver

    # 查找元素方法 (提供：点击、输入、获取文本)使用
    def base_find_element(self, loc, timeout=30, poll=0.5):
        log.info("正在查找元素：{}".format(loc))
        # 显示等待
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))
    """
    :param loc:  元素的定位信息，格式为元祖
    :param timeout: 默认超时时间30秒
    :param poll: 访问频率，默认0.5查找一次元素
    :return: 返回查找到的元素
    """
    # 点击元素 方法封装
    def base_click(self, loc):
        log.info("点击元素：{}".format(loc))
        self.base_find_element(loc).click()

    # 输入元素 方法封装
    def base_input(self, loc, value):
        log.info("导入元素：{}".format(loc,value))
        # 获取元素
        el = self.base_find_element(loc)
        log.info("获取元素：{}".format(loc))
        # 清空
        el.clear()
        log.info("清空元素：{}".format(loc))
        # 输入
        el.send_keys(value)
        log.info("输入元素：{}".format(value))

    # 获取value属性方法封装
    def base_get_value(self, loc):
        # 使用get_attribute()方法获取指定的元素属性值
        # 注意：返回
        return self.base_find_element(loc).get_attribute("value")

    # 获取文本信息 方法封装
    def base_get_text(self, loc):
        # 注意：一定要返回元素的文本信息
        return self.base_find_element(loc).text

    # 截图方法封装
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 封装判断元素是否存在 方法封装
    def base_if_exist(self, loc):
        try:
            self.base_find_element(loc, timeout=2)
            # 找到元素  aseertTrue
            return True
        except Exception:
            # 没找到元素
            return False
