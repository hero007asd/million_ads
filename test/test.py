# import system
# print system.test.test1()
import os
print os.getcwd()

import sys
# sys.path.append("D:\\Github\\million_ads\\system")
sys.path.append(os.path.dirname(os.getcwd())+"/system")
# import test1
print sys.path
import test1
print test1.test2()
# print test.test1()

print os.path.dirname(os.getcwd())