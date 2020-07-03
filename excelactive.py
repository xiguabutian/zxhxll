import time
import pandas
import xlrd
from xlrd import xldate_as_tuple
import string
#读取活动表格数据
def excel_j(dizhi): #活动表格在本地的路径 'C:/Users/Administrator/Desktop/活动测试.xlsx'
    data=xlrd.open_workbook(dizhi)
    data.sheet_names()  #获取表格分页名称
    table=data.sheet_by_name('Sheet1') #活动页内容读取 Sheet1
    d=0
    dict_e={}
    l_activ=[]
    l_activ2=[]
    for nr in range(table.nrows): #活动内容解析
        rowAll=table.row_values(nr)
        for a in range(len(rowAll)):
            b=str(type((rowAll[a])))
            if  b=="<class 'float'>": #解析数字会自动变成浮点类型数据，把浮点转为str并去掉末尾的（.0）
                rowAll[a]=str(rowAll[a]).split('.0')[0]
        for c in rowAll:
            if c !='': #去掉空行，全部为空的行不会加到列表里
                l_activ.append(rowAll)
                #print(rowAll)
                break
    l_activ.append(['活动名称'])
    #print(l_activ)
    #print(len(l_activ))
    for e in range(len(l_activ)): #把读取的列表按照每个活动放入字典里
        #print(l_activ[e])
        if l_activ[e][0] !='活动名称':
            l_activ2.append(l_activ[e])
        else:
            dict_e[d]=l_activ2
            d += 1
            l_activ2=[]
    dict_e.pop(0)
    return dict_e
# for i in dictActiv.keys():
#     print(i)
#     print(dictActiv[i])

