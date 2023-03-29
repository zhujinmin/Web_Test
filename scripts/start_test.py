"""
    目标：基于unittest框架执行生成html版报告
    操作：
        1. 复制HTMLTestRunner.py到tool文件夹内
        2. 导包 from HTMLTestRunner import HTMLTestRunner
        3. 获取报告存放文件流，并实例化HTMLTestRunner类，执行run方法
"""
# 导包
import unittest

import time
from tool.read_json import read_html
from tool.HTMLTestRunner import HTMLTestRunner


class GetName:
    data = read_html("html.json")
    # print(data)

    def get_value(self, daihao):
        return self.data[daihao]


P_name = GetName()
p_name = P_name.get_value('project_name')
print(p_name)


# 定义 测试套件
# suite = unittest.defaultTestLoader.discover("../scripts", pattern="test*.py")
suite = unittest.defaultTestLoader.discover("../scripts", pattern="test*.py")
# 定义报告存放路径及文件名称
report_dir = "../report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))
# report_dir = f"../report/{time.strftime('%Y_%m_%d %H_%M_%S')}.html"  #与上面功能一样
# 获取报告文件流 并执行
with open(report_dir, "wb") as f:
    HTMLTestRunner(stream=f,
                   title=p_name,
                   description="操作系统 win10").run(suite)

# 定义 测试套件
