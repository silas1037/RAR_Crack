#coding=gbk

import os
import subprocess

for pwd in readdiralllines("D:/Silas/Python/Python_Work/passme.txt"):
    src = "D:/z.rar"
    rc, out = subprocess.getstatusoutput("E:/PORTABLE/cmder/Rar.exe t -r \"%s\" -p\"%s\"" % (src,pwd))
    if rc != 0:
        out = 'error'
    else:
        out = 'pass'
    print(rc,out,pwd)