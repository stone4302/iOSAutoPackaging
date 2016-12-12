# -*- coding: utf-8 -*-
# flake8: noqa


import datetime
import Config
from Packaging import Packaging
from Upload import Upload
from biplist import *
import os


formt_time = datetime.datetime.now().strftime("%Y-%m-%d")
print 'start time: ', formt_time

for num in range(0,2):
    print "num --- ",num
    
    plist_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'template', 'config.plist'))
    plist = readPlist(plist_path)
    
    scheme_name = plist["items"][num]['scheme_name']
    
    provisioning_profile = plist["items"][num]['provisioning_profile']
    
    user_key = plist["items"][num]['user_key']
    
    api_key = plist["items"][num]['api_key']

    print "********scheme_name,provisioning_profile,user_key,api_key*********",scheme_name,provisioning_profile,user_key,api_key

    print "***********************************************************************************"
    print " 开始 -- ARCHIVE -- EXPORT -- "
    print "***********************************************************************************"

    ipa_path = Packaging().newIpa(scheme_name, provisioning_profile)

    print "***********************************************************************************"
    print " -- ARCHIVE -- EXPORT -- 结束 -- "
    print " 开始 -- UPLOAD -- PGY -- "
    print "***********************************************************************************"

    load = Upload().loadPGY(ipa_path, user_key, api_key)

    print "***********************************************************************************"
    print " -- UPLOAD -- PGY -- 结束 -- "
    print "***********************************************************************************"




