import os
for i in range(1,4):
    thr = str(i)
    cmd = 'iperf3 -c node-3 '+'-b '+thr+'Mb'
    iperf = os.system(cmd)
    val = os.popen('ping localhost -c 10').read()
    a = val.split('/')
    avg = a[-3]
    f = open("a.txt", "a")
    f.write(avg+thr'\n')
    os.system('killall iperf3')
    f.close()
