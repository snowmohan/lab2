import os
import time
for i in range(1,40):
    thr = str(i)
    cmd = 'iperf3 -c node-1 '+'-b '+thr+'Mb'+' -t 300'+' &'
    iperf = os.system(cmd)
    time.sleep(5)
    val = os.popen('ping node-1 -i 0.2 -c 300').read()
    a = val.split('/')
    avg = a[-3]
    f = open("a.txt", "a")
    f.write(thr+' '+avg+'\n')
    os.system('killall iperf3')
    f.close()
    time.sleep(1)
