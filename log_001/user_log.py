import logging
import os
import datetime
class UserLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        #操作控制台输出
        # consle = logging.StreamHandler()
        # logger.addHandler(consle)



        #文件的名字
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir,"logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d")+".log"
        log_name = log_dir+"/"+log_file
        print(log_name)

        #操作文件输出
        self.file_handle = logging.FileHandler(log_name,"a",encoding=None)
        formatter = logging.Formatter("%(asctime)s----> %(filename)s %(funcName)s %(levelno)s: %(levelname)s---> %(message)s")
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

    def close_handle(self):
        self.file_handle.close()
        self.logger.removeHandler(self.file_handle)

    def get_log(self):
        return self.logger

if __name__ == "__main__":
    ul = UserLog()
    log = ul.get_log()
    log.debug("test123456")
    ul.close_handle()
