import os
import shutil


# 删除指定文件
def deldir(startdir, target):
    os.chdir(startdir)
    for obj in os.listdir(os.curdir):
        if obj == target:
            print(os.getcwd() + os.sep + obj)
            try:
                # os.remove(obj)
                shutil.rmtree(obj)
            except IOError:
                print("exception")
        if os.path.isdir(obj):
            deldir(obj, target)
            os.chdir(os.pardir)  # !!!


deldir("D:\OneDrive\AndroidStudioProjects\FirstLineOfCode", "build")
