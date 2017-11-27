import os
import time
for i in range(1,102,10):
    thr = str(i)
    cmd = 'iperf3 -c node-3 '+'-b '+thr+'Mb'+' -t 240'+' &'
    iperf = os.system(cmd)
    time.sleep(5)
    val = os.popen('ping node-3 -c 60').read()
    a = val.split('/')
    avg = a[-3]
    f = open("a.txt", "a")
    f.write(avg+' '+thr+'\n')
    os.system('killall iperf3')
    f.close()
