# -*- coding: utf-8 -*-
__author__ = 'pengbingxiang'

#*************************自动化定制Appstore的IPA包********************************

#--------打包信息---------
# 需要打包的项目信息
workspace_name = '/WeRentCar.xcodeproj'

# 打包的Plist文件名
plist_name = 'AppStoreExportOptionsPlist.plist'

############定制版信息################

project_arr = []

#  WeRentCar_appstore_yiweixiang 1
project_arr.append({'scheme_name':'appstore_yiweixiang', 'provisioning_profile':'wuhandiandongfabu', 'code_sign_identity':'iPhone Distribution: wenxi bao (9TP2R8S57G)', 'project_bundle_identifier':'com.wuhandiandong.WeRentCar'})

#  WeRentCar_appstore_zhidaochuxing 2
project_arr.append({'scheme_name':'appstore_zhidaochuxing', 'provisioning_profile':'XC iOS: com.zhidaoappstore.WeRentCar', 'code_sign_identity':'iPhone Distribution: yin biao (JKCLZ3XU5V)', 'project_bundle_identifier':'com.zhidaoappstore.WeRentCar'})

#  WeRentCar_appstore_kabadiandong 3   block
#project_arr.append({'scheme_name':'appstore_kabadiandong', 'provisioning_profile':'XC iOS: com.kabazucheAppstore.WeRentCar', 'code_sign_identity':'iPhone Distribution: Kaba Electric Car Rental (Hangzhou) Co., Ltd. (Y7A27MQ967)', 'project_bundle_identifier':'com.kabazucheAppstore.WeRentCar'})

#  appstore_gangshuntong 4
project_arr.append({'scheme_name':'appstore_gangshuntong', 'provisioning_profile':'gangshuntong_fabu', 'code_sign_identity':'iPhone Distribution: SHEN ZHEN GANEN TECHNOLOGY GROUP CO;LTD (39FL249LEZ)', 'project_bundle_identifier':'com.gangshuntongAppStore.WeRentCar'})

#  WeRentCar_appstore_xiangkaichuxing 5   block
#project_arr.append({'scheme_name':'appstore_xiangkaichuxing', 'provisioning_profile':'xiangkaiapp_fabu', 'code_sign_identity':'iPhone Distribution: you di (8YSU2BSV5L)', 'project_bundle_identifier':'com.xiangkaichuxingAppStore.WeRentCar'})

#  WeRentCar_beijingchuxing 6
project_arr.append({'scheme_name':'beijingchuxing', 'provisioning_profile':'beijingchuxingAppstore', 'code_sign_identity':'iPhone Distribution: BEIJING TREK AUTO SERVICE CO.,LTD. (YZL68LYGD2)', 'project_bundle_identifier':'com.beijingchuxingAppstore.WeRentCar'})

#  WeRentCar_wanyunzuche 7
project_arr.append({'scheme_name':'wanyunzuche', 'provisioning_profile':'wanyunzuchedabao', 'code_sign_identity':'iPhone Distribution: shijian li (62HP4XBA8P)', 'project_bundle_identifier':'com.wanyunzucheAppstore.WeRentCar'})

#  WeRentCar_wuxizuche 8
project_arr.append({'scheme_name':'wuxizuche', 'provisioning_profile':'wuxizuche_fabu', 'code_sign_identity':'iPhone Distribution: Guolian Kelu Wuxi New Power Co., Ltd. (PBFZ632YUX)', 'project_bundle_identifier':'com.wuxizucheAppstore.WeRentCar'})

#  WeRentCar_weilanchuxingappstore 9
project_arr.append({'scheme_name':'weilanchuxingappstore', 'provisioning_profile':'weilanchuxingfabu', 'code_sign_identity':'iPhone Distribution: BEIJING TREK AUTO SERVICE CO.,LTD. (YZL68LYGD2)', 'project_bundle_identifier':'com.weilanchuxingappstore.WeRentCar'})

