import logging
import os

class Logger():
    def __init__(self,path,cmdLevel,FileLevel):
        self.logger = logging.getLogger(path)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        #设置控制台日志
        sh = logging.StreamHandler()
        sh .setFormatter(fmt)
        sh.setLevel(cmdLevel)

        #设置文件日志
        fh = logging.FileHandler(path)
        fh.setFormatter(fmt)
        fh.setLevel(FileLevel)

        #给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(fh)

    def debug(self,message):
        self.logger.debug(message)

    def info(self,message):
        self.logger.info(message)

    def warn(self,message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def cri(self, message):
        self.logger .critical(message)

if __name__ == "__main__":
    logger = Logger("logging.log",cmdLevel=logging.DEBUG,FileLevel=logging.ERROR)

    logging.debug("debug message")
    logging.info("info message")
    logging.warn("warning message")
    logging.error("error message")
    logging.cri("critical message")