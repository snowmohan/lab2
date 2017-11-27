import os
import time
for i in range(1,97):
    thr = str(i)
    cmd = 'iperf3 -c node-3 '+'-b '+thr+'Mb'+' -t 300'+' &'
    iperf = os.system(cmd)
    time.sleep(5)
    val = os.popen('ping node-3 -i 0.2 -c 1200').read()
    a = val.split('/')
    avg = a[-3]
    f = open("a.txt", "a")
    f.write(thr+' '+avg+'\n')
    os.system('killall iperf3')
    f.close()
    time.sleep(1)
