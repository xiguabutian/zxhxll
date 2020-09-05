# coding=utf-8
import time
import xlrd
from xlrd import xldate_as_tuple
import string
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import activ
import sys
import requests
import urllib3
import selenium
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas
from bs4 import BeautifulSoup
from time import sleep
import random
import lxml
import hashlib
import json
from lxml import etree
from sys import path
import pandas
import io
dict_sAdress={}
dict_sAdress['对外安卓测试服']='http://120.92.9.137:882'
dict_sAdress['对外IOS测试服']='http://120.92.9.137:872'
class execle():
    def __init__(self,adreess='C:/Users/Administrator/Desktop/活动测试(3).xlsx',ename='Sheet1'):
        self.ad=adreess
        self.en=ename
        self.dict={}
        self.dict_A={}
        self.excel_j()
        self.get_Amessage()

    def excel_j(self):
        data = xlrd.open_workbook(self.ad)
        data.sheet_names()  # 获取表格分页名称
        table = data.sheet_by_name(self.en)  # 活动页内容读取 Sheet1
        biaoji=True
        d = 0
        l_activ = []
        l_activ2 = []
        for nr in range(table.nrows):  # 活动内容解析
            rowAll = table.row_values(nr)[0:13]
            for a in range(len(rowAll)):
                b = str(type((rowAll[a])))
                if b == "<class 'float'>":  # 解析数字会自动变成浮点类型数据，把浮点转为str并去掉末尾的（.0）
                    rowAll[a] = str(rowAll[a]).split('.0')[0]

                elif rowAll[a] != '' and biaoji==True:  # 去掉空行，全部为空的行不会加到列表里
                    l_activ.append(rowAll)
                    biaoji=False
                    # print(rowAll)
            biaoji=True
        l_activ.append(['活动名称'])
        # print(l_activ)
        # print(len(l_activ))
        for e in range(len(l_activ)):  # 把读取的列表按照每个活动放入字典里
            # print(l_activ[e])
            if l_activ[e][0] != '活动名称':
                l_activ2.append(l_activ[e])
            else:
                self.dict[d] = l_activ2
                d += 1
                l_activ2 = []
        self.dict.pop(0)
        # return self.dict

    def get_Amessage(self):
        s = 0
        for keyA in self.dict.keys():
            # print(self.dict[keyA])
            list_a = self.dict[keyA]
            list_time = []
            list_name = []
            list_id = []
            list_neirong = []
            try:  # 读取活动时间
                time1 = list_a[0][1]
            except:
                # print(list_a)
                print("没有找到时间")
            try:  # 读取活动名字
                list_name.append(list_a[0][0])
            except:
                # print(list_a)
                list_name.append('没得名字')
                print('没有活动名字')
            try:  # 读取活动ID
                teshu1 = ['特殊召唤']
                teshu2 = ['体力双倍', '圣器双倍', '圣衣双倍']
                teshu3 = ['团购']
                if list_a[0][0] in teshu1:
                    activ_id = list_a[2][0]
                    activ_id1 = list_a[3][0]
                    list_id.append(activ_id)
                    list_id.append(activ_id1)
                    neirong1 = [['vip', '2']]
                    list_neirong.append(list_a)
                    list_neirong.append(neirong1)
                elif list_a[0][0] in teshu2:
                    # for b in list_a:
                    #     print(b)
                    activ_id = list_a[1][0]
                    activ_id1 = list_a[2][0]
                    list_id.append(activ_id)
                    list_id.append(activ_id1)
                    neirong1 = []
                    neirong2 = []
                    if list_a[0][0] == '体力双倍':
                        neirong1 = [['pve', '2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,']]
                        neirong2 = [[
                                        '[a2642e]活动时间：开始时间 [d02e2e]05:00[-]-结束时间 [d02e2e]05:00[-]\\n活动内容：活动期间购买体力可享受双倍体力值\\n活动范围：开服七日以上服务器[-]']]
                    elif list_a[0][0] == '圣器双倍':
                        neirong1 = [['elite', '[1,2]'], ['normal', '[1,2]']]
                        neirong2 = [[
                                        '[a2642e]活动时间：开始时间 5:00-结束时间 5:00\\n活动内容：活动期间通关主线普通及精英副本圣器掉落数量翻倍\\n活动范围：开服七日以上服务器\\n注：活动期间所有普通及精英副本圣器数量双倍掉落，掉落概率及其它道具的掉落倍率不变[-]']]
                    elif list_a[0][0] == '圣衣双倍':
                        neirong1 = [['cloth', '[1,2,3,4,5]']]
                        neirong2 = [[
                                        '[a2642e]活动时间：开始时间 5:00-结束时间 5:00\\n活动内容：活动期间，斗士们通关圣衣试炼可以获得双倍的圣衣材料掉落！\\n注意事项：\\n1.请尽量避免在紧邻在活动开始及结束的前后5至10分钟通关圣衣试炼，以免由于数据未同步导致无法获得双倍材料。\\n2.本次双倍为掉落材料双倍，各阶材料的掉落概率不会发生变化。[-]']]
                    list_neirong.append(neirong1)
                    list_neirong.append(neirong2)
                elif list_a[0][0] in teshu3:
                    tuangou1 = []
                    tuangou2 = []
                    tuangou3 = []
                    for t in list_a:
                        if t[0] != '' and t[0] != '团购':
                            list_id.append(t[0])
                    listfen = []
                    for k in range(len(list_a)):
                        if list_a[k][5] != '' and k > 4:
                            listfen.append(k)
                    for k in range(len(list_a)):
                        if k < listfen[0]:
                            tuangou1.append(list_a[k])
                        elif k >= listfen[0] and k < listfen[1]:
                            tuangou2.append(list_a[k])
                        elif k >= listfen[1]:
                            tuangou3.append(list_a[k])
                    list_neirong.append(tuangou1)
                    list_neirong.append(tuangou2)
                    list_neirong.append(tuangou3)
                else:
                    list_id.append(list_a[1][0])
                    list_neirong.append(list_a)
            except:
                # print(list_a)
                print('活动只有一行？')
                for b in list_a:
                    print(b)
                print('')
                list_name.append('没有活动ID')
            try:
                if '-' in time1:
                    s_time = time1.split('-')[0].replace('/', '-') + ' 0:0:0'  # 开始时间，默认0点
                    e_time = time1.split('-')[1].replace('/', '-') + ' 0:0:0'  # 结束时间，默认0点
                    self.dict_Array_s = time.strptime(s_time, '%Y-%m-%d %H:%M:%S')
                    timeStamp_s = int(time.mktime(self.dict_Array_s))
                    self.dict_Array_e = time.strptime(e_time, '%Y-%m-%d %H:%M:%S')
                    timeStamp_e = int(time.mktime(self.dict_Array_e))
                    c_time = timeStamp_e - timeStamp_s + 86399  # 持续时间，默认比时间时间少1秒
                    list_time.append(s_time)
                    list_time.append(str(c_time))
                    list_time.append(e_time)
                else:
                    s_time = xldate_as_tuple(int(time1), 0)
                    sds = str(s_time[0]) + '-' + str(s_time[1]) + '-' + str(s_time[2]) + ' 0:0:0'
                    c_time = '86399'
                    list_time.append(sds)
                    list_time.append(c_time)
            except:
                print(time1)
                print('时间格式错误')
                for b in list_a:
                    print(b)
                print('')
                list_time.append("时间格式错误")
                list_time.append("持续时间错误")
            for a in range(len(list_neirong)):
                activ_q = []
                list_title = []
                if list_name[0] == '体力双倍' or list_name[0] == '圣器双倍' or list_name[0] == '圣衣双倍' or list_name[0] == '特殊召唤':
                    if list_name[0] == '特殊召唤':
                        list_tim = list_time[0]
                    else:
                        list_tim = list_time[0].split(' ')[0] + ' 5:0:0'
                    list_title.append(list_id[a])
                    list_title.append(list_name[0])
                    if a == 0:
                        list_title.append(list_tim)
                    else:
                        list_title.append(list_time[0])
                    list_title.append(list_time[1])
                    list_title.append(list_time[2])
                    for b in list_neirong[a]:
                        b = [i for i in b if i != '']
                        activ_q.append(b)
                else:
                    for b in list_neirong[a]:
                        b = [i for i in b if i != '']
                        activ_q.append(b)
                    list_title.append(list_id[a])
                    list_title.append(list_name[0])
                    list_title.append(list_time[0])
                    list_title.append(list_time[1])
                activ_q.insert(0, list_title)
                if list_id[a] == '':
                    s += 1
                    self.dict_A[s] = activ_q
                else:
                    self.dict_A[list_id[a]] = activ_q
            # for a in list_a:
            #     a=[i for i in a if i !=''] #去掉空行
            #     activ_q.append(a)
            # activ_q.insert(0,list_time)
            # if activ_id=='':
            #     s+=1
            #     self.dict_A[s] = activ_q
            # else:
            #     self.dict_A[activ_id]=activ_q

    def chuli_activ(self):
        for keyB in list(self.dict_A.keys()):
            chongzhi = ['充值有礼']
            leijicz = ['累计充值', '消费返利', '扭蛋币']
            jiuji = ['跨服抢购']
            duihuan = ['点金返利', '守护兑换', '金币兑换', '原力兑换', '限时特殊召唤', '重生石兑换', '材料兑换', '角色魂石兑换', '觉醒石兑换', '神器觉醒', '神钢兑换',
                       '水晶兑换', '水果拉霸', '超级幸运星', '究极之力兑换', '究极之力兑换1', '究极之力兑换2', '角色魂石兑换1', '角色魂石兑换2', '觉醒石兑换1',
                       '觉醒石兑换2']
            duobao = ['一元夺宝']
            zhaohuan = ['特殊召唤']
            guigui = ['贵鬼奖励', '贵鬼游戏']
            hunxia = ['魂匣']
            xiaohuodong = ['潘多拉魔盒', '超级金币翻牌', '女神问答', '旋转派对', '消消乐', '开工福利', '活跃有礼', '副本挑战', '守护雅典娜', '体力消耗', '射箭',
                           '砸金蛋', '扭蛋币']
            zhuanpan = ['幸运转盘']
            tili = ['体力双倍', '圣衣双倍', '圣器双倍']
            tuangou = ['团购']
            # 充值有礼活动
            if self.dict_A[keyB][0][1] in chongzhi:
                self.dict_A[keyB][-1].insert(0, '100天')  # 最终奖励配置，不用管
                self.dict_A[keyB][-1].insert(0, '60')  # 连续充值多少天可以领取60/10=6天
                del self.dict_A[keyB][1][0:2]
                if self.dict_A[keyB][0][0] != '':
                    del self.dict_A[keyB][2][0]
            # 累计充值 消费返利 重生石兑换 扭蛋币
            elif self.dict_A[keyB][0][1] in leijicz:
                del self.dict_A[keyB][1][0:2]
                if self.dict_A[keyB][0][0] != '':
                    del self.dict_A[keyB][2][0]
                if self.dict_A[keyB][0][1] == '消费返利':
                    for i in range(len(self.dict_A[keyB])):
                        if i > 0:
                            self.dict_A[keyB][i].append('LotteryShow+2')  # 跳转
                elif self.dict_A[keyB][0][1] == '扭蛋币':
                    for i in range(len(self.dict_A[keyB])):
                        if i > 0:
                            self.dict_A[keyB][i].append('ReChargeShow')  # 跳转
                # for i in self.dict_A[keyB]:
                #     print(i)
            # 跨服究极之力抽卡
            elif self.dict_A[keyB][0][1] in jiuji:
                listt = []
                del self.dict_A[keyB][1:3]
                del self.dict_A[keyB][2][0]
                kuid = self.dict_A[keyB][4][0].split('：')[1]
                jifen = '10'  # 每抽获得积分，默认10
                kuafu = '1'  # 是否跨服，1为跨服，0为不跨服
                rangk = self.dict_A[keyB][(len(self.dict_A[keyB]) - 1)][1].split('上榜积分')[1]
                rangkn = self.dict_A[keyB][(len(self.dict_A[keyB]) - 1)][2].split('排行榜人数')[1]
                del self.dict_A[keyB][(len(self.dict_A[keyB]) - 1)]
                listt.append(kuid)
                listt.append(jifen)
                listt.append(rangk)
                listt.append(rangkn)
                listt.append(kuafu)
                del self.dict_A[keyB][4][0]
                del self.dict_A[keyB][6][0]
                self.dict_A[keyB].insert(1, listt)
                for i in range(len(self.dict_A[keyB])):
                    if '到' in self.dict_A[keyB][i][0]:
                        rankings = self.dict_A[keyB][i][0].split('到')[0]
                        self.dict_A[keyB][i][0] = self.dict_A[keyB][i][0].split('到')[1]
                        self.dict_A[keyB][i].insert(0, rankings)
                    elif i > 1:
                        rankings = self.dict_A[keyB][i][0]
                        self.dict_A[keyB][i].insert(0, rankings)
            # '点金返利','金币兑换','原力兑换','限时特殊召唤','重生石兑换'，材料兑换,'角色魂石兑换','觉醒石兑换','神器觉醒',神钢兑换 水晶兑换 水果拉霸
            elif self.dict_A[keyB][0][1] in duihuan:
                duihuan1 = ['材料兑换', '角色魂石兑换', '神器觉醒', '守护兑换', '究极之力兑换1', '究极之力兑换2', '角色魂石兑换1', '角色魂石兑换2', '究极之力兑换']
                duihuan2 = ['重生石兑换', '神钢兑换', '水晶兑换']
                duihuan3 = ['超级幸运星']
                duihuan4 = ['觉醒石兑换', '觉醒石兑换1', '觉醒石兑换2']
                del self.dict_A[keyB][1][0:2]
                if self.dict_A[keyB][0][0] != '':
                    del self.dict_A[keyB][2][0]
                if self.dict_A[keyB][0][1] == '点金返利':
                    for i in range(len(self.dict_A[keyB])):
                        if i > 0:
                            del self.dict_A[keyB][i][0]
                            self.dict_A[keyB][i].append('GoldPointingShow')  # 跳转
                elif self.dict_A[keyB][0][1] == '金币兑换':
                    for i in range(len(self.dict_A[keyB])):
                        if i > 0:
                            self.dict_A[keyB][i].append('GoldPointingShow')  # 跳转
                            self.dict_A[keyB][i].insert(0, '次数')
                elif self.dict_A[keyB][0][1] == '原力兑换':
                    for i in range(len(self.dict_A[keyB])):
                        if i > 0:
                            self.dict_A[keyB][i].insert(0, '次数')
                elif self.dict_A[keyB][0][1] == '限时特殊召唤':
                    del self.dict_A[keyB][5][0]
                    del self.dict_A[keyB][6][0]
                elif self.dict_A[keyB][0][1] in duihuan2:
                    for i in range(len(self.dict_A[keyB])):
                        if i > 0:
                            self.dict_A[keyB][i].append('ReChargeShow')  # 跳转
                            self.dict_A[keyB][i].insert(0, '次数')
                        # for i in self.dict_A[keyB]:
                        #     print(i)
                elif self.dict_A[keyB][0][1] in duihuan1:
                    for i in range(len(self.dict_A[keyB])):
                        if i > 0:
                            self.dict_A[keyB][i].insert(0, '次数')
                elif self.dict_A[keyB][0][1] in duihuan4:
                    for i in range(len(self.dict_A[keyB])):
                        if i > 0:
                            self.dict_A[keyB][i].insert(0, '次数')
                            if '石' in self.dict_A[keyB][i][4]:
                                self.dict_A[keyB][i][4] = self.dict_A[keyB][i][4].replace('石', '')
                elif self.dict_A[keyB][0][1] in duihuan3:
                    for i in range(len(self.dict_A[keyB])):
                        if i > 0:
                            self.dict_A[keyB][i].append('ReChargeShow')  # 跳转
                    # for i in self.dict_A[keyB]:
                    #     print(i)
            # 夺宝奇兵
            elif self.dict_A[keyB][0][1] in duobao:
                del self.dict_A[keyB][1][0:2]
                if self.dict_A[keyB][0][0] != '':
                    del self.dict_A[keyB][2][0:3]
                try:
                    times = self.dict_A[keyB][2][1].split('最多可买')[1].split('次')[0]
                except:
                    times = '默认10'
                del self.dict_A[keyB][2][2]
                del self.dict_A[keyB][3][0:3]
                del self.dict_A[keyB][4][0:3]
                self.dict_A[keyB][1].insert(0, times)
                self.dict_A[keyB][2].insert(0, times)
                self.dict_A[keyB][0].append('561600')  # 竞猜时间
                self.dict_A[keyB][0].append('43199')  # 领奖时间
            # 特殊召唤
            elif self.dict_A[keyB][0][2] in zhaohuan:
                del self.dict_A[keyB][1][0:2]
                keyZ = self.dict_A[keyB][0][1]
                listZ = []
                listZ.append(keyZ)
                listZ.append(self.dict_A[keyB][2][0])
                listZ.append(self.dict_A[keyB][0][3])
                listZ.append(self.dict_A[keyB][0][4])
                if self.dict_A[keyB][0][0] != '':
                    del self.dict_A[keyB][2][0]
                del self.dict_A[keyB][0][1]
                del self.dict_A[keyB][4][0]
                del self.dict_A[keyB][3][0]
                for i in range(len(self.dict_A[keyB])):
                    if i > 0:
                        self.dict_A[keyB][i].append('LotteryShow+3')  # 跳转
                self.dict_A[keyB].append(listZ)
            # 贵鬼
            elif self.dict_A[keyB][0][1] in guigui:
                if self.dict_A[keyB][0][1] == '贵鬼游戏':
                    del self.dict_A[keyB][1][0:3]
                    del self.dict_A[keyB][2][0:2]
                    del self.dict_A[keyB][3][0]
                    del self.dict_A[keyB][4][0:2]
                    listg = []
                    listga = []
                    listgb = []
                    listga.append('贵鬼证明')
                    listga.append('1')
                    listg.append(self.dict_A[keyB][5][0])
                    listg.append('1')
                    listgb.append(self.dict_A[keyB][5][0])
                    listgb.append('1')
                    listgb.append('1分')
                    listg.append('晶莹水晶3阶碎片')
                    listg.append('1')
                    listg.append('2分')
                    del self.dict_A[keyB][5][0]
                    del self.dict_A[keyB][6][0]
                    del self.dict_A[keyB][7][0]
                    del self.dict_A[keyB][8][0]
                    del self.dict_A[keyB][9][0]
                    self.dict_A[keyB].append(listga)
                    self.dict_A[keyB].append(listgb)
                    self.dict_A[keyB].append(listg)
                elif self.dict_A[keyB][0][1] == '贵鬼奖励':
                    del self.dict_A[keyB][1][0:2]
                    if self.dict_A[keyB][0][0] != '':
                        del self.dict_A[keyB][2][0]
                    for i in range(len(self.dict_A[keyB])):
                        if i > 0:
                            self.dict_A[keyB][i].append('ReChargeShow')
            # 魂匣
            elif self.dict_A[keyB][0][1] in hunxia or self.dict_A[keyB][0][1][0:2] == '魂匣' or self.dict_A[keyB][0][1][0:2] == '神圣':
                if self.dict_A[keyB][1][2][-1] == ' ':
                    self.dict_A[keyB][1][2] = self.dict_A[keyB][1][2][:-1]
                kuid = self.dict_A[keyB][1][2][-6:]
                if kuid[0] != '1':
                    kuid = kuid[1:]
                heroid1 = self.dict_A[keyB][1][4]
                heroid2 = self.dict_A[keyB][1][6]
                heroid3 = self.dict_A[keyB][1][8]
                listhx = [kuid, heroid1, heroid2, heroid3]
                self.dict_A[keyB][1] = listhx
                del self.dict_A[keyB][2]
            # 小活动 潘多拉魔盒 超级金币翻牌 女神问答 旋转派对 斗士消消乐 活跃有礼 副本挑战 守护雅典娜 体力消耗 扭蛋
            elif self.dict_A[keyB][0][1] in xiaohuodong:
                del self.dict_A[keyB][1][0:2]
                if self.dict_A[keyB][0][0] != '':
                    del self.dict_A[keyB][2][0]
                if self.dict_A[keyB][0][1] == '潘多拉魔盒':
                    del self.dict_A[keyB][1][2]
                    listc = ['0', '10', '30', '50', '70', '90', '120', '150', '180']  # 每次消耗的钻石
                    for i in listc:
                        self.dict_A[keyB][1].append(i)
                    del self.dict_A[keyB][2:]
                elif self.dict_A[keyB][0][1] == '超级金币翻牌':
                    listm = []
                    listm.append('钻石')
                    listm.append(self.dict_A[keyB][3][0])
                    times = self.dict_A[keyB][4][0].split('购买')[1].split('次')[0]
                    listm.append(times)
                    listm.append('3')  # 必出幸运卡片轮数
                    listm.append('3')  # 每轮几张
                    self.dict_A[keyB][1] = listm
                    del self.dict_A[keyB][2]
                    del self.dict_A[keyB][2][0]
                    del self.dict_A[keyB][3][0]
                    for i in range(len(self.dict_A[keyB])):
                        if i > 1 and i < 12:
                            self.dict_A[keyB][i] = self.dict_A[keyB][i][0:1]
                            self.dict_A[keyB][i].insert(0, '游戏币')
                    del self.dict_A[keyB][12:14]
                elif self.dict_A[keyB][0][1] == '旋转派对':  # 奖励没得
                    lista = []
                    lista = self.dict_A[keyB][0]
                    lista[1] = '女神对对碰'
                    listb = []
                    listb.append(lista)
                    self.dict_A[keyB] = listb
                elif self.dict_A[keyB][0][1] == '消消乐':  # 积分奖励GM上没有，删除掉
                    del self.dict_A[keyB][1:12]
                elif self.dict_A[keyB][0][1] == '开工福利':
                    self.dict_A[keyB][2].append('等级')
                    self.dict_A[keyB][2].append('1')
                elif self.dict_A[keyB][0][1] == '副本挑战':
                    for i in range(len(self.dict_A[keyB])):
                        if self.dict_A[keyB][i][0][0:2] == '普通':
                            self.dict_A[keyB][i].append('LevelShow+PT')
                        elif self.dict_A[keyB][i][0][0:2] == '精英':
                            self.dict_A[keyB][i].append('LevelShow+JY')
                elif self.dict_A[keyB][0][1] == '守护雅典娜':
                    for i in range(len(self.dict_A[keyB])):
                        if self.dict_A[keyB][i][0][0:2] == '守护':
                            self.dict_A[keyB][i].append('GuardAthenaIn')
                elif self.dict_A[keyB][0][1] == '体力消耗':
                    for i in range(len(self.dict_A[keyB])):
                        if self.dict_A[keyB][i][0][0:2] == '消耗':
                            self.dict_A[keyB][i].append('LevelShow')
                elif self.dict_A[keyB][0][1] == '射箭':
                    del self.dict_A[keyB][2]
                elif self.dict_A[keyB][0][1] == '砸金蛋':
                    self.dict_A[keyB][1] = [self.dict_A[keyB][1][0]]
                    del self.dict_A[keyB][2][-1]
                    del self.dict_A[keyB][3][-1]
                    del self.dict_A[keyB][4][-1]

                elif self.dict_A[keyB][0][1] == '活跃有礼':
                    dicth = {}
                    dicth['钻石召唤5次'] = 'LotteryShow+2'
                    dicth['BOSS挑战3次'] = 'BossFightViewShow'
                    dicth['竞技场获得30分'] = 'ArenaViewShow'
                    dicth['点金5次'] = 'GoldPointingShow'
                    dicth['星力消耗18000'] = 'HeroBgShow+3'
                    dicth['特殊召唤5次'] = 'HeroBgShow+3'
                    dicth['金币抽奖次数20次'] = 'HeroBgShow+3'
                    dicth['竞技场胜利3次'] = 'HeroBgShow+3'
                    dicth['参与竞技场11次'] = 'HeroBgShow+3'
                    dicth['钻石抽奖3次'] = 'LotteryShow+2'
                    for i in range(len(self.dict_A[keyB])):
                        if i > 0:
                            self.dict_A[keyB][i].append(dicth[self.dict_A[keyB][i][0]])
                # for i in self.dict_A[keyB]:
                #     print(i)
            # 幸运转盘
            elif self.dict_A[keyB][0][1] in zhuanpan:
                listbll = []
                listtitle = self.dict_A[keyB][0]
                baodi = self.dict_A[keyB][2][1].split('每')[1].split('次一次')[0]  # 多少次保底
                times = self.dict_A[keyB][2][1].split('一共保')[1].split('次')[0]  # 一共保底几次
                putong = self.dict_A[keyB][1][2]  # 普通道具名称
                teshu = self.dict_A[keyB][2][2]  # 特殊道具名称
                listta = ['消耗', '转盘抽奖券', '1']
                listtb = ['500', '废墟遗石', '3', '2000', '钻石', '170', '2800', '普通', '15', '1800', '普通', '15', '2800', '普通',
                          '20', '1000', '废墟遗石', '2', '1800', '普通', '20', '1200', '普通', '25', '1000', '废墟遗石', '2',
                          '1200', '普通', '25']
                listtc = ['100', '特殊', '1', '500', '废墟遗石', '3', '2000', '钻石', '170', '2800', '普通', '15', '100', '钻石',
                          '3000', '1800', '普通', '15', '2800', '普通', '20', '1000', '废墟遗石', '2', '1800', '普通', '20',
                          '1200', '普通', '25', '1000', '废墟遗石', '2', '1200', '普通', '25']
                listtd = [putong if i == '普通' else i for i in listtb]
                listte = [putong if i == '普通' else i for i in listtc]
                listte = [teshu if i == '特殊' else i for i in listte]
                listbll.append(listtitle)
                listbll.append(listta)
                for i in range(int(times)):
                    listbd = []
                    times_a = (i + 1) * int(baodi)
                    listbd.append(str(times_a) + '次')
                    listbd.append(teshu)
                    listbd.append('1')
                    listbll.append(listbd)
                listbll.append(listtd)
                listbll.append(listte)
                listbe = [putong, listtb[1], teshu]
                listbll.append(listbe)
                listbf = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']  # 高亮的设置
                listbff = []
                listbff.append(listbf)
                listbll.append(listbf)
                self.dict_A[keyB] = listbll
                # for i in self.dict_A[keyB]:
                #     print(i)
            # 体力双倍
            elif self.dict_A[keyB][0][1] in tili:
                if len(self.dict_A[keyB][1]) == 1:
                    strtime = self.dict_A[keyB][0][2].split(' ')[0].split('-')[1] + '月' + \
                              self.dict_A[keyB][0][2].split(' ')[0].split('-')[2] + '日'
                    endtime = self.dict_A[keyB][0][4].split(' ')[0].split('-')[1] + '月' + \
                              self.dict_A[keyB][0][4].split(' ')[0].split('-')[2] + '日'
                    self.dict_A[keyB][1] = [self.dict_A[keyB][1][0].replace('开始时间', strtime).replace('结束时间', endtime)]
                # for i in self.dict_A[keyB]:
                #     print(i)
            # 团购
            elif self.dict_A[keyB][0][1] in tuangou:
                if keyB == self.dict_A[keyB][2][0]:
                    # for i in self.dict_A[keyB]:
                    #     print(i)
                    del self.dict_A[keyB][1][0:2]
                    del self.dict_A[keyB][1][2]
                    del self.dict_A[keyB][2][0]
                    del self.dict_A[keyB][3][0]
                    del self.dict_A[keyB][4][0]
                    for k in range(len(self.dict_A[keyB])):
                        if k > 1:
                            self.dict_A[keyB][k] = [self.dict_A[keyB][k][2], (self.dict_A[keyB][k][1].split('.')[1] + '00')]
                else:
                    del self.dict_A[keyB][1][2]
                    for k in range(len(self.dict_A[keyB])):
                        if k > 1:
                            self.dict_A[keyB][k] = [self.dict_A[keyB][k][2], (self.dict_A[keyB][k][1].split('.')[1] + '00')]

        return self.dict_A

