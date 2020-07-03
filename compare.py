import time
import pandas
import xlrd
from xlrd import xldate_as_tuple
import string
from excelactive import excel
from server import server
# d_card=dict_card('')
# d_item=dict_item('')
# activ_h=get_activ('http://120.92.9.137:872','/sgame_gm/gm_active_port/get_activeshow')
# dict_a=j_activ(activ_h)
d_server=server('') #获取服务器的活动信息
# timeb=get_Amessage(dictActiv)
# timec=chuli_teshu(timeb)
d_excel=excel('')#获取本地的活动表
# for i in d_server['1589531518']:
#     print(i)
# for i in d_excel['1589531518']:
#     print(i)
print('开始对比')
for i in d_server.keys():
    if i in d_excel.keys() and (d_server[i][0][2]=='2020-7-5 0:0:0' or d_server[i][0][2]=='2020-7-5 5:0:0') :
        print(i)
        print(d_server[i][0])
        if d_server[i]==d_excel[i]:
            print('完全相同')
        else:
            try:
                if len(d_server[i])<len(d_excel[i]):
                    print('活动表比服务器的长')
                    print(d_server[i]+['服务器'])
                    print(d_excel[i]+['活动表'])
                    # print('不同内容：'+str((set(d_server[i][j])^set(d_excel[i][j]))))
                for j in range(len(d_server[i])):
                    if d_server[i][j]!=d_excel[i][j]:
                        print(d_server[i][j]+['服务器'])
                        print(d_excel[i][j]+['活动表'])
                        if set(d_server[i][j])^set(d_excel[i][j])==set():
                            print('内容一致，排序不同')
                        else:
                            print('不同内容：'+str((set(d_server[i][j])^set(d_excel[i][j]))))
                        print('-----------------------------------------------')
            except:
                print('服务器比客户端的长')
                print(d_server[i]+['服务器']) 
                print(d_excel[i]+['活动表'])
                # print('不同内容：' + str((set(d_server[i][j]) ^ set(d_excel[i][j]))))
        print('')
    elif i not in d_excel.keys():
        print( d_server[i][0])
        print(['没有这个活动'])
        print('')

    # elif i in d_excel.keys() and (d_server[i][0][2].split(' ')[1]!='0:0:0' or d_server[i][0][2].split(' ')[1]!='5:0:0'):
    #     print(d_server[i][0])
    #     print(['活动开启时间不是0点和5点'])
    #     print('')