#  WeRentCar_Exiangxing 10
project_arr.append({'scheme_name':'Exiangxing', 'provisioning_profile':'ExiangxingAppstore', 'code_sign_identity':'iPhone Distribution: Gansu E-Xiangxing New Energy Development Co., Ltd. (R2MUJJUHCZ)', 'project_bundle_identifier':'com.exiangyongcheAppstore.WeRentCar'})

#  WeRentCar_yifanchuxing 11
project_arr.append({'scheme_name':'yifanchuxing', 'provisioning_profile':'yifanchuxingfabu', 'code_sign_identity':'iPhone Distribution: Shantou Yifan Car Rental Service Co., Ltd. (6PZ8XC5GLM)', 'project_bundle_identifier':'com.yifanchuxAppStore.WeRentCar'})

#   WeRentCar_rangozuche 12
project_arr.append({'scheme_name':'rangozuche', 'provisioning_profile':'rangozuchefabu', 'code_sign_identity':'iPhone Distribution: Shenzhen Ranglin Network Co., Ltd. (7N3Y8UJC38)', 'project_bundle_identifier':'com.rangozucheAppStore.WeRentCar'})

#  WeRentCar_dashengchuxing 13
project_arr.append({'scheme_name':'dashengchuxing', 'provisioning_profile':'dashengchuxingfabu', 'code_sign_identity':'iPhone Distribution: Fujian Dasheng Travel Technology Co., Ltd. (BA77UGP9E6)', 'project_bundle_identifier':'com.dashengchuxingAppStore.WeRentCar'})

#  WeRentCar_youchichuxing 14
project_arr.append({'scheme_name':'youchichuxing', 'provisioning_profile':'xc-ios-com.youchichuxingAppstore.WeRentCar', 'code_sign_identity':'iPhone Distribution: Fuzhou Utrip New Energy Technology Co., Ltd. (MKRZ367ZHA)', 'project_bundle_identifier':'com.youchichuxingAppstore.WeRentCar'})

#  WeRentCar_weichuxing 15
project_arr.append({'scheme_name':'weichuxing', 'provisioning_profile':'weichuxingfabu', 'code_sign_identity':'iPhone Distribution: Zuowei Xie (YRDB434N5Y)', 'project_bundle_identifier':'com.weichuxingappstore.WeRentCar'})

#  WeRentCar_lixiangchuxing 16
project_arr.append({'scheme_name':'lixiangchuxing', 'provisioning_profile':'lixiangchuxingAppstoreFabu', 'code_sign_identity':'iPhone Distribution: HUNAN ABLE FLY U-CAR NEW ENERGY VEHICLE OPERATION CO.,LTD. (YE5RBXQJEK)', 'project_bundle_identifier':'com.lixiangchuxingAppStore.WeRentCar'})

#  WeRentCar_bananachuxing 17
project_arr.append({'scheme_name':'bananachuxing', 'provisioning_profile':'bananachuxingfabuappstore', 'code_sign_identity':'iPhone Distribution: Shenzhen Banana Technology Co.,Ltd. (GR6ZJTM9VW)', 'project_bundle_identifier':'com.bananachuxingAppStore.WeRentCar'})

#  WeRentCar_shiguangchuxing 18
project_arr.append({'scheme_name':'shiguangchuxing', 'provisioning_profile':'shiguangchuxingfabu', 'code_sign_identity':'iPhone Distribution: Lijiang Xiang Teng car rental Co., Ltd. (LC2753J9WU)', 'project_bundle_identifier':'com.shiguangchuxingAppstore.WeRentCar'})

#  WeRentCar_biyuanzuche 19
project_arr.append({'scheme_name':'biyuanzuche', 'provisioning_profile':'biyuanzuchefabu', 'code_sign_identity':'iPhone Distribution: Qingyuan BiYuan Car Rental Service Co., Ltd. (4MA2FF5R2B)', 'project_bundle_identifier':'com.biyuanAppStore.WeRentCar'})