class sever():
    def __init__(self,url='',iadress='',cadress='',api='/sgame_gm/gm_active_port/get_activeshow'):
        self.u=url
        self.a=api
        self.i=iadress
        self.c=cadress
        self.d_iteam={}
        self.d_card={}
        self.dict_card()
        self.dict_item()

    #获取道具配置表，存入self.d_iteam
    def dict_item(self):
        item_l = []
        with open(self.i, 'r', encoding='UTF-8') as file_to_read:
            while True:
                lines = file_to_read.readline()  # 整行读取数据
                if not lines:
                    break
                    pass
                item = [i for i in lines.split()]  # 将整行数据分割处理
                item_l.append(item)
        for i in item_l:
            try:  # 装备和普通道具在表里的位置不一样，装备在第6，普通道具在第5
                int(i[5])  # 如果第5个不是数字，就是道具，是数字，就是装备
                self.d_iteam[i[0]] = i[6]
            except:  # 道具就走这里
                try:
                    int(i[6])
                    self.d_iteam[i[0]] = i[5]
                except:
                    self.d_iteam[i[0]] = i[5] + i[6]
        self.d_iteam['rmb'] = '钻石'
        self.d_iteam['role_money'] = '游戏币'
        self.d_iteam['times'] = '次数'
        self.d_iteam['draw_special'] = '次'
        self.d_iteam['5202'] = '5202'
        self.d_iteam['5019'] = '5019'
        self.d_iteam['5020'] = '5020'
        self.d_iteam['5021'] = '5021'
        return self.d_iteam

    # 获取卡牌配置表，存入self.d_card
    def dict_card(self):
        card_l = []
        with open(self.c, 'r', encoding='UTF-8') as file_to_read:
            while True:
                lines = file_to_read.readline()  # 整行读取数据
                if not lines:
                    break
                    pass
                card = [i for i in lines.split()]  # 将整行数据分割处理
                card_l.append(card)
        for i in card_l:
            self.d_card[i[0]] = i[1]
        return self.d_card



    #输入服务器返回的道具ID，转换为道具的名称
    def jiangli_j(self,jiangli,fanzhuan):  # 传入奖励 '[{role_money,540000},{prop,{3502,6}},{prop,{3576,2}}]'
        self.liste = []
        if '},{' in jiangli and '[' in jiangli:
            jiangli = jiangli.replace('},{', '/').replace('{', '').replace('}', '')
            jiangli = jiangli.replace('[', '').replace(']', '')  # 替换掉括号
            jianglia = jiangli.split('/')
        elif '[' in jiangli:
            jiangli = jiangli.replace('[', '').replace(']', '').replace('{', '').replace('}', '')
            jianglia = []
            jianglia.append(jiangli)
        else:
            jiangli = jiangli.replace('{', '').replace('}', '')
            jianglia = []
            jianglia.append(jiangli)
        daoju = ['prop']
        jinbi = ['role_money', 'rmb', 'times', 'draw_special']
        jiuji = ['force_card']
        yingxiong = ['hero']
        if fanzhuan == 1:
            for a in range(len(jianglia)):
                jianglia[a] = jianglia[a].split(',')
                # print(jianglia[a])
                if jianglia[a][0] in daoju:  # 判断道具类型
                    jianglia[a][1] = self.d_iteam[jianglia[a][1]]
                    self.liste.append(jianglia[a][1])
                    self.liste.append(jianglia[a][2])
                elif jianglia[a][0] in jiuji:
                    # print(jianglia[a])
                    jianglia[a][1] = self.d_card[jianglia[a][1]]
                    if int(jianglia[a][2]) > 1:
                        jianglia[a][1] = jianglia[a][2] + '星' + jianglia[a][1]
                    # print(jianglia[a])
                    self.liste.append(jianglia[a][1])
                    self.liste.append(jianglia[a][3])
                elif jianglia[a][0] in yingxiong:
                    jianglia[a][1] = jianglia[a][2] + '星' + self.d_iteam['4' + jianglia[a][1][1:4]].split('魂石')[0]
                    self.liste.append(jianglia[a][1])
                    self.liste.append(jianglia[a][3])
                elif jianglia[a][0] in jinbi:
                    jianglia[a][0] = self.d_iteam[jianglia[a][0]]
                    # print(self.d_iteam['role_money'])
                    self.liste.append(jianglia[a][0])
                    self.liste.append(jianglia[a][1])
        elif fanzhuan == 0:
            for a in reversed(range(len(jianglia))):
                jianglia[a] = jianglia[a].split(',')
                # print(jianglia[a])
                if jianglia[a][0] in daoju:  # 判断道具类型
                    jianglia[a][1] = self.d_iteam[jianglia[a][1]]
                    self.liste.append(jianglia[a][1])
                    self.liste.append(jianglia[a][2])
                elif jianglia[a][0] in jiuji:
                    # print(jianglia[a])
                    jianglia[a][1] = self.d_card[jianglia[a][1]]
                    if int(jianglia[a][2]) > 1:
                        jianglia[a][1] = jianglia[a][2] + '星' + jianglia[a][1]
                    # print(jianglia[a])
                    self.liste.append(jianglia[a][1])
                    self.liste.append(jianglia[a][3])
                elif jianglia[a][0] in yingxiong:
                    jianglia[a][1] = jianglia[a][2] + '星' + self.d_iteam['4' + jianglia[a][1][1:4]].split('魂石')[0]
                    self.liste.append(jianglia[a][1])
                    self.liste.append(jianglia[a][3])
                elif jianglia[a][0] in jinbi:
                    jianglia[a][0] = self.d_iteam[jianglia[a][0]]
                    # print(self.d_iteam['role_money'])
                    self.liste.append(jianglia[a][0])
                    self.liste.append(jianglia[a][1])
        return self.liste

    #从服务器获取当前的所有活动
    def get_activ(self):  # 从服务器获取现在开启的所有活动
        # host2 = 'http://120.92.15.130:902' #渠道验收服
        # host1='http://120.92.9.137:882' #对外安卓
        # host='http://192.168.9.11:882' #本地服
        host3 = 'http://120.92.9.137:872'  # 对外IOS
        # api = '/sgame_gm/gm_active_port/get_activeshow'  # 查询服务器开启活动的接口
        url = '%s%s' % (self.u, self.a)
        data = {  # 发送的参数
            "type": "1",
            'user': 'admin',
            'password': '123456',
            'active_m': 'active_checkin-active_consume_buy-active_exchange-active_first_cash_double-active_one_cash_double-active_one_cash-active_total_cash-active_total_consume',
        }
        self.r = requests.post(url, data)

    #去掉活动无用的信息，按活动ID把活动存入self.dict{}
    def j_activ(self):
        soup = BeautifulSoup(self.r.text, 'lxml')
        table = soup.find_all(name='table', attrs={'border': 3})
        activ = []
        for tab in table:
            tr_arr = tab.find_all('tr')  # 把数据分列
            for tr in tr_arr:
                activ1 = []
                # print(tr)
                td_s = tr.find_all('td')  # 把列的数据分格
                # print(type(td_s))
                for td in td_s:
                    td_o = td.string
                    activ1.append(td_o)
                    # print((activ1))
                # print(activ1)
                activ.append(activ1)
            activ.append("这是一个标记")
        self.dict = {}
        activ2 = []
        f = 0
        for i in activ:
            # print(i)
            if i != "这是一个标记":
                activ2.append(i)
                # print(activ2)
            else:
                f += 1
                self.dict[f] = activ2
                activ2 = []
                # print(f)

    #按照格式处理活动，用于与活动表读取的数据对比self.dict_final{}
    def jx_huodong(self):
        self.get_activ()
        self.j_activ()
        self.dict_final = {}
        for i in list(self.dict.keys()):
            chongzhi = ['充值有礼']
            leijicz = ['累计充值']
            yuanli = ['原力抽卡']
            dianjin = ['点金返利']
            xiaofei = ['消费返利', '消费返利全转盘', '金币兑换', '原力兑换', '重生石兑换', '材料兑换', '角色魂石兑换', '觉醒石兑换', '神器觉醒', '水晶兑换', '神钢兑换',
                       '水果拉霸', '超级幸运星', '守护兑换', '究极之力兑换', '究极之力兑换1', '究极之力兑换2', '角色魂石兑换1', '角色魂石兑换2', '觉醒石兑换1',
                       '觉醒石兑换2']
            duobao = ['奇兵夺宝']
            zhaohuan = ['特殊召唤', '召唤特惠']
            xianshi = ['限时特殊召唤']
            guigui = ['贵鬼的游戏', '贵鬼的奖励']
            hunxia = ['魂匣', '神圣']
            panduola = ['潘多拉魔盒', '女神问答', '女神对对碰', '开工福利', '副本挑战', '守护雅典娜', '体力消耗', '砸金蛋', '扭蛋币']
            fanpan = ['超级金币翻牌', '金币翻牌']
            zhuanpan = ['幸运转盘']
            tili = ['体力双倍']
            tuangou = ['超级团购']
            huoyue = ['活跃有礼']
            shengqi = ['圣器双倍']
            shengyi = ['圣衣双倍']
            shuangbei = ['双倍充值']
            activ_a = self.dict[i]
            listb = []
            # print('')
            # print(i)
            # for j in self.dict[i]:
            #     print(j)
            # 每日充值活动
            if self.dict[i][0][0] in chongzhi:
                listc = []
                listd = []
                actid = self.dict[i][2][0]
                actname = self.dict[i][0][0]
                acttime = self.dict[i][5][2]
                acttimec = self.dict[i][5][3]
                listd = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                listc.append(listd)
                for j in range(len(activ_a)):
                    activ_j = activ_a[j]
                    if j >= 9:
                        liste = []
                        if activ_j[2] == '1':
                            slect = '可选'
                            liste.append(slect)
                        else:
                            day = activ_j[0] + '天'
                            charge = activ_j[1].split(',')[1].split('}')[0] + '0'
                            liste.append(charge)
                            liste.append(day)
                        print(activ_j[3])
                        jiangli = self.jiangli_j(activ_j[3], 0)
                        print(jiangli)
                        for k in jiangli:
                            liste.append(k)
                        listc.append(liste)
                self.dict[i] = listc

            # 累计充值活动
            elif self.dict[i][0][0] in leijicz:
                listdz = []
                actid = self.dict[i][2][0]
                actidz = self.dict[i][2][0]
                actname = self.dict[i][0][0]
                acttime = self.dict[i][5][2]
                acttimec = self.dict[i][5][3]
                listdz = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                listez = []
                listez.append(listdz)
                for j in range(len(activ_a)):
                    activ_j = activ_a[j]
                    if j >= 9:
                        listjx = []
                        if activ_j[1] == '1':  # 读取奖励的可选状态
                            slect = '可选'
                            listjx.append(slect)
                        else:  # 读取奖励的充值金额
                            charge = activ_j[0] + '0'
                            listjx.append(charge)
                        print(33)
                        listjl = self.jiangli_j(activ_j[2], 0)
                        print(listjl)
                        for k in listjl:
                            listjx.append(k)
                        listez.append(listjx)
                self.dict[i] = listez
            elif self.dict[i][0][0] in shuangbei:
                listdz = []
                actid = self.dict[i][2][0]
                actidz = self.dict[i][2][0]
                actname = self.dict[i][0][0]
                acttime = self.dict[i][5][2]
                acttimec = self.dict[i][5][3]
                listdz = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                listez = []
                listez.append(listdz)
                for j in range(len(activ_a)):
                    activ_j = activ_a[j]
                    if j >= 9:
                        listjx = []
                        listjx.append(activ_j[1])
                        listjx.append((activ_j[3] + '次'))
                        listjl = self.jiangli_j(activ_j[4], 0)
                        for k in listjl:
                            listjx.append(k)
                        listez.append(listjx)
                self.dict[i] = listez
            # 跨服究极之力抽卡活动
            elif self.dict[i][0][0] in yuanli:
                lista = []
                actid = self.dict[i][2][0]
                actidz = self.dict[i][2][0]
                actname = '跨服抢购'
                acttime = self.dict[i][5][2]
                acttimec = self.dict[i][5][3]
                listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                lista.append(listt)
                listn = []
                listn.append(self.dict[i][9][0])
                listn.append(self.dict[i][9][1])
                listn.append(self.dict[i][9][2])
                listn.append(self.dict[i][9][3])
                listn.append(self.dict[i][9][5])
                lista.append(listn)  # ['300100', '10', '3000', '500', '1']
                for j in range(len(self.dict[i])):
                    activ_j = self.dict[i][j]
                    if j >= 12:
                        listxs = []
                        listxs.append(activ_j[0])
                        listxs.append(activ_j[1])
                        listjl = self.jiangli_j(activ_j[2], 0)
                        for k in listjl:
                            listxs.append(k)
                        lista.append(listxs)
                self.dict[i] = lista
            # 点金
            elif self.dict[i][0][0] in dianjin:
                listall = []
                actid = self.dict[i][2][0]
                actidz = self.dict[i][2][0]
                actname = self.dict[i][0][0]
                acttime = self.dict[i][5][2]
                acttimec = self.dict[i][5][3]
                listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                listall.append(listt)
                listn = []
                for j in range(len(self.dict[i])):
                    activ_j = self.dict[i][j]
                    if j >= 9:
                        listxs = []
                        activ_j[1] = activ_j[1].split(',')[1].split('}')[0] + '次'
                        listxs.append(activ_j[1])
                        listjl = self.jiangli_j(activ_j[2], 0)
                        for k in listjl:
                            listxs.append(k)
                        listall.append(listxs)
                        listxs.append('GoldPointingShow')
                self.dict[i] = listall
            # 消费返利 金币兑换 材料兑换 重生石兑换 材料兑换 神钢兑换 水晶兑换 水果拉霸
            elif self.dict[i][0][0] in xiaofei:
                duihuan = ['金币兑换', '重生石兑换', '材料兑换', '角色魂石兑换', '觉醒石兑换', '神器觉醒', '水晶兑换', '神钢兑换', '守护兑换', '究极之力兑换',
                           '究极之力兑换1', '究极之力兑换2', '角色魂石兑换1', '角色魂石兑换2', '觉醒石兑换1', '觉醒石兑换2']
                duihuan1 = ['水果拉霸']
                duihuan2 = ['超级幸运星']
                listall = []
                actid = self.dict[i][2][0]
                actname = self.dict[i][0][0]
                acttime = self.dict[i][5][2]
                acttimec = self.dict[i][5][3]
                listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                listall.append(listt)
                listn = []
                if self.dict[i][0][0] == '消费返利' or self.dict[i][0][0] == '消费返利全转盘':
                    for j in range(len(self.dict[i])):
                        activ_a = self.dict[i][j]
                        if j >= 9:
                            listxs = []
                            listxs.append(activ_a[0])
                            listjl = self.jiangli_j(activ_a[2], 0)
                            for l in listjl:
                                listxs.append(l)
                            listxs.append(activ_a[3])
                            listall.append(listxs)
                elif self.dict[i][0][0] in duihuan:
                    for j in range(len(self.dict[i])):
                        activ_a = self.dict[i][j]
                        if j >= 9:
                            listxs = []
                            listjl = self.jiangli_j(activ_a[1], 0)
                            for l in listjl:
                                listxs.append(l)
                            listjj = self.jiangli_j(activ_a[2], 0)
                            for k in listjj:
                                listxs.append(k)
                            if activ_a[3] != 'none':
                                listxs.append(activ_a[3])
                            listall.append(listxs)
                elif self.dict[i][0][0] == '原力兑换':
                    for j in range(len(self.dict[i])):
                        activ_a = self.dict[i][j]
                        if j >= 9:
                            listxs = []
                            listjl = self.jiangli_j(activ_a[1], 0)
                            for l in listjl:
                                listxs.append(l)
                            listjj = self.jiangli_j(activ_a[2], 0)
                            for k in listjj:
                                listxs.append(k)
                            listall.append(listxs)
                elif self.dict[i][0][0] in duihuan1:
                    for j in range(len(self.dict[i])):
                        activ_a = self.dict[i][j]
                        if j >= 9:
                            listxs = []
                            listxs.append(activ_a[0])
                            listjj = self.jiangli_j(activ_a[1], 0)
                            for k in listjj:
                                listxs.append(k)
                            listall.append(listxs)
                elif self.dict[i][0][0] in duihuan2:
                    for j in range(len(self.dict[i])):
                        activ_a = self.dict[i][j]
                        if j >= 9:
                            listxs = []
                            listxs.append((activ_a[0] + '0'))
                            listjj = self.jiangli_j(activ_a[2], 0)
                            for k in listjj:
                                listxs.append(k)
                            listxs.append(activ_a[3])
                            listall.append(listxs)
                self.dict[i] = listall
                # for i in self.dict[i]:
                #     print(i)
            # 奇兵夺宝
            elif self.dict[i][0][0] in duobao:
                listall = []
                actid = self.dict[i][2][0]
                actname = self.dict[i][0][0]
                acttime = self.dict[i][5][2]
                acttimec = self.dict[i][5][3]
                acttimed = self.dict[i][5][5]
                listt = [actid, actname, acttime, acttimec,
                         acttimed]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                listall.append(listt)
                for j in range(len(self.dict[i])):
                    listn = []
                    if j > 8 and j < 11:
                        listjl = self.jiangli_j(self.dict[i][j][2], 0)
                        listn.append(self.dict[i][j][1])
                        listn.append(listjl[0])
                        listn.append(listjl[1])
                        listjz = self.jiangli_j(self.dict[i][j][3], 0)
                        listn.append(listjz[0])
                        listn.append(listjz[1])
                        listall.append(listn)
                    elif j > 12:
                        listjl = self.jiangli_j(self.dict[i][j][1], 0)
                        listn.append(self.dict[i][j][0])
                        listn.append(listjl[0])
                        listn.append(listjl[1])
                        listall.append(listn)
                self.dict[i] = listall
                # for i in self.dict[i]:
                #     print(i)
            # 特殊召唤
            elif self.dict[i][0][0] in zhaohuan:
                # for j in self.dict[i]:
                #     print(j)
                listall = []
                actid = self.dict[i][2][0]
                actname = self.dict[i][0][0]
                acttime = self.dict[i][5][2]
                acttimec = self.dict[i][5][3]
                listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                listall.append(listt)
                if self.dict[i][0][0] == '特殊召唤':
                    for j in range(len(self.dict[i])):
                        activ_a = self.dict[i][j]
                        if j >= 9:
                            listj = []
                            lista = self.jiangli_j(activ_a[1], 0)
                            listj.append(lista[1] + lista[0])
                            lista = self.jiangli_j(activ_a[2], 0)
                            for k in lista:
                                listj.append(k)
                            listj.append(activ_a[3])
                            listall.append(listj)
                    self.dict[i] = listall
                elif self.dict[i][0][0] == '召唤特惠':
                    neirong = [self.dict[i][9][1], self.dict[i][9][2]]
                    listall.append(neirong)
                    self.dict[i] = listall
            # 限时特殊召唤
            elif self.dict[i][0][0] in xianshi:
                listall = []
                actid = self.dict[i][2][0]
                actidz = self.dict[i][2][0]
                actname = self.dict[i][0][0]
                acttime = self.dict[i][5][2]
                acttimec = self.dict[i][5][3]
                listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                listall.append(listt)
                listn = []
                for j in range(len(self.dict[i])):
                    activ_j = self.dict[i][j]
                    if j >= 16:
                        listxs = []
                        lista = self.jiangli_j(self.dict[i][j][2], 1)
                        listxs.append((self.dict[i][j][1] + '积分'))
                        for k in lista:
                            listxs.append(k)
                        listall.append(listxs)
                for j in range(len(self.dict[i])):
                    if j >= 11 and j < 15:
                        listxs = []
                        lista = self.jiangli_j(self.dict[i][j][2], 1)
                        if self.dict[i][j][0] == self.dict[i][j][1]:
                            listxs.append(('第' + self.dict[i][j][1] + '名'))
                        else:
                            listxs.append(('第' + self.dict[i][j][0] + '到' + self.dict[i][j][1] + '名'))
                        for k in lista:
                            listxs.append(k)
                        listall.append(listxs)
                self.dict[i] = listall
            # 贵鬼
            elif self.dict[i][0][0] in guigui:
                if self.dict[i][0][0] == '贵鬼的游戏':
                    listall = []
                    actid = self.dict[i][2][0]
                    actidz = self.dict[i][2][0]
                    actname = '贵鬼游戏'
                    acttime = self.dict[i][5][2]
                    acttimec = self.dict[i][5][3]
                    listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                    listall.append(listt)
                    listn = []
                    for j in range(len(self.dict[i])):
                        activ_j = self.dict[i][j]
                        listg = []
                        if j >= 17:
                            listg.append(activ_j[0])
                            listj = self.jiangli_j(activ_j[1], 0)
                            for k in listj:
                                listg.append(k)
                            listall.append(listg)
                    listna = self.jiangli_j(self.dict[i][9][0], 1)
                    listnb = self.jiangli_j(self.dict[i][9][3], 1)
                    listnb.append(self.dict[i][9][2] + '分')
                    for l in listnb:
                        listn.append(l)
                    listnc = self.jiangli_j(self.dict[i][12][5], 0)
                    listnn = []
                    for l in listnc:
                        listnn.append(l)
                    listnn.append(self.dict[i][13][4] + '分')
                    self.dict[i].append(listnn)
                    self.dict[i] = listall
                    self.dict[i].append(listna)
                    self.dict[i].append(listn)
                    self.dict[i].append(listnn)
                elif self.dict[i][0][0] == '贵鬼的奖励':
                    listall = []
                    actid = self.dict[i][2][0]
                    actname = '贵鬼奖励'
                    acttime = self.dict[i][5][2]
                    acttimec = self.dict[i][5][3]
                    listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                    listall.append(listt)
                    listn = []
                    for j in range(len(self.dict[i])):
                        activ_j = self.dict[i][j]
                        listy = []
                        if j >= 9:
                            listy.append(activ_j[0] + '0')
                            listg = self.jiangli_j(activ_j[2], 0)
                            for k in listg:
                                listy.append(k)
                            listy.append('ReChargeShow')
                            listall.append(listy)
                self.dict[i] = listall
            # 魂匣
            elif self.dict[i][0][0].split('-')[0] in hunxia or self.dict[i][0][0][0:2] in hunxia:
                listall = []
                actid = self.dict[i][2][0]
                actname = self.dict[i][0][0]
                acttime = self.dict[i][5][2]
                acttimec = self.dict[i][5][3]
                listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                listall.append(listt)
                activk = self.dict[i][9][5]
                activh = self.dict[i][9][6].split('},{')[0].split('{{')[1]
                activh1 = '1' + self.dict[i][9][7].split(',')[7][1:]
                activh2 = '1' + self.dict[i][9][7].split(',')[8].split('}')[0][1:]
                listt1 = [activk, activh, activh1, activh2]
                listall.append(listt1)
                self.dict[i] = listall
                # for b in self.dict[i]:
                #     print(b)
            # 潘多拉魔盒 女神问答 女神对对碰 旋转派对 副本挑战 守护雅典娜 扭蛋
            elif self.dict[i][0][0] in panduola:
                listall = []
                actid = self.dict[i][2][0]
                actname = self.dict[i][0][0]
                acttime = self.dict[i][5][2]
                acttimec = self.dict[i][5][3]
                listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                listall.append(listt)
                # print(lista1)
                if self.dict[i][0][0] == '潘多拉魔盒':
                    listn = ['库ID：']
                    listn.append(self.dict[i][9][2])
                    cost = self.dict[i][9][1].split('{0,{')[1].split('}}')[0].split(',')
                    for i in cost:
                        listn.append(i)
                    listall.append(listn)
                    self.dict[i] = listall
                elif self.dict[i][0][0] == '女神问答':
                    for j in range(len(self.dict[i])):
                        if j > 14:
                            listjl = []
                            listjl.append(self.dict[i][j][0])
                            jiangli = self.jiangli_j(self.dict[i][j][1], 1)
                            for k in jiangli:
                                listjl.append(k)
                            listall.append(listjl)
                    self.dict[i] = listall
                elif self.dict[i][0][0] == '女神对对碰':
                    self.dict[i] = listall
                elif self.dict[i][0][0] == '开工福利':
                    jiangli = self.jiangli_j(self.dict[i][9][2], 0)
                    listall.append(jiangli)
                    lista = []
                    if self.dict[i][9][1].split(',')[0].split('{')[1] == 'role_level':
                        lista.append('等级')
                        lista.append(self.dict[i][9][1].split(',')[1].split('}')[0])
                    listall.append(lista)
                    self.dict[i] = listall
                elif self.dict[i][0][0] == '副本挑战' or self.dict[i][0][0] == '守护雅典娜':
                    for j in range(len(self.dict[i])):
                        if j >= 9:
                            listjl = []
                            if self.dict[i][j][1].split(',')[0].split('{')[1] == 'total_fb_pass1':
                                mubiao = '普通副本*' + self.dict[i][j][1].split(',')[1].split('}')[0]
                                listjl.append(mubiao)
                            elif self.dict[i][j][1].split(',')[0].split('{')[1] == 'total_fb_pass2':
                                mubiao = '精英副本*' + self.dict[i][j][1].split(',')[1].split('}')[0]
                                listjl.append(mubiao)
                            elif self.dict[i][j][1].split(',')[0].split('{')[1] == 'guard_section':
                                mubiao = '守护雅典娜通关' + self.dict[i][j][1].split(',')[1].split('}')[0] + '波'
                                listjl.append(mubiao)
                            jiangli = self.jiangli_j(self.dict[i][j][2], 0)
                            for k in jiangli:
                                listjl.append(k)
                            listjl.append(self.dict[i][j][3])
                            listall.append(listjl)
                    self.dict[i] = listall
                elif self.dict[i][0][0] == '体力消耗':
                    for j in range(len(self.dict[i])):
                        if j >= 9:
                            listjl = []
                            mubiao = '消耗体力' + self.dict[i][j][1].split(',')[1].split('}')[0] + '点'
                            listjl.append(mubiao)
                            jiangli = self.jiangli_j(self.dict[i][j][2], 0)
                            for k in jiangli:
                                listjl.append(k)
                            listjl.append(self.dict[i][j][3])
                            listall.append(listjl)
                    self.dict[i] = listall
                elif self.dict[i][0][0] == '砸金蛋':
                    jiangli = self.jiangli_j(self.dict[i][9][0], 1)
                    listjl = '砸蛋消耗' + jiangli[1] + '个' + jiangli[0] + "+" + jiangli[3] + jiangli[2]
                    listjla = [listjl]
                    listjlb = []
                    listjlc = []
                    listjld = []
                    listjlb.append(self.dict[i][20][0])
                    listjlb.append('青铜')
                    listjlb.append(self.dict[i][12][1])
                    listjlb.append(self.dict[i][12][2])
                    listjlc.append(self.dict[i][21][0])
                    listjlc.append('白银')
                    listjlc.append(self.dict[i][13][1])
                    listjlc.append(self.dict[i][13][2])
                    listjld.append(self.dict[i][22][0])
                    listjld.append('黄金')
                    listjld.append(self.dict[i][14][1])
                    listjld.append(self.dict[i][14][2])
                    listall.append(listjla)
                    listall.append(listjlb)
                    listall.append(listjlc)
                    listall.append(listjld)
                    self.dict[i] = listall
                elif self.dict[i][0][0] == '扭蛋币':
                    for j in range(len(self.dict[i])):
                        activ_a = self.dict[i][j]
                        if j >= 9:
                            listj = []
                            listj.append(activ_a[0])
                            lista = self.jiangli_j(activ_a[2], 0)
                            for k in lista:
                                listj.append(k)
                            listj.append(activ_a[3])
                            listall.append(listj)
                    self.dict[i] = listall
                    # for b in self.dict[i]:
                    #     print(b)
            # 超级金币翻牌
            elif self.dict[i][0][0] in fanpan:
                listall = []
                actid = self.dict[i][2][0]
                actname = self.dict[i][0][0]
                acttime = self.dict[i][5][2]
                acttimec = self.dict[i][5][3]
                listt = [actid, '超级金币翻牌', acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                listall.append(listt)
                # print(lista1)
                cost = self.jiangli_j(self.dict[i][9][3], 1)
                cost.append(self.dict[i][9][5])
                cost.append(self.dict[i][9][1])
                cost.append(self.dict[i][9][2])
                listall.append(cost)
                for j in range(len(self.dict[i])):
                    if j > 18 and j < 29:
                        reword = self.jiangli_j(self.dict[i][j][1], 1)
                        listall.append(reword)
                    elif j > 30:
                        reword = self.jiangli_j(self.dict[i][j][1], 1)
                        jiangli = self.dict[i][j][0] + '积分'
                        reword.insert(0, jiangli)
                        listall.append(reword)
                self.dict[i] = listall
                # for i in self.dict[i]:
                #     print(i)
            # 幸运转盘
            elif self.dict[i][0][0] in zhuanpan:
                listall = []
                actid = self.dict[i][2][0]
                actname = self.dict[i][0][0]
                acttime = self.dict[i][5][2]
                acttimec = self.dict[i][5][3]
                listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                listall.append(listt)
                # print(listall)
                listxh = self.jiangli_j(self.dict[i][9][3], 1)
                listxh.insert(0, '消耗')
                listall.append(listxh)
                k = 0
                listdy = ['X次后', '奖池内容']
                for j in range(len(self.dict[i])):
                    if self.dict[i][j] == listdy:
                        k = j
                for j in range(len(self.dict[i])):
                    if j > 14 and j < k:
                        listbc = []
                        listbc.append(self.dict[i][j][0] + '次')
                        strjl = self.dict[i][j][1].split('prop,{')[1].split('}}')[0]
                        strjln = self.d_iteam[strjl.split(',')[0]]
                        strjlc = strjl.split(',')[1]
                        listbc.append(strjln)
                        listbc.append(strjlc)
                        listall.append(listbc)
                    elif j > k + 1 and j < k + 4:
                        listg = self.dict[i][j][1].split('}]},')
                        listz = []
                        for l in range(len(listg)):
                            listg1 = listg[l].replace('[', '').replace(']', '').replace('{', '').replace('}', '').split(
                                ',')
                            if l == 0:
                                listg1 = listg1[1:]
                            if listg1[2] == 'prop':
                                listz.append(listg1[0])
                                listz.append(self.d_iteam[listg1[3]])
                                listz.append(listg1[4])
                            elif listg1[2] == 'rmb':
                                listz.append(listg1[0])
                                listz.append(self.d_iteam[listg1[2]])
                                listz.append(listg1[3])
                        listall.append(listz)
                listgl = self.dict[i][k + 11][0].replace('[', '').replace(']', '').replace('}', '').split(',')
                listgln = []
                listgln.append(self.d_iteam[listgl[1]])
                listgln.append(self.d_iteam[listgl[2]])
                listgln.append(self.d_iteam[listgl[3]])
                listall.append(listgln)
                listxx = str(self.dict[i][-1][0]).split('[')[1].split(']')[0].split(',')
                listall.append(listxx)
                self.dict[i] = listall
                # for i in self.dict[i]:
                #     print(i)
            # 体力双倍
            elif self.dict[i][0][0] in tili:
                listall = []
                actid = self.dict[i][2][0]
                actname = self.dict[i][0][0]
                acttime = self.dict[i][5][2]
                acttimec = self.dict[i][5][3]
                listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                listall.append(listt)
                if self.dict[i][7][0] == '类型':
                    listn = []
                    listn = self.dict[i][9]
                    listall.append(listn)
                else:
                    listm = []
                    listm = self.dict[i][8][2]
                    listall.append(listm)
                self.dict[i] = listall
                # for i in self.dict[i]:
                #     print(i)
            # 圣器双倍
            elif self.dict[i][0][0] in shengqi:
                listall = []
                actid = self.dict[i][2][0]
                actname = self.dict[i][0][0]
                acttime = self.dict[i][5][2]
                acttimec = self.dict[i][5][3]
                listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                listall.append(listt)
                if self.dict[i][7][0] == '图标':
                    gonggao = [self.dict[i][8][2]]
                    listall.append(gonggao)
                else:
                    diaoluo1 = [self.dict[i][9][0], self.dict[i][9][1]]
                    diaoluo2 = [self.dict[i][10][0], self.dict[i][10][1]]
                    listall.append(diaoluo1)
                    listall.append(diaoluo2)
                self.dict[i] = listall
            # 圣衣双倍
            elif self.dict[i][0][0] in shengyi:
                listall = []
                actid = self.dict[i][2][0]
                actname = self.dict[i][0][0]
                acttime = self.dict[i][5][2]
                acttimec = self.dict[i][5][3]
                listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                listall.append(listt)
                if self.dict[i][7][0] == '图标':
                    gonggao = [self.dict[i][8][2]]
                    listall.append(gonggao)
                else:
                    diaoluo1 = [self.dict[i][9][0], self.dict[i][9][1]]
                    listall.append(diaoluo1)
                self.dict[i] = listall
                for j in self.dict[i]:
                    print(j)
            # 消消乐
            elif self.dict[i][0][0] == '斗士消消乐':
                listall = []
                actid = self.dict[i][2][0]
                actidz = self.dict[i][2][0]
                actname = '消消乐'
                acttime = self.dict[i][5][2]
                acttimec = self.dict[i][5][3]
                listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                listall.append(listt)
                listn = []
                for j in range(len(self.dict[i])):
                    if j >= 15 and j < 20:
                        listxs = []
                        lista = self.jiangli_j(self.dict[i][j][2], 0)
                        if self.dict[i][j][0] == self.dict[i][j][1]:
                            listxs.append(self.dict[i][j][1])
                        else:
                            listxs.append((self.dict[i][j][0] + '至' + self.dict[i][j][1]))
                        for k in lista:
                            listxs.append(k)
                        listall.append(listxs)
                self.dict[i] = listall
                # for i in self.dict[i]:
                #     print(i)
            # 团购
            elif self.dict[i][0][0] in tuangou:
                listall = []
                actid = self.dict[i][2][0]
                actidz = self.dict[i][2][0]
                actname = self.dict[i][0][0]
                acttime = self.dict[i][5][2]
                acttimec = self.dict[i][5][3]
                listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                listall.append(listt)
                listn = []
                listn.append(self.dict[i][9][0])
                listn.append(self.dict[i][9][1])
                listall.append(listn)
                jiangli = self.jiangli_j(self.dict[i][9][2], 0)
                for j in jiangli:
                    listn.append(j)
                for k in range(len(self.dict[i])):
                    listm = []
                    if k > 11:
                        listm = self.dict[i][k]
                        listall.append(listm)
                self.dict[i] = listall
            # 活跃有礼
            elif self.dict[i][0][0] in huoyue:
                listall = []
                actid = self.dict[i][2][0]
                actidz = self.dict[i][2][0]
                actname = self.dict[i][0][0]
                acttime = self.dict[i][5][2]
                acttimec = self.dict[i][5][3]
                listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                listall.append(listt)
                dicth = {}
                dicth['draw_rmb'] = ['钻石抽奖', '次', 'LotteryShow+2']
                dicth['boss_times'] = ['BOSS挑战', '次', 'BossFightViewShow']
                dicth['arena_integral'] = ['竞技场获得', '分', 'ArenaViewShow']
                dicth['alchemys'] = ['点金', '次', 'GoldPointingShow']
                dicth['draw_special'] = ['特殊召唤', '次', 'HeroBgShow+3']
                dicth['draw_money'] = ['金币抽奖次数', '次', 'HeroBgShow+3']
                dicth['arena_win'] = ['竞技场胜利', '次', 'HeroBgShow+3']
                dicth['consume_arena_times'] = ['参与竞技场', '次', 'HeroBgShow+3']
                dicth['nebula_consume'] = ['星力消耗', '', 'HeroBgShow+3']
                for j in range(len(self.dict[i])):
                    activ_a = self.dict[i][j]
                    if j >= 9:
                        listxs = []
                        listjl = self.jiangli_j(activ_a[2], 0)
                        for l in listjl:
                            listxs.append(l)
                        tiaomu = dicth[activ_a[1].split(',')[0].split('{')[1]][0] + activ_a[1].split(',')[1].split('}')[
                            0] + dicth[activ_a[1].split(',')[0].split('{')[1]][1]
                        listxs.insert(0, tiaomu)
                        listxs.append(dicth[activ_a[1].split(',')[0].split('{')[1]][2])
                        listall.append(listxs)
                self.dict[i] = listall
                # for i in self.dict[i]:
                #     print(i)
            elif self.dict[i][0][0] == '欢乐射击':
                listall = []
                actid = self.dict[i][2][0]
                actidz = self.dict[i][2][0]
                actname = self.dict[i][0][0]
                acttime = self.dict[i][5][2]
                acttimec = self.dict[i][5][3]
                listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                listall.append(listt)
                self.dict[i] = listall
            # print(i)
            # for k in self.dict[i]:
            #     print(k)
            self.dict_final[self.dict[i][0][0]] = self.dict[i]
        return self.dict_final

class Time():
    def __init__(self,url,types,datein):
        self.t=types
        self.d=datein
        self.u=url
        self.a = '/sgame_gm/server_port/server_time'
    def time(self):
        #查询：：1；重置：2；修改：3
        url = '%s%s' % (self.u, self.a)
        data = {  # 发送的参数
            "type": self.t,
            "time": "",
            "date": self.d,
            "user": "admin",
            "password": "123456"

        }
        r = requests.post(url, data)
        return r.text

class ui_compare(QMainWindow,activ.Ui_MainWindow):
    def __init__(self):
        super(ui_compare,self).__init__()
        self.ui=activ.Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.tabWidget.setTabText(self.ui.tabWidget.indexOf(self.ui.t_1),'3434')
        # self.ui.t_4=QtWidgets.QWidget()
        # self.ui.t_4.setObjectName('4')
        # self.ui.tabWidget.addTab(self.ui.t_4,'444')
        # self.ui.tabWidget.removeTab(self.ui.tab_2)
        self.ui.b_load.clicked.connect(lambda :self.compare_d())
        self.ui.excel_1.clicked.connect(lambda :self.getmassage(1))
        self.ui.excel_2.clicked.connect(lambda: self.getmassage(2))
        self.listr=[]
        self.liste=[]
        self.lists=[]
        self.ui.checkBox.clicked.connect(lambda :self.check(1))
        self.ui.checkBox_2.clicked.connect(lambda :self.check(2))
        self.ui.checkBox_3.clicked.connect(lambda :self.check(3))
        self.ui.c_xiangxi.clicked.connect(lambda :self.check(4))
        self.ui.c_suonlue.clicked.connect(lambda :self.check(5))
        self.ui.b_selectCard.clicked.connect(lambda :self.getCard())
        self.ui.b_selectItem.clicked.connect(lambda :self.getIteam())
        self.ui.b_selectExcel.clicked.connect(lambda :self.getExcel())
    def check(self,a):
        if a==1:
            self.ui.checkBox.setChecked(True)
            self.ui.checkBox_2.setChecked(False)
            self.ui.checkBox_3.setChecked(False)
        elif a==2:
            self.ui.checkBox.setChecked(False)
            self.ui.checkBox_2.setChecked(True)
            self.ui.checkBox_3.setChecked(False)
        elif a==3:
            self.ui.checkBox.setChecked(False)
            self.ui.checkBox_2.setChecked(False)
            self.ui.checkBox_3.setChecked(True)
        elif a==4:
            self.ui.c_suonlue.setChecked(False)
            self.ui.c_xiangxi.setChecked(True)
        elif a==5:
            self.ui.c_suonlue.setChecked(True)
            self.ui.c_xiangxi.setChecked(False)
    def getSever(self):
        pass
    def getIteam(self):
        self.openfile_iteam=QFileDialog.getOpenFileName(self,'选择文件','','Txt files(*.txt)')
    def getCard(self):
        self.openfile_card = QFileDialog.getOpenFileName(self, '选择文件', '', 'Txt files(*.txt)')
    def getExcel(self):
        self.openfile_name=QFileDialog.getOpenFileName(self,'选择文件','','Excel files(*.xlsx , *.xls)')

    def compare_d(self):
        page=self.ui.l_ename.text()
        if page=='':
            page='Sheet3'
        print(1)
        urln=dict_sAdress[self.ui.comboBox.currentText()]
        time=self.ui.calendarWidget.selectedDate()
        ddd=str(time).split('(')[1].split(')')[0].split(',')
        aaa='2020-09-05 12:00:00'
        print(aaa)
        Time(urln,'3',aaa).time()
        self.ui.pushButton.setText(aaa)
        print(1111)
        self.excel = sever(urln,self.openfile_iteam[0],self.openfile_card[0]).jx_huodong()
        # sever(urln,self.openfile_iteam,self.openfile_card).get_activ()
        # sever(urln,self.openfile_iteam,self.openfile_card).j_activ()
        # self.sever=sever(urln,self.openfile_iteam,self.openfile_card).jx_huodong()
        self.sever= sever(urln,self.openfile_iteam[0],self.openfile_card[0]).jx_huodong()
        self.model_2 = QStandardItemModel(3,8)
        self.ui.excel_2.setModel(self.model_2)
        self.model_1 = QStandardItemModel(3, 8)
        self.ui.excel_1.setModel(self.model_1)
        self.ui.excel_1.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.excel_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        r=0
        #使对比的活动表和服务器返回的字典里key完全相同，缺少的加一个空活动进去
        for key in self.sever.keys():
            if self.excel.__contains__(key)==False:
                self.excel[key]=[[key,'活动不存在']]
        for key in self.excel.keys():
            if self.sever.__contains__(key)==False:
                self.sever[key]=[[key,'活动不存在']]

        for key in self.sever.keys():
            #使同一个活动的列数相同，少的加空行
            a=len(self.sever[key])
            b=len(self.excel[key])
            if a>b:
                for c in range(a-b):
                    self.excel[key].append([])
            elif a<b:
                lists=[]
                for c in range(b-a):
                    lists=self.excel[key]
                    lists.append([])
                self.excel[key]=lists
            b=True
            if self.excel[key]!=self.sever[key]:
                b=False
            for i in range(len(self.sever[key])):
                #处理活动的列数，保证表格和服务器一致
                d=len(self.sever[key][i])
                e=len(self.excel[key][i])
                if d>e:
                    for c in range(d - e):
                        self.excel[key][i].append('')
                elif d< e:
                    lists = []
                    for c in range(e - d):
                        lists = self.sever[key][i]
                        lists.append('')
                    self.sever[key][i] = lists
                a=True
                if self.sever[key][i] != self.excel[key][i]:
                    a=False
                #显示所有活动内容
                for j in range(len(self.sever[key][i])):
                    r_sever=QStandardItem(self.sever[key][i][j])
                    r_excel=QStandardItem(self.excel[key][i][j])
                    if self.sever[key][i][j] !=self.excel[key][i][j]:
                        self.listr.append([r,j])
                    self.model_1.setItem(r,j,r_sever)
                    self.model_2.setItem(r,j,r_excel)
                    if a==False:
                        # r_sever.setForeground(QColor(255,0,0))
                        r_excel.setBackground(QColor(255,0,0))
                        r_sever.setBackground(QColor(255,0,0))
                    if b==False and i==0:
                        r_excel.setBackground(QColor(255, 255, 0))
                        r_sever.setBackground(QColor(255, 255, 0))
                self.liste.append(self.excel[key][i])
                self.lists.append(self.sever[key][i])
                r+=1
            r+=1
            self.liste.append(self.excel[key][i])
            self.lists.append(self.sever[key][i])
    def getmassage(self,a):
        if a==1:
            row=self.ui.excel_1.currentIndex().row()
        else:
            row=self.ui.excel_2.currentIndex().row()
        self.model_3=QStandardItemModel(1,10)
        self.model_4=QStandardItemModel(1,10)
        self.ui.tableView_3.setModel(self.model_4)
        self.ui.tableView_4.setModel(self.model_3)
        self.ui.tableView_3.verticalHeader().setVisible(False)
        self.ui.tableView_4.horizontalHeader().setVisible(False)
        self.ui.tableView_4.verticalHeader().setVisible(False)
        self.ui.tableView_3.horizontalHeader().setVisible(False)
        self.ui.tableView_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableView_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
        for i in range(len(self.liste[row])):
            zuobiao=[row,i]
            r_severline=QStandardItem(self.liste[row][i])
            r_excelline=QStandardItem(self.lists[row][i])
            self.model_4.setItem(0,i,r_excelline)
            self.model_3.setItem(0,i,r_severline)
            if zuobiao in self.listr:
                r_severline.setBackground(QColor(255,0,0))
                r_excelline.setBackground(QColor(255,0,0))




if __name__=='__main__':
    app=QApplication(sys.argv) #外部输入的沟通桥梁
    find=ui_compare()
    find.show()
    sys.exit(app.exec_())