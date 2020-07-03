# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.unity3d import UnityPoco

connect_device("android:///127.0.0.1:7555")

poco = UnityPoco()


def global_not():
    shop_time = poco("GameStoreView(Clone)").offspring("StoreBuyView(Clone)").offspring("Lab").get_text()
    print(int(shop_time))
    if shop_time == 0:
        poco("GameStoreView(Clone)").offspring("GameStoreInfoView(Clone)").offspring("CloseBtn").click()
        poco("GameStoreView(Clone)").offspring("GameStoreInfoView(Clone)").offspring("Gold").offspring("AddBtn").click()
        poco("GoldPointingView(Clone)").offspring("Btn_right").click()
        poco("GoldPointingView(Clone)").offspring("Btn_right").click()
        sleep(2)
        poco("GameStoreView(Clone)").child("Content").child("CloseBtn").click()
    else:
        pass


global_not()
# poco("Play").click()
buy_items = set()
for item in poco("GameStoreView(Clone)").offspring("GameStoreInfoView(Clone)").offspring("ScrollView").offspring(
        "Name"):
    item_name = item.get_text()
    if item_name not in buy_items:
        item.click()
        #         global_not()
        poco("BuyBtn").click()
        buy_items.add(item_name)


# 金币不足断言
def global_not():
    shop_time = poco("GameStoreView(Clone)").offspring("StoreBuyView(Clone)").offspring("Lab").get_text()
    print(int(shop_time))
    if shop_time == 0:
        poco("GameStoreView(Clone)").offspring("GameStoreInfoView(Clone)").offspring("CloseBtn").click()
        poco("GameStoreView(Clone)").offspring("GameStoreInfoView(Clone)").offspring("Gold").offspring("AddBtn").click()
        poco("GoldPointingView(Clone)").offspring("Btn_right").click()
        poco("GoldPointingView(Clone)").offspring("Btn_right").click()
        sleep(2)
        poco("GameStoreView(Clone)").child("Content").child("CloseBtn").click()
    else:
        pass