# 根据活动表格的格式获取活动时间、名字、日期，传入具体的活动
def get_Amessage(dict_A):
    activ_d = {}
    s = 0
    for keyA in dict_A.keys():
        #print(dict_A[keyA])
        list_a=dict_A[keyA]
        list_time = []
        list_name=[]
        list_id = []
        list_neirong=[]
        try: #读取活动时间
            time1=list_a[0][1]
        except:
            # print(list_a)
            print("没有找到时间")
        try:# 读取活动名字
            list_name.append(list_a[0][0])
        except:
            # print(list_a)
            list_name.append('没得名字')
            print('没有活动名字')
        try: #读取活动ID
            teshu1=['特殊召唤']
            teshu2=['体力双倍','圣器双倍','圣衣双倍']
            teshu3=['团购']
            if list_a[0][0] in teshu1:
                activ_id = list_a[2][0]
                activ_id1=list_a[3][0]
                list_id.append(activ_id)
                list_id.append(activ_id1)
                neirong1=[['vip', '2']]
                list_neirong.append(list_a)
                list_neirong.append(neirong1)
            elif list_a[0][0] in teshu2:
                # for b in list_a:
                #     print(b)
                activ_id = list_a[1][0]
                activ_id1=list_a[2][0]
                list_id.append(activ_id)
                list_id.append(activ_id1)
                neirong1=[]
                neirong2=[]
                if list_a[0][0]=='体力双倍':
                    neirong1=[['pve', '2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,']]
                    neirong2=[['[a2642e]活动时间：开始时间 [d02e2e]05:00[-]-结束时间 [d02e2e]05:00[-]\\n活动内容：活动期间购买体力可享受双倍体力值\\n活动范围：开服七日以上服务器[-]']]
                elif list_a[0][0]=='圣器双倍':
                    neirong1=[['elite', '[1,2]'],['normal', '[1,2]']]
                    neirong2=[['[a2642e]活动时间：开始时间 5:00-结束时间 5:00\\n活动内容：活动期间通关主线普通及精英副本圣器掉落数量翻倍\\n活动范围：开服七日以上服务器\\n注：活动期间所有普通及精英副本圣器数量双倍掉落，掉落概率及其它道具的掉落倍率不变[-]']]
                elif list_a[0][0]=='圣衣双倍':
                    neirong1=[['cloth', '[1,2,3,4,5]']]
                    neirong2=[['[a2642e]活动时间：开始时间 5:00-结束时间 5:00\\n活动内容：活动期间，斗士们通关圣衣试炼可以获得双倍的圣衣材料掉落！\\n注意事项：\\n1.请尽量避免在紧邻在活动开始及结束的前后5至10分钟通关圣衣试炼，以免由于数据未同步导致无法获得双倍材料。\\n2.本次双倍为掉落材料双倍，各阶材料的掉落概率不会发生变化。[-]']]
                list_neirong.append(neirong1)
                list_neirong.append(neirong2)
            elif list_a[0][0] in teshu3:
                tuangou1=[]
                tuangou2=[]
                tuangou3=[]
                for t in list_a:
                    if t[0] !='' and t[0] !='团购':
                        list_id.append(t[0])
                listfen = []
                for k in range(len(list_a)):
                    if list_a[k][5]!='' and k>4:
                        listfen.append(k)
                for k in range(len(list_a)):
                    if k<listfen[0]:
                        tuangou1.append(list_a[k])
                    elif k>=listfen[0] and k<listfen[1]:
                        tuangou2.append(list_a[k])
                    elif k>=listfen[1]:
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
                s_time=time1.split('-')[0].replace('/','-')+' 0:0:0' #开始时间，默认0点
                e_time=time1.split('-')[1].replace('/','-')+' 0:0:0' #结束时间，默认0点
                timeArray_s = time.strptime(s_time, '%Y-%m-%d %H:%M:%S')
                timeStamp_s = int(time.mktime(timeArray_s))
                timeArray_e = time.strptime(e_time, '%Y-%m-%d %H:%M:%S')
                timeStamp_e = int(time.mktime(timeArray_e))
                c_time = timeStamp_e - timeStamp_s +86399  # 持续时间，默认比时间时间少1秒
                list_time.append(s_time)
                list_time.append(str(c_time))
                list_time.append(e_time)
            else:
                s_time= xldate_as_tuple(int(time1), 0)
                sds=str(s_time[0])+'-'+str(s_time[1])+'-'+str(s_time[2])+' 0:0:0'
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
            list_title=[]
            if list_name[0]=='体力双倍' or list_name[0]=='圣器双倍' or list_name[0]=='圣衣双倍' or list_name[0]=='特殊召唤':
                if list_name[0]=='特殊召唤':
                    list_tim=list_time[0]
                else:
                    list_tim = list_time[0].split(' ')[0]+ ' 5:0:0'
                list_title.append(list_id[a])
                list_title.append(list_name[0])
                if a==0:
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
                s+=1
                activ_d[s] = activ_q
            else:
                activ_d[list_id[a]]=activ_q
        # for a in list_a:
        #     a=[i for i in a if i !=''] #去掉空行
        #     activ_q.append(a)
        # activ_q.insert(0,list_time)
        # if activ_id=='':
        #     s+=1
        #     activ_d[s] = activ_q
        # else:
        #     activ_d[activ_id]=activ_q
    return activ_d


