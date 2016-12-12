# -*- coding: utf-8 -*-
__author__ = 'pengbingxiang'

import subprocess
import Config
import os
import datetime


class Packaging:
    def newIpa(self, scheme_name, provisioning_profile):
        formt_time = datetime.datetime.now().strftime("%Y%m%d%H%M")
        archive_name = scheme_name + formt_time + '.xcarchive'
        archivePath = os.path.abspath(os.path.join(os.path.dirname(__file__),'history',formt_time, archive_name))
        projectPath = Config.project_path + Config.workspace_name
        # xcarchive
        print "projectPath ---- ",projectPath
        archiveCmd = "xcodebuild -derivedDataPath " + projectPath + " -scheme " + scheme_name + ' -archivePath ' + archivePath + ' clean archive'
        
        print 'archiveCmd: ',archiveCmd
        process = subprocess.Popen(archiveCmd, shell=True)
        # 等上一步执行完再执行下一步
        process.wait()

        # 打包成ipa包
        export_name = scheme_name + formt_time + '.ipa'
        exportPath = os.path.abspath(os.path.join(os.path.dirname(__file__),'history',formt_time, export_name))
    
        exportCmd = 'xcodebuild -exportArchive -archivePath ' + archivePath + ' -exportPath ' + exportPath + ' -exportFormat ipa -exportProvisioningProfile ' + provisioning_profile
        print 'exportCmd: ',exportCmd
        exportProcess = subprocess.Popen(exportCmd, shell=True)
        exportProcess.wait()
        return exportPath



if  __name__ == '__main__':
    new_ipa = Packaging().newIpa()
    print new_ipa


