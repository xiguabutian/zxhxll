import requests
import urllib3
import selenium
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
path.append(r'E:\ceshi\AT\public')
from GM import *
#读取道具配置表
def dict_item(itempath):
    itempath='E:/shendoushi/client/Int/Dev/Unity/Assets/Resources/Config/Game/ItemConfig.txt'
    item_l=[]
    d_item={}
    with open(itempath, 'r',encoding='UTF-8') as file_to_read:
        while True:
            lines = file_to_read.readline() # 整行读取数据
            if not lines:
                break
                pass
            item = [i for i in lines.split()] # 将整行数据分割处理
            item_l.append(item)
    for i in item_l:
        try: #装备和普通道具在表里的位置不一样，装备在第6，普通道具在第5
            int(i[5]) #如果第5个不是数字，就是道具，是数字，就是装备
            d_item[i[0]]=i[6]
        except: #道具就走这里
            try:
                int(i[6])
                d_item[i[0]]=i[5]
            except:
                d_item[i[0]]=i[5]+i[6]
    d_item['rmb']='钻石'
    d_item['role_money']='游戏币'
    d_item['times']='次数'
    d_item['draw_special']='次'
    d_item['5202']='5202'
    d_item['5019']='5019'
    d_item['5020']='5020'
    d_item['5021']='5021'
    return d_item

#读取究极之力获取ID和名称
def dict_card(cardpatch):
    cardpatch='E:/shendoushi/client/Patch/Dev/Unity/Assets/Resources/Config/Game/RoleEquipCard/RoleEquipCardItemCfg.txt'
    card_l=[]
    d_card={}
    with open(cardpatch, 'r',encoding='UTF-8') as file_to_read:
        while True:
            lines = file_to_read.readline() # 整行读取数据
            if not lines:
                break
                pass
            card = [i for i in lines.split()] # 将整行数据分割处理
            card_l.append(card)
    for i in card_l:
            d_card[i[0]]=i[1]
    return d_card

#读取网页数据
def get_activ(host,api):    #从服务器获取现在开启的所有活动
    # host2 = 'http://120.92.15.130:902' #渠道验收服
    # host1='http://120.92.9.137:882' #对外安卓
    # host='http://192.168.9.11:882' #本地服
    # host3='http://120.92.9.137:872' #对外IOS
    # api = '/sgame_gm/gm_active_port/get_activeshow' #查询服务器开启活动的接口
    url = '%s%s' % (host, api)
    data = {  #发送的参数
        "type":"1",
        'user': 'admin',
        'password': '123456',
        'active_m':'active_checkin-active_consume_buy-active_exchange-active_first_cash_double-active_one_cash_double-active_one_cash-active_total_cash-active_total_consume',
    }
    r = requests.post(url, data)
    return r

#解析活动的数据并返回一个dict
def j_activ(html_r):
    soup=BeautifulSoup(html_r.text,'lxml')
    table=soup.find_all(name='table',attrs={'border':3})
    activ=[]
    for tab in table:
        tr_arr = tab.find_all('tr')#把数据分列
        for tr in tr_arr:
            activ1 = []
            #print(tr)
            td_s=tr.find_all('td') #把列的数据分格
            #print(type(td_s))
            for td in td_s:
                td_o=td.string
                activ1.append(td_o)
                #print((activ1))
            #print(activ1)
            activ.append(activ1)
        activ.append("这是一个标记")
    dict = {}
    activ2 = []
    f=0
    for i in activ:
        #print(i)
        if i != "这是一个标记":
            activ2.append(i)
            #print(activ2)
        else:
            f += 1
            dict[f] = activ2
            activ2 = []
            #print(f)
    return dict

