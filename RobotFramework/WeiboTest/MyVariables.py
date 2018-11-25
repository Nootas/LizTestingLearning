import os
import time
import linecache

CURRENT_TIME = time.asctime()  #timestamp
MESSAGE = linecache.getline("doc.txt",1) #lineno start from 1
#MESSAGE = linecache.getline("doc.txt",1).strip()
