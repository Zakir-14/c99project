import shutil 
import os
import time

path = input("ENTER THE PATH : ")
isExist=os.path.exists(path)
if isExist=="true":
    print("PATH FOUND!")
elif isExist=="false":
    print("PATH NOT FOUND!")    

days = 30
seconds =time.time(days-24*60*60)

ctime = os.stat(path)


for path in os.walk(path):
    if





       
