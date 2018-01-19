# -*- coding: utf-8 -*-
__author__ = 'pengbingxiang'

import subprocess
import Config
import datetime
import os

class Upload:
    def loadPGY(self, ipa_path, user_key, api_key):
        formt_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        print 'time:', formt_time
        
        project_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        
        loadCmd = "curl -F file=@" + ipa_path + " -F uKey=" + user_key + " -F _api_key=" + api_key + " http://www.pgyer.com/apiv1/app/upload | xargs echo >> " + project_path + "/log"
        
        print 'loadCmd: ',loadCmd
        load = subprocess.Popen(loadCmd, shell=True)
        
        # 等上一步执行完再执行下一步
        load.wait()


if  __name__ == '__main__':
    loadPGY = Upload().loadPGY()
    print loadPGY
