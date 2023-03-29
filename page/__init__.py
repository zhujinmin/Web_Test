from tool.read_json import read_html
from selenium.webdriver.common.by import By


# 获取WEB项目地址
class GetUrl:
    data = read_html("html.json")
    # print(data)

    def get_value(self, daihao):
        return self.data[daihao]


url = GetUrl()
url = url.get_value('url')
print(url)


# url = "http://localhost"


"""以下为登录页面元素配置信息"""
# 首页提示确认
login_sure_popup = By.ID, "sure-popup"
# 登录链接
login_link = By.PARTIAL_LINK_TEXT, "登录"
# 用户名
login_username = By.ID, "username"
# 密码
login_pwd = By.ID, "password"
# 验证码
login_verify_code = By.ID, "verify_code"
# 选择框勾选
login_checkbox = By.ID, "remember_password"
# 登录按钮
login_btn = By.CLASS_NAME, "login_button"
# login_btn = By.CSS_SELECTOR, ".J-login-submit"
# 获取异常文本信息
login_err_info = By.CSS_SELECTOR, ".layui-layer-content"
# 点击异常提示框 按钮
login_err_btn_ok = By.CSS_SELECTOR, ".layui-layer-btn0"
# 安全退出
login_logout = By.PARTIAL_LINK_TEXT, "安全退出"

"""以下为订单页面配置数据"""
