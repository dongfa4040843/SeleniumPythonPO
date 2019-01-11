import logging
import os
#创建logger
logger = logging.Logger("fox")
Log_file = "test.log"

#设置默认log的级别
logger.setLevel(logging.DEBUG)

#借助Handler将日志输出到日志文件中
fh = logging.FileHandler(Log_file)
fh.setLevel(logging.ERROR)

#创建一个handler将日志输出到控制台上
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)

#定义输出handler的格式
fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

#配置logger
fh.setFormatter(fmt)
sh.setFormatter(fmt)

#给logger添加handler
logger.addHandler(fh)
logger.addHandler(fh)


#应用日志
logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")