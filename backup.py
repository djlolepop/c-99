import os 
import shutil
source = "/users/jatinsai/downloads/djlolepoop/"
dest = "/users/jatinsai/downloads/back up/"
listOfFiles = os.listdir(source)
for file in listOfFiles:
    shutil.copy((source+file),dest)
