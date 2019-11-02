import os,sys,platform
ini="""[global]
index-url = https://pypi.doubanio.com/simple/
[install]
trusted-host=pypi.doubanio.com
"""
os_version=platform.platform()
if 'Windows' in os_version:
    os_flag=False
    file_name='pip.ini'
else:
    os_flag=True
    file_name='pip.conf'
if os_flag==True:
    pippath=os.environ["HOME"]+os.sep+".pip"+os.sep
else:
    pippath=os.environ["USERPROFILE"]+os.sep+"pip"+os.sep
if not os.path.exists(pippath):
    os.mkdir(pippath)
with open(pippath+file_name,"w") as f:
    f.write(ini)