#根据特定的格式解析表格里的数据方便与服务器数据进行对比
def chuli_activ(timea):
    for keyB in list(timea.keys()):
        chongzhi=['充值有礼']
        leijicz=['累计充值','消费返利','扭蛋币']
        jiuji=['跨服抢购']
        duihuan=['点金返利','守护兑换','金币兑换','原力兑换','限时特殊召唤','重生石兑换','材料兑换','角色魂石兑换','觉醒石兑换','神器觉醒','神钢兑换','水晶兑换','水果拉霸','超级幸运星','究极之力兑换','究极之力兑换1','究极之力兑换2','角色魂石兑换1','角色魂石兑换2','觉醒石兑换1','觉醒石兑换2']
        duobao=['一元夺宝']
        zhaohuan=['特殊召唤']
        guigui=['贵鬼奖励','贵鬼游戏']
        hunxia=['魂匣']
        xiaohuodong=['潘多拉魔盒','超级金币翻牌','女神问答','旋转派对','消消乐','开工福利','活跃有礼','副本挑战','守护雅典娜','体力消耗','射箭','砸金蛋','扭蛋币']
        zhuanpan=['幸运转盘']
        tili=['体力双倍','圣衣双倍','圣器双倍']
        tuangou=['团购']
        # 充值有礼活动
        if timea[keyB][0][1] in chongzhi:
            timea[keyB][-1].insert(0,'100天') #最终奖励配置，不用管
            timea[keyB][-1].insert(0,'60') #连续充值多少天可以领取60/10=6天
            del timea[keyB][1][0:2]
            if  timea[keyB][0][0] !='':
                del timea[keyB][2][0]
        # 累计充值 消费返利 重生石兑换 扭蛋币
        elif timea[keyB][0][1] in leijicz:
            del timea[keyB][1][0:2]
            if timea[keyB][0][0] !='':
                del timea[keyB][2][0]
            if timea[keyB][0][1]=='消费返利':
                for i in range(len(timea[keyB])):
                    if i > 0:
                        timea[keyB][i].append('LotteryShow+2')  # 跳转
            elif timea[keyB][0][1]=='扭蛋币':
                for i in range(len(timea[keyB])):
                    if i > 0:
                        timea[keyB][i].append('ReChargeShow')  # 跳转
            # for i in timea[keyB]:
            #     print(i)
        # 跨服究极之力抽卡
        elif timea[keyB][0][1] in jiuji:
            listt=[]
            del timea[keyB][1:3]
            del timea[keyB][2][0]
            kuid=timea[keyB][4][0].split('：')[1]
            jifen='10'#每抽获得积分，默认10
            kuafu='1' #是否跨服，1为跨服，0为不跨服
            rangk=timea[keyB][(len(timea[keyB])-1)][1].split('上榜积分')[1]
            rangkn=timea[keyB][(len(timea[keyB])-1)][2].split('排行榜人数')[1]
            del timea[keyB][(len(timea[keyB])-1)]
            listt.append(kuid)
            listt.append(jifen)
            listt.append(rangk)
            listt.append(rangkn)
            listt.append(kuafu)
            del timea[keyB][4][0]
            del timea[keyB][6][0]
            timea[keyB].insert(1, listt)
            for i in range(len(timea[keyB])):
                if '到' in timea[keyB][i][0]:
                    rankings=timea[keyB][i][0].split('到')[0]
                    timea[keyB][i][0]=timea[keyB][i][0].split('到')[1]
                    timea[keyB][i].insert(0,rankings)
                elif i>1:
                    rankings=timea[keyB][i][0]
                    timea[keyB][i].insert(0, rankings)
        # '点金返利','金币兑换','原力兑换','限时特殊召唤','重生石兑换'，材料兑换,'角色魂石兑换','觉醒石兑换','神器觉醒',神钢兑换 水晶兑换 水果拉霸
        elif timea[keyB][0][1] in duihuan:
            duihuan1=['材料兑换','角色魂石兑换','神器觉醒','守护兑换','究极之力兑换1','究极之力兑换2','角色魂石兑换1','角色魂石兑换2','究极之力兑换']
            duihuan2=['重生石兑换','神钢兑换','水晶兑换']
            duihuan3=['超级幸运星']
            duihuan4=['觉醒石兑换','觉醒石兑换1','觉醒石兑换2']
            del timea[keyB][1][0:2]
            if timea[keyB][0][0] !='':
                del timea[keyB][2][0]
            if timea[keyB][0][1]=='点金返利':
                for i in range(len(timea[keyB])):
                    if i>0:
                        del timea[keyB][i][0]
                        timea[keyB][i].append('GoldPointingShow') #跳转
            elif timea[keyB][0][1]=='金币兑换':
                for i in range(len(timea[keyB])):
                    if i>0:
                        timea[keyB][i].append('GoldPointingShow') #跳转
                        timea[keyB][i].insert(0,'次数')
            elif timea[keyB][0][1]=='原力兑换':
                for i in range(len(timea[keyB])):
                    if i>0:
                        timea[keyB][i].insert(0, '次数')
            elif timea[keyB][0][1] == '限时特殊召唤':
                del timea[keyB][5][0]
                del timea[keyB][6][0]
            elif timea[keyB][0][1] in duihuan2:
                for i in range(len(timea[keyB])):
                    if i > 0:
                        timea[keyB][i].append('ReChargeShow')  # 跳转
                        timea[keyB][i].insert(0, '次数')
                    # for i in timea[keyB]:
                    #     print(i)
            elif timea[keyB][0][1] in duihuan1:
                for i in range(len(timea[keyB])):
                    if i > 0:
                        timea[keyB][i].insert(0, '次数')
            elif timea[keyB][0][1] in duihuan4:
                for i in range(len(timea[keyB])):
                    if i > 0:
                        timea[keyB][i].insert(0, '次数')
                        if '石' in timea[keyB][i][4]:
                            timea[keyB][i][4]=timea[keyB][i][4].replace('石','')
            elif timea[keyB][0][1] in duihuan3:
                for i in range(len(timea[keyB])):
                    if i > 0:
                        timea[keyB][i].append('ReChargeShow')  # 跳转
                # for i in timea[keyB]:
                #     print(i)
        # 夺宝奇兵
        elif timea[keyB][0][1] in duobao:
            del timea[keyB][1][0:2]
            if timea[keyB][0][0] !='':
                del timea[keyB][2][0:3]
            try:
                times=timea[keyB][2][1].split('最多可买')[1].split('次')[0]
            except:
                times='默认10'
            del timea[keyB][2][2]
            del timea[keyB][3][0:3]
            del timea[keyB][4][0:3]
            timea[keyB][1].insert(0,times)
            timea[keyB][2].insert(0, times)
            timea[keyB][0].append('561600') #竞猜时间
            timea[keyB][0].append('43199')  #领奖时间
        # 特殊召唤
        elif timea[keyB][0][2] in zhaohuan:
            del timea[keyB][1][0:2]
            keyZ=timea[keyB][0][1]
            listZ=[]
            listZ.append(keyZ)
            listZ.append(timea[keyB][2][0])
            listZ.append(timea[keyB][0][3])
            listZ.append(timea[keyB][0][4])
            if timea[keyB][0][0] !='':
                del timea[keyB][2][0]
            del timea[keyB][0][1]
            del timea[keyB][4][0]
            del timea[keyB][3][0]
            for i in range(len(timea[keyB])):
                if i > 0:
                    timea[keyB][i].append('LotteryShow+3')  # 跳转
            timea[keyB].append(listZ)
        # 贵鬼
        elif timea[keyB][0][1] in guigui:
            if timea[keyB][0][1] == '贵鬼游戏':
                del timea[keyB][1][0:3]
                del timea[keyB][2][0:2]
                del timea[keyB][3][0]
                del timea[keyB][4][0:2]
                listg=[]
                listga=[]
                listgb = []
                listga.append('贵鬼证明')
                listga.append('1')
                listg.append(timea[keyB][5][0])
                listg.append('1')
                listgb.append(timea[keyB][5][0])
                listgb.append('1')
                listgb.append('1分')
                listg.append('晶莹水晶3阶碎片')
                listg.append('1')
                listg.append('2分')
                del timea[keyB][5][0]
                del timea[keyB][6][0]
                del timea[keyB][7][0]
                del timea[keyB][8][0]
                del timea[keyB][9][0]
                timea[keyB].append(listga)
                timea[keyB].append(listgb)
                timea[keyB].append(listg)
            elif timea[keyB][0][1] == '贵鬼奖励':
                del timea[keyB][1][0:2]
                if timea[keyB][0][0] != '':
                    del timea[keyB][2][0]
                for i in range(len(timea[keyB])):
                    if i>0:
                        timea[keyB][i].append('ReChargeShow')
        #魂匣
        elif timea[keyB][0][1] in hunxia or timea[keyB][0][1][0:2]=='魂匣' or timea[keyB][0][1][0:2]=='神圣':
            if timea[keyB][1][2][-1]==' ':
                timea[keyB][1][2]=timea[keyB][1][2][:-1]
            kuid = timea[keyB][1][2][-6:]
            if kuid[0]!='1':
                kuid=kuid[1:]
            heroid1=timea[keyB][1][4]
            heroid2=timea[keyB][1][6]
            heroid3=timea[keyB][1][8]
            listhx=[kuid,heroid1,heroid2,heroid3]
            timea[keyB][1]=listhx
            del timea[keyB][2]
        #小活动 潘多拉魔盒 超级金币翻牌 女神问答 旋转派对 斗士消消乐 活跃有礼 副本挑战 守护雅典娜 体力消耗 扭蛋
        elif timea[keyB][0][1] in xiaohuodong:
            del timea[keyB][1][0:2]
            if timea[keyB][0][0] != '':
                del timea[keyB][2][0]
            if timea[keyB][0][1]=='潘多拉魔盒':
                del timea[keyB][1][2]
                listc=['0', '10', '30', '50', '70', '90', '120', '150', '180'] #每次消耗的钻石
                for i in listc:
                    timea[keyB][1].append(i)
                del timea[keyB][2:]
            elif timea[keyB][0][1] == '超级金币翻牌':
                listm=[]
                listm.append('钻石')
                listm.append(timea[keyB][3][0])
                times=timea[keyB][4][0].split('购买')[1].split('次')[0]
                listm.append(times)
                listm.append('3')#必出幸运卡片轮数
                listm.append('3')#每轮几张
                timea[keyB][1]=listm
                del timea[keyB][2]
                del timea[keyB][2][0]
                del timea[keyB][3][0]
                for i in range(len(timea[keyB])):
                    if i>1 and i<12:
                        timea[keyB][i]=timea[keyB][i][0:1]
                        timea[keyB][i].insert(0,'游戏币')
                del timea[keyB][12:14]
            elif timea[keyB][0][1] == '旋转派对': #奖励没得
                lista=[]
                lista=timea[keyB][0]
                lista[1]='女神对对碰'
                listb=[]
                listb.append(lista)
                timea[keyB]=listb
            elif timea[keyB][0][1] == '消消乐': #积分奖励GM上没有，删除掉
                del timea[keyB][1:12]
            elif timea[keyB][0][1] == '开工福利':
                timea[keyB][2].append('等级')
                timea[keyB][2].append('1')
            elif timea[keyB][0][1] == '副本挑战':
                for i in range(len(timea[keyB])):
                    if timea[keyB][i][0][0:2]=='普通':
                        timea[keyB][i].append('LevelShow+PT')
                    elif timea[keyB][i][0][0:2]=='精英':
                        timea[keyB][i].append('LevelShow+JY')
            elif timea[keyB][0][1] == '守护雅典娜':
                for i in range(len(timea[keyB])):
                    if timea[keyB][i][0][0:2]=='守护':
                        timea[keyB][i].append('GuardAthenaIn')
            elif timea[keyB][0][1] == '体力消耗':
                for i in range(len(timea[keyB])):
                    if timea[keyB][i][0][0:2]=='消耗':
                        timea[keyB][i].append('LevelShow')
            elif timea[keyB][0][1] == '射箭':
                del timea[keyB][2]
            elif timea[keyB][0][1] == '砸金蛋':
                timea[keyB][1]=[timea[keyB][1][0]]
                del timea[keyB][2][-1]
                del timea[keyB][3][-1]
                del timea[keyB][4][-1]

            elif timea[keyB][0][1] == '活跃有礼':
                dicth={}
                dicth['钻石召唤5次']='LotteryShow+2'
                dicth['BOSS挑战3次'] = 'BossFightViewShow'
                dicth['竞技场获得30分'] = 'ArenaViewShow'
                dicth['点金5次'] = 'GoldPointingShow'
                dicth['星力消耗18000'] = 'HeroBgShow+3'
                dicth['特殊召唤5次'] = 'HeroBgShow+3'
                dicth['金币抽奖次数20次'] = 'HeroBgShow+3'
                dicth['竞技场胜利3次'] = 'HeroBgShow+3'
                dicth['参与竞技场11次'] = 'HeroBgShow+3'
                dicth['钻石抽奖3次'] = 'LotteryShow+2'
                for i in range(len(timea[keyB])):
                    if i>0:
                        timea[keyB][i].append(dicth[timea[keyB][i][0]])
            # for i in timea[keyB]:
            #     print(i)
        #幸运转盘
        elif timea[keyB][0][1] in zhuanpan:
            listbll=[]
            listtitle=timea[keyB][0]
            baodi=timea[keyB][2][1].split('每')[1].split('次一次')[0] #多少次保底
            times=timea[keyB][2][1].split('一共保')[1].split('次')[0] #一共保底几次
            putong=timea[keyB][1][2] #普通道具名称
            teshu=timea[keyB][2][2] #特殊道具名称
            listta=['消耗', '转盘抽奖券', '1']
            listtb=['500', '废墟遗石', '3', '2000', '钻石', '170', '2800', '普通', '15', '1800', '普通', '15', '2800', '普通', '20', '1000', '废墟遗石', '2', '1800', '普通', '20', '1200', '普通', '25', '1000', '废墟遗石', '2', '1200', '普通', '25']
            listtc=['100', '特殊', '1', '500', '废墟遗石', '3', '2000', '钻石', '170', '2800', '普通', '15', '100', '钻石', '3000', '1800', '普通', '15', '2800', '普通', '20', '1000', '废墟遗石', '2', '1800', '普通', '20', '1200', '普通', '25', '1000', '废墟遗石', '2', '1200', '普通', '25']
            listtd=[putong if i=='普通'else i for i in listtb]
            listte=[putong if i=='普通'else i for i in listtc]
            listte = [teshu if i == '特殊' else i for i in listte]
            listbll.append(listtitle)
            listbll.append(listta)
            for i in range(int(times)):
                listbd=[]
                times_a=(i+1)*int(baodi)
                listbd.append(str(times_a)+'次')
                listbd.append(teshu)
                listbd.append('1')
                listbll.append(listbd)
            listbll.append(listtd)
            listbll.append(listte)
            listbe=[putong,listtb[1],teshu]
            listbll.append(listbe)
            listbf=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'] #高亮的设置
            listbff=[]
            listbff.append(listbf)
            listbll.append(listbf)
            timea[keyB]=listbll
            # for i in timea[keyB]:
            #     print(i)
        #体力双倍
        elif timea[keyB][0][1] in tili:
            if len(timea[keyB][1])==1:
                strtime=timea[keyB][0][2].split(' ')[0].split('-')[1]+'月'+timea[keyB][0][2].split(' ')[0].split('-')[2]+'日'
                endtime = timea[keyB][0][4].split(' ')[0].split('-')[1] + '月' + \
                          timea[keyB][0][4].split(' ')[0].split('-')[2] + '日'
                timea[keyB][1]=[timea[keyB][1][0].replace('开始时间',strtime).replace('结束时间',endtime)]
            # for i in timea[keyB]:
            #     print(i)
        #团购
        elif timea[keyB][0][1] in tuangou:
            if keyB==timea[keyB][2][0]:
                # for i in timea[keyB]:
                #     print(i)
                del timea[keyB][1][0:2]
                del timea[keyB][1][2]
                del timea[keyB][2][0]
                del timea[keyB][3][0]
                del timea[keyB][4][0]
                for k in range(len(timea[keyB])):
                    if k>1:
                        timea[keyB][k]=[timea[keyB][k][2],(timea[keyB][k][1].split('.')[1]+'00')]
            else:
                del timea[keyB][1][2]
                for k in range(len(timea[keyB])):
                    if k>1:
                        timea[keyB][k]=[timea[keyB][k][2],(timea[keyB][k][1].split('.')[1]+'00')]

    return timea

def excel(e):
    e=d_excel
    return e

dictActiv=excel_j('C:/Users/Administrator/Desktop/活动测试(11).xlsx')
timeb=get_Amessage(dictActiv)
# timec=chuli_teshu(timeb)
# for i in timec.keys():
#     print(i)
d_excel=chuli_activ(timeb)

# for i in d_excel.keys():
#     print(i)
#     for j in d_excel[i]:
#         print(j)











