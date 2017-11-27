
# coding: utf-8

# In[31]:


import os
iperf = os.system("iperf3 -c node-3  &")
val = os.popen('ping node-3 -c 10').read()
a = val.split('/')
avg = a[-3]
f = open("a.txt", "a")
#f.read()
f.write(avg+'\n')
os.system('killall iperf3')
f.close()