#  WeRentCar_dadayongche 20
project_arr.append({'scheme_name':'dadayongche', 'provisioning_profile':'dadayongchefabu', 'code_sign_identity':'iPhone Distribution: meiling Liu (KBP2BW987S)', 'project_bundle_identifier':'com.dadayongcheAppstore.WeRentCar'})

#  WeRentCar_shikexing 21
project_arr.append({'scheme_name':'shikexing', 'provisioning_profile':'shikexingfabu', 'code_sign_identity':'iPhone Distribution: GuiJin Zhang (RL4G65Q6M7)', 'project_bundle_identifier':'com.shikexingappstore.WeRentCar'})

##  WeRentCar_warmcar 22
#project_arr.append({'scheme_name':'warmcar', 'provisioning_profile':'warmcarappstorefabu', 'code_sign_identity':'iPhone Distribution: GuangDong  Southern  Intelligent Transportation Co., Ltd. (JGKXST286F)', 'project_bundle_identifier':'com.warmcarAppStore.WeRentCar'})

#  WeRentCar_jinglingchuxing 23
project_arr.append({'scheme_name':'jinglingchuxing', 'provisioning_profile':'jinglingchuxingappstore', 'code_sign_identity':'iPhone Distribution: xingxiang yang (PB89478M9Y)', 'project_bundle_identifier':'com.jinglingchuxingAppstore.WeRentCar'})

#  WeRentCar_dianxiaoer 24
project_arr.append({'scheme_name':'dianxiaoer', 'provisioning_profile':'xuzhouchuxingfabu', 'code_sign_identity':'iPhone Distribution: Xuzhou green travel Automobile Service Co.,Ltd (8367693744)', 'project_bundle_identifier':'com.xuzhouchuxingappstore.WeRentCar'})

#  jiajiachuxing 25
project_arr.append({'scheme_name':'jiajiachuxing', 'provisioning_profile':'xuzhouchuxingfabu', 'code_sign_identity':'iPhone Distribution: Shandong yiluchangtong car rental co.LTD (E7G57UAZ7H)', 'project_bundle_identifier':'com.jiajiachuxing.app'})

#  quyongche 26
project_arr.append({'scheme_name':'quyongche', 'provisioning_profile':'xuzhouchuxingfabu', 'code_sign_identity':'iPhone Distribution: Wuhan easily use Internet Technology Co., Ltd. (799BDT7TB8)', 'project_bundle_identifier':'com.quyongche.appstore'})

#  appstore_mengdagongxiang 27
project_arr.append({'scheme_name':'appstore_mengdagongxiang', 'provisioning_profile':'xuzhouchuxingfabu', 'code_sign_identity':'iPhone Distribution: Fujian Meng Da Amperex Technology Limited (W2AVZ6FZYG)', 'project_bundle_identifier':'com.mengdagongxiang.app'})

#  wochuxing 28
project_arr.append({'scheme_name':'wochuxing', 'provisioning_profile':'xuzhouchuxingfabu', 'code_sign_identity':'iPhone Distribution: Guanmiao Lin (3L8GQSJN3B)', 'project_bundle_identifier':'com.wochuxingappstore.zhongwo'})

#  appstore_diandianyongche 29
project_arr.append({'scheme_name':'appstore_diandianyongche', 'provisioning_profile':'xuzhouchuxingfabu', 'code_sign_identity':'iPhone Distribution: nan zhang (4LXXU8RMVY)', 'project_bundle_identifier':'com.diandianyongcheAppstore.app'})

#  gongchuanggongxiang 30
project_arr.append({'scheme_name':'gongchuanggongxiang', 'provisioning_profile':'xuzhouchuxingfabu', 'code_sign_identity':'iPhone Distribution: Guangdong Innovation Energy Automotive Co., Ltd. (RW2DDZV7HG)', 'project_bundle_identifier':'com.gongchuanggongxiangAppstore.WeRentCar'})



# print 'project_arr  ==  ',project_arr
# print 'project_arr[1]  ==  ',project_arr[1]
