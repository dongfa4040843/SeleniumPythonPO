#coding:utf-8
import os
import configparser

proDir = os.path.split(os.path.relpath(__file__))[0]
configPath = os.path.join(proDir,"config.ini")
#读取配置文件

cf = configparser.ConfigParser()

#读取config.ini文件
cf.read("configPath")
def getconfigvalue(section,name):
    value = cf.get(section,name)
    return value
getconfigvalue("url","baidu")


