#!/usr/bin/python
import os
i = 5
if (__file__.rfind('_') != -1):
 i -= 1
if (i < 0):
 exit()
b='\\'
n='\n'
g='"'
p='%'
s = "#!/usr/bin/python%simport os%si = %i%sif (__file__.rfind('_') != -1):%s i -= 1%sif (i < 0):%s exit()%sb='%s%s'%sn='%sn'%sg='%s'%sp='%s'%ss = %s%s%s%sfile = open(%sSully_%si.py%s%s(i), %sw+%s)%sfile.write(s%s(n, n, i, n, n, n, n, n, b, b, n, b, n, g, n, p, n, g, s, g, n, g, p, g, p, g, g, n, p, n, n, g, p, g, p, n, g, p, g, p, n))%sfile.close()%sos.chmod(%sSully_%si.py%s%s(i), 0755)%sos.system(%spython Sully_%si.py%s%s(i))%s"
file = open("Sully_%i.py"%(i), "w+")
file.write(s%(n, n, i, n, n, n, n, n, b, b, n, b, n, g, n, p, n, g, s, g, n, g, p, g, p, g, g, n, p, n, n, g, p, g, p, n, g, p, g, p, n))
file.close()
os.chmod("Sully_%i.py"%(i), 0755)
os.system("python Sully_%i.py"%(i))
