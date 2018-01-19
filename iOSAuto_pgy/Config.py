# -*- coding: utf-8 -*-
__author__ = 'pengbingxiang'

#--------打包信息---------
# 需要打包的项目信息
workspace_name = '/WeRentCar.xcodeproj'

# 打包的Plist文件名
plist_name = 'EnterpriseExportOptionsPlist.plist'

#企业证书名字
ep_cer_name = 'Yiweixing (beijing)Technology Co, Ltd.'

############定制版信息################

project_arr = []
# print 'project_arr  ==  ',project_arr

#  WeRentCar
project_arr.append({'scheme_name':'WeRentCar', 'provisioning_profile':'weizucheGuanWangqiyedabao', 'user_key':'*****', 'api_key':'****'})

# print 'project_arr  ==  ',project_arr
# print 'project_arr[1]  ==  ',project_arr[1]