#传入奖励 '[{role_money,540000},{prop,{3502,6}},{prop,{3576,2}}]'
def jiangli_jx(jiangli,fanzhuan): #传入奖励 '[{role_money,540000},{prop,{3502,6}},{prop,{3576,2}}]'
    liste=[]
    if '},{' in jiangli and '[' in jiangli:
        jiangli=jiangli.replace('},{','/').replace('{','').replace('}','')
        jiangli=jiangli.replace('[','').replace(']','') #替换掉括号
        jianglia=jiangli.split('/')
    elif '[' in jiangli:
        jiangli = jiangli.replace('[', '').replace(']', '').replace('{','').replace('}','')
        jianglia=[]
        jianglia.append(jiangli)
    else:
        jiangli = jiangli.replace('{', '').replace('}', '')
        jianglia = []
        jianglia.append(jiangli)
    daoju=['prop']
    jinbi=['role_money','rmb','times','draw_special']
    jiuji=['force_card']
    yingxiong=['hero']
    if fanzhuan==1:
        for a in range(len(jianglia)):
            jianglia[a]=jianglia[a].split(',')
            #print(jianglia[a])
            if jianglia[a][0] in daoju: #判断道具类型
                jianglia[a][1]=d_item[jianglia[a][1]]
                liste.append(jianglia[a][1])
                liste.append(jianglia[a][2])
            elif jianglia[a][0] in jiuji:
                #print(jianglia[a])
                jianglia[a][1] = d_card[jianglia[a][1]]
                if int(jianglia[a][2])>1:
                    jianglia[a][1]=jianglia[a][2]+'星'+jianglia[a][1]
                #print(jianglia[a])
                liste.append(jianglia[a][1])
                liste.append(jianglia[a][3])
            elif jianglia[a][0] in yingxiong:
                jianglia[a][1] =jianglia[a][2] +'星'+ d_item['4'+jianglia[a][1][1:4]].split('魂石')[0]
                liste.append(jianglia[a][1])
                liste.append(jianglia[a][3])
            elif jianglia[a][0] in jinbi:
                jianglia[a][0] = d_item[jianglia[a][0]]
                #print(d_item['role_money'])
                liste.append(jianglia[a][0])
                liste.append(jianglia[a][1])
    elif fanzhuan==0:
        for a in reversed(range(len(jianglia))):
            jianglia[a]=jianglia[a].split(',')
            #print(jianglia[a])
            if jianglia[a][0] in daoju: #判断道具类型
                jianglia[a][1]=d_item[jianglia[a][1]]
                liste.append(jianglia[a][1])
                liste.append(jianglia[a][2])
            elif jianglia[a][0] in jiuji:
                #print(jianglia[a])
                jianglia[a][1] = d_card[jianglia[a][1]]
                if int(jianglia[a][2])>1:
                    jianglia[a][1]=jianglia[a][2]+'星'+jianglia[a][1]
                #print(jianglia[a])
                liste.append(jianglia[a][1])
                liste.append(jianglia[a][3])
            elif jianglia[a][0] in yingxiong:
                jianglia[a][1] =jianglia[a][2] +'星'+ d_item['4'+jianglia[a][1][1:4]].split('魂石')[0]
                liste.append(jianglia[a][1])
                liste.append(jianglia[a][3])
            elif jianglia[a][0] in jinbi:
                jianglia[a][0] = d_item[jianglia[a][0]]
                #print(d_item['role_money'])
                liste.append(jianglia[a][0])
                liste.append(jianglia[a][1])
    return liste

