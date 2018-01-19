# -*- coding: utf-8 -*-
# flake8: noqa


import datetime
import Config
from Packaging import Packaging
from Upload import Upload
from biplist import *
import os


formt_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
print 'start time: ', formt_time

now_time = datetime.datetime.now().strftime("%Y%m%d%H%M")

project_arrs = Config.project_arr
print 'project_arrs = ',project_arrs

plist_path = Config.plist_name

ep_cer_name = Config.ep_cer_name;

for num in range(0,len(project_arrs)):
    print "num --- ",num
    
    scheme_name = project_arrs[num]['scheme_name']
    
    provisioning_profile = project_arrs[num]['provisioning_profile']
    
    user_key = project_arrs[num]['user_key']
    
    api_key = project_arrs[num]['api_key']

    print "********scheme_name,provisioning_profile,user_key,api_key,plist_path*********",scheme_name,provisioning_profile,user_key,api_key,plist_path

    print "***********************************************************************************"
    print " 开始 -- ARCHIVE -- EXPORT -- ",num
    print "***********************************************************************************"

    ipa_path = Packaging().newIpa(scheme_name, ep_cer_name, provisioning_profile, now_time, plist_path)

    print "***********************************************************************************"
    print " -- ARCHIVE -- EXPORT -- 结束 -- ",num
    print "***********************************************************************************"

for num1 in range(0,len(project_arrs)):
    print "num1 --- ",num1
    
    print "***********************************************************************************"
    print " 开始 -- UPLOAD -- PGY -- ",num1
    print "***********************************************************************************"
    scheme_name = project_arrs[num1]['scheme_name']
    
    export_name = scheme_name + '.ipa'
    
    user_key = project_arrs[num1]['user_key']
    
    api_key = project_arrs[num1]['api_key']
    
    ipa_export_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'history',now_time,scheme_name, export_name))
    
    load = Upload().loadPGY(ipa_export_path, user_key, api_key)

    print "***********************************************************************************"
    print " -- UPLOAD -- PGY -- 结束 -- ",num1
    print "***********************************************************************************"




