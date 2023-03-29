# 导包
import time
import logging.handlers


# 注意以后导logging包，不在使用此方式 import logging
# 导包时 导入 import logging.handlers
# 推荐：原因 logging是包名，导入包名时会自动执行包下面的__init__文件，所以这样导入，相当于导入 logging
# handlers为模块名称


class GetLogger:
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            # 获取 日志器
            cls.logger = logging.getLogger()
            # 设置 日志器 级别
            cls.logger.setLevel(logging.INFO)

            # 获取处理器 控制台
            sh = logging.StreamHandler()
            # 获取处理器 文件-以时间分隔
            th = logging.handlers.TimedRotatingFileHandler(filename=f"../log/log{time.strftime('%Y_%m_%d %H_%M_%S')}.log",
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=30,
                                                           encoding="utf-8")
            # 设置格式器：设置默认的输入日志格式
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到 处理器 控制台
            sh.setFormatter(fm)
            # 将格式器添加到 处理器 文件
            th.setFormatter(fm)
            # 将处理器添加到 日志器
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
        return cls.logger


# # 调用 指定级别，输入日志信息
# if __name__ == '__main__':
#     logger = GetLogger().get_logger()
#     logger.debug("debug信息被执行")
#     logger.info("info信息被执行")
#     logger.warning("warning信息被执行")
#     logger.error("error信息被执行")
#     logging.critical("critical信息被执行")

    # 切记：设置级别以后，日志信息只会记录大于等于此级别的信息；
    # 1. debug # 调试级别
    # 2. info  # 信息级别
    # 3. warning # 警告
    # 4. error # 错误级别
    # 5. critical # 严重