#按格式把活动解析到字典里方便对比
def jx_huodong(dict_e):
    dict_finall={}
    for i in list(dict_e.keys()):
        chongzhi=['充值有礼']
        leijicz=['累计充值']
        yuanli=['原力抽卡']
        dianjin=['点金返利']
        xiaofei=['消费返利','消费返利全转盘','金币兑换','原力兑换','重生石兑换','材料兑换','角色魂石兑换','觉醒石兑换','神器觉醒','水晶兑换','神钢兑换','水果拉霸','超级幸运星','守护兑换','究极之力兑换','究极之力兑换1','究极之力兑换2','角色魂石兑换1','角色魂石兑换2','觉醒石兑换1','觉醒石兑换2']
        duobao=['奇兵夺宝']
        zhaohuan=['特殊召唤','召唤特惠']
        xianshi=['限时特殊召唤']
        guigui=['贵鬼的游戏','贵鬼的奖励']
        hunxia=['魂匣','神圣']
        panduola=['潘多拉魔盒','女神问答','女神对对碰','开工福利','副本挑战','守护雅典娜','体力消耗','砸金蛋','扭蛋币']
        fanpan=['超级金币翻牌','金币翻牌']
        zhuanpan=['幸运转盘']
        tili=['体力双倍']
        tuangou=['超级团购']
        huoyue=['活跃有礼']
        shengqi=['圣器双倍']
        shengyi=['圣衣双倍']
        shuangbei=['双倍充值']
        activ_a=dict_e[i]
        listb= []
        # print('')
        # print(i)
        # for j in dict_e[i]:
        #     print(j)
        #每日充值活动
        if dict_e[i][0][0] in chongzhi:
            listc=[]
            listd=[]
            actid=dict_e[i][2][0]
            actname=dict_e[i][0][0]
            acttime=dict_e[i][5][2]
            acttimec=dict_e[i][5][3]
            listd=[actid,actname,acttime,acttimec] #['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
            listc.append(listd)
            for j in range(len(activ_a)):
                activ_j=activ_a[j]
                if j>=9:
                    liste=[]
                    if activ_j[2]=='1':
                        slect='可选'
                        liste.append(slect)
                    else:
                        day=activ_j[0]+'天'
                        charge=activ_j[1].split(',')[1].split('}')[0]+'0'
                        liste.append(charge)
                        liste.append(day)
                    jiangli=jiangli_jx(activ_j[3],0)
                    for k in jiangli:
                        liste.append(k)
                    listc.append(liste)
            dict_e[i]=listc

        #累计充值活动
        elif dict_e[i][0][0] in leijicz:
            listdz = []
            actid = dict_e[i][2][0]
            actidz = dict_e[i][2][0]
            actname = dict_e[i][0][0]
            acttime = dict_e[i][5][2]
            acttimec = dict_e[i][5][3]
            listdz = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
            listez = []
            listez.append(listdz)
            for j in range(len(activ_a)):
                activ_j=activ_a[j]
                if j>=9:
                    listjx=[]
                    if activ_j[1]=='1': #读取奖励的可选状态
                        slect='可选'
                        listjx.append(slect)
                    else: #读取奖励的充值金额
                        charge = activ_j[0]+'0'
                        listjx.append(charge)
                    listjl=jiangli_jx(activ_j[2],0)
                    for k in listjl:
                        listjx.append(k)
                    listez.append(listjx)
            dict_e[i]=listez
        elif dict_e[i][0][0] in shuangbei:
            listdz = []
            actid = dict_e[i][2][0]
            actidz = dict_e[i][2][0]
            actname = dict_e[i][0][0]
            acttime = dict_e[i][5][2]
            acttimec = dict_e[i][5][3]
            listdz = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
            listez = []
            listez.append(listdz)
            for j in range(len(activ_a)):
                activ_j=activ_a[j]
                if j>=9:
                    listjx=[]
                    listjx.append(activ_j[1])
                    listjx.append((activ_j[3]+'次'))
                    listjl=jiangli_jx(activ_j[4],0)
                    for k in listjl:
                        listjx.append(k)
                    listez.append(listjx)
            dict_e[i]=listez
        #跨服究极之力抽卡活动
        elif dict_e[i][0][0] in yuanli:
            lista = []
            actid = dict_e[i][2][0]
            actidz = dict_e[i][2][0]
            actname = '跨服抢购'
            acttime = dict_e[i][5][2]
            acttimec = dict_e[i][5][3]
            listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
            lista.append(listt)
            listn = []
            listn.append(dict_e[i][9][0])
            listn.append(dict_e[i][9][1])
            listn.append(dict_e[i][9][2])
            listn.append(dict_e[i][9][3])
            listn.append(dict_e[i][9][5])
            lista.append(listn) #['300100', '10', '3000', '500', '1']
            for j in range(len(dict_e[i])):
                activ_j=dict_e[i][j]
                if j>=12:
                    listxs=[]
                    listxs.append(activ_j[0])
                    listxs.append(activ_j[1])
                    listjl=jiangli_jx(activ_j[2],0)
                    for k in listjl:
                        listxs.append(k)
                    lista.append(listxs)
            dict_e[i]=lista
        #点金
        elif dict_e[i][0][0] in dianjin:
            listall = []
            actid = dict_e[i][2][0]
            actidz = dict_e[i][2][0]
            actname = dict_e[i][0][0]
            acttime = dict_e[i][5][2]
            acttimec = dict_e[i][5][3]
            listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
            listall.append(listt)
            listn = []
            for j in range(len(dict_e[i])):
                activ_j=dict_e[i][j]
                if j>=9:
                    listxs=[]
                    activ_j[1]=activ_j[1].split(',')[1].split('}')[0]+'次'
                    listxs.append(activ_j[1])
                    listjl=jiangli_jx(activ_j[2],0)
                    for k in listjl:
                        listxs.append(k)
                    listall.append(listxs)
                    listxs.append('GoldPointingShow')
            dict_e[i] = listall
        #消费返利 金币兑换 材料兑换 重生石兑换 材料兑换 神钢兑换 水晶兑换 水果拉霸
        elif dict_e[i][0][0] in xiaofei:
            duihuan=['金币兑换','重生石兑换','材料兑换','角色魂石兑换','觉醒石兑换','神器觉醒','水晶兑换','神钢兑换','守护兑换','究极之力兑换','究极之力兑换1','究极之力兑换2','角色魂石兑换1','角色魂石兑换2','觉醒石兑换1','觉醒石兑换2']
            duihuan1=['水果拉霸']
            duihuan2=['超级幸运星']
            listall = []
            actid = dict_e[i][2][0]
            actname = dict_e[i][0][0]
            acttime = dict_e[i][5][2]
            acttimec = dict_e[i][5][3]
            listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
            listall.append(listt)
            listn = []
            if dict_e[i][0][0]=='消费返利' or dict_e[i][0][0]=='消费返利全转盘':
                for j in range(len(dict_e[i])):
                    activ_a = dict_e[i][j]
                    if j >= 9:
                        listxs = []
                        listxs.append(activ_a[0])
                        listjl = jiangli_jx(activ_a[2],0)
                        for l in listjl:
                            listxs.append(l)
                        listxs.append(activ_a[3])
                        listall.append(listxs)
            elif dict_e[i][0][0] in duihuan:
                for j in range(len(dict_e[i])):
                    activ_a = dict_e[i][j]
                    if j >= 9:
                        listxs = []
                        listjl = jiangli_jx(activ_a[1],0)
                        for l in listjl:
                            listxs.append(l)
                        listjj = jiangli_jx(activ_a[2],0)
                        for k in listjj:
                            listxs.append(k)
                        if activ_a[3]!='none':
                            listxs.append(activ_a[3])
                        listall.append(listxs)
            elif dict_e[i][0][0]=='原力兑换':
                for j in range(len(dict_e[i])):
                    activ_a = dict_e[i][j]
                    if j >= 9:
                        listxs = []
                        listjl = jiangli_jx(activ_a[1],0)
                        for l in listjl:
                            listxs.append(l)
                        listjj = jiangli_jx(activ_a[2],0)
                        for k in listjj:
                            listxs.append(k)
                        listall.append(listxs)
            elif dict_e[i][0][0] in duihuan1:
                for j in range(len(dict_e[i])):
                    activ_a = dict_e[i][j]
                    if j >= 9:
                        listxs = []
                        listxs.append(activ_a[0])
                        listjj = jiangli_jx(activ_a[1],0)
                        for k in listjj:
                            listxs.append(k)
                        listall.append(listxs)
            elif dict_e[i][0][0] in duihuan2:
                for j in range(len(dict_e[i])):
                    activ_a = dict_e[i][j]
                    if j >= 9:
                        listxs = []
                        listxs.append((activ_a[0]+'0'))
                        listjj = jiangli_jx(activ_a[2],0)
                        for k in listjj:
                            listxs.append(k)
                        listxs.append(activ_a[3])
                        listall.append(listxs)
            dict_e[i] = listall
            # for i in dict_e[i]:
            #     print(i)
         #奇兵夺宝
        elif dict_e[i][0][0] in duobao:
            listall= []
            actid = dict_e[i][2][0]
            actname = dict_e[i][0][0]
            acttime = dict_e[i][5][2]
            acttimec = dict_e[i][5][3]
            acttimed=dict_e[i][5][5]
            listt = [actid, actname, acttime, acttimec,acttimed]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
            listall.append(listt)
            for j in range(len(dict_e[i])):
                listn = []
                if j>8 and j<11:
                    listjl = jiangli_jx(dict_e[i][j][2],0)
                    listn.append(dict_e[i][j][1])
                    listn.append(listjl[0])
                    listn.append(listjl[1])
                    listjz = jiangli_jx(dict_e[i][j][3],0)
                    listn.append(listjz[0])
                    listn.append(listjz[1])
                    listall.append(listn)
                elif j>12:
                    listjl = jiangli_jx(dict_e[i][j][1],0)
                    listn.append(dict_e[i][j][0])
                    listn.append(listjl[0])
                    listn.append(listjl[1])
                    listall.append(listn)
            dict_e[i] = listall
            # for i in dict_e[i]:
            #     print(i)
        #特殊召唤
        elif dict_e[i][0][0] in zhaohuan:
            # for j in dict_e[i]:
            #     print(j)
            listall = []
            actid = dict_e[i][2][0]
            actname = dict_e[i][0][0]
            acttime = dict_e[i][5][2]
            acttimec = dict_e[i][5][3]
            listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
            listall.append(listt)
            if dict_e[i][0][0]=='特殊召唤':
                for j in range(len(dict_e[i])):
                    activ_a = dict_e[i][j]
                    if j >= 9:
                        listj = []
                        lista=jiangli_jx(activ_a[1],0)
                        listj.append(lista[1]+lista[0])
                        lista = jiangli_jx(activ_a[2],0)
                        for k in lista:
                            listj.append(k)
                        listj.append(activ_a[3])
                        listall.append(listj)
                dict_e[i]=listall
            elif dict_e[i][0][0]=='召唤特惠':
                neirong=[dict_e[i][9][1],dict_e[i][9][2]]
                listall.append(neirong)
                dict_e[i] = listall
        #限时特殊召唤
        elif dict_e[i][0][0] in xianshi:
            listall = []
            actid = dict_e[i][2][0]
            actidz = dict_e[i][2][0]
            actname = dict_e[i][0][0]
            acttime = dict_e[i][5][2]
            acttimec = dict_e[i][5][3]
            listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
            listall.append(listt)
            listn = []
            for j in range(len(dict_e[i])):
                activ_j=dict_e[i][j]
                if j>=16:
                    listxs=[]
                    lista=jiangli_jx(dict_e[i][j][2],1)
                    listxs.append((dict_e[i][j][1]+'积分'))
                    for k in lista:
                        listxs.append(k)
                    listall.append(listxs)
            for j in range(len(dict_e[i])):
                if j>=11 and j<15:
                    listxs=[]
                    lista=jiangli_jx(dict_e[i][j][2],1)
                    if dict_e[i][j][0]==dict_e[i][j][1]:
                        listxs.append(('第'+dict_e[i][j][1]+'名'))
                    else:
                        listxs.append(('第' + dict_e[i][j][0] + '到'+dict_e[i][j][1]+'名'))
                    for k in lista:
                        listxs.append(k)
                    listall.append(listxs)
            dict_e[i] = listall
        #贵鬼
        elif dict_e[i][0][0] in guigui:
            if dict_e[i][0][0]=='贵鬼的游戏':
                listall = []
                actid = dict_e[i][2][0]
                actidz = dict_e[i][2][0]
                actname = '贵鬼游戏'
                acttime = dict_e[i][5][2]
                acttimec = dict_e[i][5][3]
                listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                listall.append(listt)
                listn = []
                for j in range(len(dict_e[i])):
                    activ_j = dict_e[i][j]
                    listg=[]
                    if j >= 17:
                        listg.append(activ_j[0])
                        listj=jiangli_jx(activ_j[1],0)
                        for k in listj:
                            listg.append(k)
                        listall.append(listg)
                listna=jiangli_jx(dict_e[i][9][0],1)
                listnb=jiangli_jx(dict_e[i][9][3],1)
                listnb.append(dict_e[i][9][2]+'分')
                for l in listnb:
                    listn.append(l)
                listnc = jiangli_jx(dict_e[i][12][5],0)
                listnn=[]
                for l in listnc:
                    listnn.append(l)
                listnn.append(dict_e[i][13][4]+'分')
                dict_e[i].append(listnn)
                dict_e[i]=listall
                dict_e[i].append(listna)
                dict_e[i].append(listn)
                dict_e[i].append(listnn)
            elif dict_e[i][0][0]=='贵鬼的奖励':
                listall = []
                actid = dict_e[i][2][0]
                actname = '贵鬼奖励'
                acttime = dict_e[i][5][2]
                acttimec = dict_e[i][5][3]
                listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
                listall.append(listt)
                listn = []
                for j in range(len(dict_e[i])):
                    activ_j = dict_e[i][j]
                    listy = []
                    if j >= 9:
                        listy.append(activ_j[0]+'0')
                        listg=jiangli_jx(activ_j[2],0)
                        for k in listg:
                            listy.append(k)
                        listy.append('ReChargeShow')
                        listall.append(listy)
            dict_e[i]=listall
        #魂匣
        elif dict_e[i][0][0].split('-')[0]in hunxia or dict_e[i][0][0][0:2] in hunxia:
            listall = []
            actid = dict_e[i][2][0]
            actname = dict_e[i][0][0]
            acttime = dict_e[i][5][2]
            acttimec = dict_e[i][5][3]
            listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
            listall.append(listt)
            activk=dict_e[i][9][5]
            activh=dict_e[i][9][6].split('},{')[0].split('{{')[1]
            activh1='1'+dict_e[i][9][7].split(',')[7][1:]
            activh2 = '1' + dict_e[i][9][7].split(',')[8].split('}')[0][1:]
            listt1=[activk,activh,activh1,activh2]
            listall.append(listt1)
            dict_e[i]=listall
            # for b in dict_e[i]:
            #     print(b)
        #潘多拉魔盒 女神问答 女神对对碰 旋转派对 副本挑战 守护雅典娜 扭蛋
        elif dict_e[i][0][0] in panduola:
            listall = []
            actid = dict_e[i][2][0]
            actname = dict_e[i][0][0]
            acttime = dict_e[i][5][2]
            acttimec = dict_e[i][5][3]
            listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
            listall.append(listt)
            #print(lista1)
            if dict_e[i][0][0]=='潘多拉魔盒':
                listn=['库ID：']
                listn.append(dict_e[i][9][2])
                cost=dict_e[i][9][1].split('{0,{')[1].split('}}')[0].split(',')
                for i in cost:
                    listn.append(i)
                listall.append(listn)
                dict_e[i]=listall
            elif dict_e[i][0][0] == '女神问答':
                for j in range(len(dict_e[i])):
                    if j>14:
                        listjl=[]
                        listjl.append(dict_e[i][j][0])
                        jiangli=jiangli_jx(dict_e[i][j][1],1)
                        for k in jiangli:
                            listjl.append(k)
                        listall.append(listjl)
                dict_e[i]=listall
            elif dict_e[i][0][0] == '女神对对碰':
                dict_e[i] = listall
            elif dict_e[i][0][0] == '开工福利':
                jiangli=jiangli_jx(dict_e[i][9][2],0)
                listall.append(jiangli)
                lista=[]
                if dict_e[i][9][1].split(',')[0].split('{')[1]=='role_level':
                    lista.append('等级')
                    lista.append(dict_e[i][9][1].split(',')[1].split('}')[0])
                listall.append(lista)
                dict_e[i] = listall
            elif dict_e[i][0][0]=='副本挑战' or dict_e[i][0][0]=='守护雅典娜':
                for j in range(len(dict_e[i])):
                    if j>=9:
                        listjl=[]
                        if dict_e[i][j][1].split(',')[0].split('{')[1]=='total_fb_pass1':
                            mubiao='普通副本*'+dict_e[i][j][1].split(',')[1].split('}')[0]
                            listjl.append(mubiao)
                        elif dict_e[i][j][1].split(',')[0].split('{')[1]=='total_fb_pass2':
                            mubiao='精英副本*'+dict_e[i][j][1].split(',')[1].split('}')[0]
                            listjl.append(mubiao)
                        elif dict_e[i][j][1].split(',')[0].split('{')[1]=='guard_section':
                            mubiao='守护雅典娜通关'+dict_e[i][j][1].split(',')[1].split('}')[0]+'波'
                            listjl.append(mubiao)
                        jiangli=jiangli_jx(dict_e[i][j][2],0)
                        for k in jiangli:
                            listjl.append(k)
                        listjl.append(dict_e[i][j][3])
                        listall.append(listjl)
                dict_e[i] = listall
            elif dict_e[i][0][0] == '体力消耗':
                for j in range(len(dict_e[i])):
                    if j >= 9:
                        listjl = []
                        mubiao = '消耗体力' + dict_e[i][j][1].split(',')[1].split('}')[0]+'点'
                        listjl.append(mubiao)
                        jiangli = jiangli_jx(dict_e[i][j][2], 0)
                        for k in jiangli:
                            listjl.append(k)
                        listjl.append(dict_e[i][j][3])
                        listall.append(listjl)
                dict_e[i] = listall
            elif dict_e[i][0][0] == '砸金蛋':
                jiangli = jiangli_jx(dict_e[i][9][0], 1)
                listjl = '砸蛋消耗'+jiangli[1]+'个'+jiangli[0]+"+"+jiangli[3]+jiangli[2]
                listjla=[listjl]
                listjlb=[]
                listjlc=[]
                listjld=[]
                listjlb.append(dict_e[i][20][0])
                listjlb.append('青铜')
                listjlb.append(dict_e[i][12][1])
                listjlb.append(dict_e[i][12][2])
                listjlc.append(dict_e[i][21][0])
                listjlc.append('白银')
                listjlc.append(dict_e[i][13][1])
                listjlc.append(dict_e[i][13][2])
                listjld.append(dict_e[i][22][0])
                listjld.append('黄金')
                listjld.append(dict_e[i][14][1])
                listjld.append(dict_e[i][14][2])
                listall.append(listjla)
                listall.append(listjlb)
                listall.append(listjlc)
                listall.append(listjld)
                dict_e[i]=listall
            elif dict_e[i][0][0] == '扭蛋币':
                for j in range(len(dict_e[i])):
                    activ_a = dict_e[i][j]
                    if j >= 9:
                        listj = []
                        listj.append(activ_a[0])
                        lista = jiangli_jx(activ_a[2], 0)
                        for k in lista:
                            listj.append(k)
                        listj.append(activ_a[3])
                        listall.append(listj)
                dict_e[i] = listall
                # for b in dict_e[i]:
                #     print(b)
        #超级金币翻牌
        elif dict_e[i][0][0] in fanpan:
            listall = []
            actid = dict_e[i][2][0]
            actname = dict_e[i][0][0]
            acttime = dict_e[i][5][2]
            acttimec = dict_e[i][5][3]
            listt = [actid, '超级金币翻牌', acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
            listall.append(listt)
            #print(lista1)
            cost=jiangli_jx(dict_e[i][9][3],1)
            cost.append(dict_e[i][9][5])
            cost.append(dict_e[i][9][1])
            cost.append(dict_e[i][9][2])
            listall.append(cost)
            for j in range(len(dict_e[i])):
                if j>18 and j<29:
                    reword=jiangli_jx(dict_e[i][j][1],1)
                    listall.append(reword)
                elif j>30:
                    reword=jiangli_jx(dict_e[i][j][1],1)
                    jiangli=dict_e[i][j][0]+'积分'
                    reword.insert(0,jiangli)
                    listall.append(reword)
            dict_e[i]=listall
            # for i in dict_e[i]:
            #     print(i)
        #幸运转盘
        elif dict_e[i][0][0] in zhuanpan:
            listall = []
            actid = dict_e[i][2][0]
            actname = dict_e[i][0][0]
            acttime = dict_e[i][5][2]
            acttimec = dict_e[i][5][3]
            listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
            listall.append(listt)
            # print(listall)
            listxh=jiangli_jx(dict_e[i][9][3],1)
            listxh.insert(0,'消耗')
            listall.append(listxh)
            k=0
            listdy=['X次后', '奖池内容']
            for j in range(len(dict_e[i])):
                if dict_e[i][j]==listdy:
                    k=j
            for j in range(len(dict_e[i])):
                if j>14 and j<k:
                    listbc=[]
                    listbc.append(dict_e[i][j][0]+'次')
                    strjl=dict_e[i][j][1].split('prop,{')[1].split('}}')[0]
                    strjln=d_item[strjl.split(',')[0]]
                    strjlc=strjl.split(',')[1]
                    listbc.append(strjln)
                    listbc.append(strjlc)
                    listall.append(listbc)
                elif j>k+1 and j<k+4:
                    listg=dict_e[i][j][1].split('}]},')
                    listz=[]
                    for l in range(len(listg)):
                        listg1=listg[l].replace('[','').replace(']', '').replace('{', '').replace('}', '').split(',')
                        if l==0:
                            listg1=listg1[1:]
                        if listg1[2]=='prop':
                            listz.append(listg1[0])
                            listz.append(d_item[listg1[3]])
                            listz.append(listg1[4])
                        elif listg1[2]=='rmb':
                            listz.append(listg1[0])
                            listz.append(d_item[listg1[2]])
                            listz.append(listg1[3])
                    listall.append(listz)
            listgl=dict_e[i][k+11][0].replace('[','').replace(']','').replace('}','').split(',')
            listgln=[]
            listgln.append(d_item[listgl[1]])
            listgln.append(d_item[listgl[2]])
            listgln.append(d_item[listgl[3]])
            listall.append(listgln)
            listxx=str(dict_e[i][-1][0]).split('[')[1].split(']')[0].split(',')
            listall.append(listxx)
            dict_e[i]=listall
            # for i in dict_e[i]:
            #     print(i)
        #体力双倍
        elif dict_e[i][0][0] in tili:
            listall = []
            actid = dict_e[i][2][0]
            actname = dict_e[i][0][0]
            acttime = dict_e[i][5][2]
            acttimec = dict_e[i][5][3]
            listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
            listall.append(listt)
            if dict_e[i][7][0]=='类型':
                listn=[]
                listn=dict_e[i][9]
                listall.append(listn)
            else:
                listm=[]
                listm=dict_e[i][8][2]
                listall.append(listm)
            dict_e[i]=listall
            # for i in dict_e[i]:
            #     print(i)
        #圣器双倍
        elif dict_e[i][0][0] in shengqi:
            listall = []
            actid = dict_e[i][2][0]
            actname = dict_e[i][0][0]
            acttime = dict_e[i][5][2]
            acttimec = dict_e[i][5][3]
            listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
            listall.append(listt)
            if dict_e[i][7][0]=='图标':
                gonggao=[dict_e[i][8][2]]
                listall.append(gonggao)
            else:
                diaoluo1=[dict_e[i][9][0],dict_e[i][9][1]]
                diaoluo2 = [dict_e[i][10][0], dict_e[i][10][1]]
                listall.append(diaoluo1)
                listall.append(diaoluo2)
            dict_e[i] = listall
        #圣衣双倍
        elif dict_e[i][0][0] in shengyi:
            listall = []
            actid = dict_e[i][2][0]
            actname = dict_e[i][0][0]
            acttime = dict_e[i][5][2]
            acttimec = dict_e[i][5][3]
            listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
            listall.append(listt)
            if dict_e[i][7][0] == '图标':
                gonggao = [dict_e[i][8][2]]
                listall.append(gonggao)
            else:
                diaoluo1 = [dict_e[i][9][0], dict_e[i][9][1]]
                listall.append(diaoluo1)
            dict_e[i] = listall
            for j in dict_e[i]:
                print(j)
        #消消乐
        elif dict_e[i][0][0]=='斗士消消乐':
            listall = []
            actid = dict_e[i][2][0]
            actidz = dict_e[i][2][0]
            actname = '消消乐'
            acttime = dict_e[i][5][2]
            acttimec = dict_e[i][5][3]
            listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
            listall.append(listt)
            listn = []
            for j in range(len(dict_e[i])):
                if j >= 15 and j < 20:
                    listxs = []
                    lista = jiangli_jx(dict_e[i][j][2], 0)
                    if dict_e[i][j][0] == dict_e[i][j][1]:
                        listxs.append(dict_e[i][j][1])
                    else:
                        listxs.append((dict_e[i][j][0] + '至' + dict_e[i][j][1] ))
                    for k in lista:
                        listxs.append(k)
                    listall.append(listxs)
            dict_e[i] = listall
            # for i in dict_e[i]:
            #     print(i)
        #团购
        elif dict_e[i][0][0] in tuangou:
            listall = []
            actid = dict_e[i][2][0]
            actidz = dict_e[i][2][0]
            actname = dict_e[i][0][0]
            acttime = dict_e[i][5][2]
            acttimec = dict_e[i][5][3]
            listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
            listall.append(listt)
            listn = []
            listn.append(dict_e[i][9][0])
            listn.append(dict_e[i][9][1])
            listall.append(listn)
            jiangli=jiangli_jx(dict_e[i][9][2],0)
            for j in jiangli:
                listn.append(j)
            for k in range(len(dict_e[i])):
                listm=[]
                if k>11:
                    listm=dict_e[i][k]
                    listall.append(listm)
            dict_e[i]=listall
        #活跃有礼
        elif dict_e[i][0][0] in huoyue:
            listall = []
            actid = dict_e[i][2][0]
            actidz = dict_e[i][2][0]
            actname = dict_e[i][0][0]
            acttime = dict_e[i][5][2]
            acttimec = dict_e[i][5][3]
            listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
            listall.append(listt)
            dicth={}
            dicth['draw_rmb']=['钻石抽奖','次','LotteryShow+2']
            dicth['boss_times']=['BOSS挑战','次','BossFightViewShow']
            dicth['arena_integral'] = ['竞技场获得','分', 'ArenaViewShow']
            dicth['alchemys'] = ['点金', '次', 'GoldPointingShow']
            dicth['draw_special'] = ['特殊召唤', '次','HeroBgShow+3']
            dicth['draw_money'] = ['金币抽奖次数', '次', 'HeroBgShow+3']
            dicth['arena_win'] = ['竞技场胜利', '次', 'HeroBgShow+3']
            dicth['consume_arena_times'] = ['参与竞技场', '次', 'HeroBgShow+3']
            dicth['nebula_consume'] = ['星力消耗', '', 'HeroBgShow+3']
            for j in range(len(dict_e[i])):
                activ_a = dict_e[i][j]
                if j >= 9:
                    listxs = []
                    listjl = jiangli_jx(activ_a[2], 0)
                    for l in listjl:
                        listxs.append(l)
                    tiaomu=dicth[activ_a[1].split(',')[0].split('{')[1]][0]+activ_a[1].split(',')[1].split('}')[0]+dicth[activ_a[1].split(',')[0].split('{')[1]][1]
                    listxs.insert(0,tiaomu)
                    listxs.append(dicth[activ_a[1].split(',')[0].split('{')[1]][2])
                    listall.append(listxs)
            dict_e[i] = listall
            # for i in dict_e[i]:
            #     print(i)
        elif dict_e[i][0][0] == '欢乐射击':
            listall = []
            actid = dict_e[i][2][0]
            actidz = dict_e[i][2][0]
            actname = dict_e[i][0][0]
            acttime = dict_e[i][5][2]
            acttimec = dict_e[i][5][3]
            listt = [actid, actname, acttime, acttimec]  # ['1588058523', '充值有礼', '2020-5-18 0:0:0', '604799']
            listall.append(listt)
            dict_e[i] = listall
        # print(i)
        # for k in dict_e[i]:
        #     print(k)
        dict_finall[dict_e[i][0][0]]=dict_e[i]
    return dict_finall

def server(d):
    d=d_server
    return d

d_card=dict_card('')
d_item=dict_item('')
activ_h=get_activ('http://120.92.9.137:872','/sgame_gm/gm_active_port/get_activeshow')
dict_a=j_activ(activ_h)
d_server=jx_huodong(dict_a)

# for i in d_server.keys():
#     print(i)
#     for j in d_server[i]:
#         print(j)











