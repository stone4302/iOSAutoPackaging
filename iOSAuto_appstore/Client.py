# -*- coding: utf-8 -*-
# flake8: noqa


import datetime
import Config
from Packaging import Packaging
from biplist import *
import os


formt_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
print 'start time: ', formt_time

now_time = datetime.datetime.now().strftime("%Y%m%d%H%M")

project_arrs = Config.project_arr
print 'project_arrs = ',project_arrs

plist_path = Config.plist_name

for num in range(0,len(project_arrs)):
    print "num --- ",num
    
    scheme_name = project_arrs[num]['scheme_name']
    
    provisioning_profile = project_arrs[num]['provisioning_profile']
    
    code_sign_identity = project_arrs[num]['code_sign_identity']
    
    project_bundle_identifier = project_arrs[num]['project_bundle_identifier']
    

    print "****scheme_name,provisioning_profile,code_sign_identity,project_bundle_identifier,plist_path****",scheme_name,provisioning_profile,code_sign_identity,project_bundle_identifier,plist_path

    print "***********************************************************************************"
    print " 开始 -- ARCHIVE -- EXPORT -- ",num
    print "***********************************************************************************"

    ipa_path = Packaging().newIpa(scheme_name, now_time, plist_path, provisioning_profile, code_sign_identity, project_bundle_identifier)

    print "***********************************************************************************"
    print " -- ARCHIVE -- EXPORT -- 结束 -- ",num
    print "***********************************************************************************"






