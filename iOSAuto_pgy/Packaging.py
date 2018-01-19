# -*- coding: utf-8 -*-
__author__ = 'pengbingxiang'

import subprocess
import Config
import os
import datetime


class Packaging:
    def newIpa(self, scheme_name, ep_cer_name, provisioning_profile, now_time, plist_path):
        formt_time = datetime.datetime.now().strftime("%Y%m%d%H%M")
        archive_name = scheme_name + '.xcarchive'
        archivePath = os.path.abspath(os.path.join(os.path.dirname(__file__),'history',now_time,scheme_name, archive_name))
        project_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        projectPath = project_path + Config.workspace_name
        # xcarchive
        print "projectPath ---- ",projectPath
        archiveCmd = "xcodebuild -derivedDataPath " + projectPath + " -scheme " + scheme_name + ' -archivePath ' + archivePath + ' clean archive'
        
        print 'archiveCmd: ',archiveCmd
        process = subprocess.Popen(archiveCmd, shell=True)
        # 等上一步执行完再执行下一步
        process.wait()
        
        # 打包成ipa包
        export_name = scheme_name + '.ipa'
        exportPath = os.path.abspath(os.path.join(os.path.dirname(__file__),'history',now_time,scheme_name))
        
        exportOptionsPlist_path = os.path.abspath(os.path.join(os.path.dirname(__file__),plist_path))
        
        exportCmd = 'xcodebuild -exportArchive -allowProvisioningUpdates -archivePath ' + archivePath + ' -exportPath ' + exportPath + ' -exportOptionsPlist ' + exportOptionsPlist_path + ' CODE_SIGN_IDENTITY=' + '"' + ep_cer_name + '"'
        print 'exportCmd: ',exportCmd
        exportProcess = subprocess.Popen(exportCmd, shell=True)
        exportProcess.wait()
        return exportPath



if  __name__ == '__main__':
    new_ipa = Packaging().newIpa()
    print new_ipa


