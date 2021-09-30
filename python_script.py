#  -*- coding:utf-8 -*-
from uiautomator import device as d
import unittest
import time



def test_b(mycont=None):
    d.press("home")
    d.press("home")

    time.sleep(1)
    d.swipe(500, 1196, 65, 1196, 5)
    d.swipe(500, 1196, 65, 1196, 5)
    d(text="二维码生成").click()
    time.sleep(1)
    mtext = "什么几把鬼{}"
    d(resourceId="com.example.myapplication:id/input_text").clear_text()
    d(resourceId="com.example.myapplication:id/input_text").set_text(mtext.format(mycont))
    time.sleep(1)
    d(text="生成二维码").click()
    time.sleep(1)
    d(text="分享").click()
    time.sleep(1)
    d(text="发送给朋友").click()
    # d(text="钉钉").click()




class Mytest(unittest.TestCase):
    # 初始化工作
    def setUp(self):
        print("--------------初始化工作")

    # 退出清理工作
    def tearDown(self):
        print("--------------退出清理工作")

    @staticmethod
    def test_a():
        mcont=0
        while 1:

            # d.click(65, 1196)
            test_b(mcont)
            mcont += 1
        # d(text="二维码生成").click()
        # print("--------------测试1")





if __name__ == '__main__':
    unittest.main()

