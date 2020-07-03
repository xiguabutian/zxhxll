# -*- encoding=utf8 -*-
from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco

def global_not():  # 金币不足判断1
    shop_time = poco("GameStoreView(Clone)").offspring("StoreBuyView(Clone)").offspring("Lab").get_text()
    print(int(shop_time))
    while (int(shop_time) == 0):
        poco("GameStoreView(Clone)").offspring("GameStoreInfoView(Clone)").offspring("CloseBtn").click()
        poco("GameStoreView(Clone)").offspring("GameStoreInfoView(Clone)").offspring("Gold").offspring("AddBtn").click()
        poco("GoldPointingView(Clone)").offspring("Btn_right").click()
        poco("GoldPointingView(Clone)").offspring("Btn_right").click()
        sleep(3)
        poco("GameStoreView(Clone)").child("Content").child("CloseBtn").click()
        # 功能bug，需要重新刷新才能获取新次数
        poco("GameStoreView(Clone)").offspring("GameStoreInfoView(Clone)").offspring("RightBtn").click()
        poco("GameStoreView(Clone)").offspring("GameStoreInfoView(Clone)").offspring("LeftBtn").click()
        item.click()
        shop_time = poco("GameStoreView(Clone)").offspring("StoreBuyView(Clone)").offspring("Lab").get_text()

    print("继续购买")


def global_buy():# 金币不足判断2
    global1 = poco("CoinGetPathView(Clone)").child("Content").child("Bg")
    global2 = poco("CoinGetPathView(Clone)").offspring("0")
    global2.click()
    poco("GoldPointingView(Clone)").offspring("Btn_right").click()
    poco("GoldPointingView(Clone)").offspring("Btn_right").click()
    sleep(2)
    poco("GameStoreView(Clone)").child("Content").child("CloseBtn").click()
    poco("GameStoreView(Clone)").offspring("GameStoreInfoView(Clone)").offspring("CloseBtn").click()