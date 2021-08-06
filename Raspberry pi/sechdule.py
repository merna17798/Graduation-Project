import subprocess
from crontab import CronTab
import requests
import json
import time

# check for time now
time_now = time.localtime() 
day = time.strftime("%Y-%m-%d",time_now)
timeStamp=time.strftime("%H:%M:%S",time_now)
s=timeStamp.split(":")
local_hour=int(s[0])
local_min=int(s[1])
print(local_hour ,local_min)
##dictionary to pass to api
x = {}
## covert dictionary to json object 
sorted_string = json.dumps(x, indent=4, sort_keys=True)
#requesting API
url="http://192.168.43.198/LoginRegister/getid.php"
r = requests.post(url, json=x)
arr=json.loads(r.text)
IDs=[]
out=[]
for i in range(len(arr)):
    IDs.append(int(arr[i]['id']))
print(IDs)
for i in IDs :
    x = {'id': i}
    url="http://192.168.43.198/LoginRegister/getVISIT.php"
    r2 = requests.post(url, json=x)
    try:
        arr2=json.loads(r2.text)
        for k in range(len(arr2)):
            splitted=arr2[k]['time'].split(":")
            hour=splitted[0]
            minute=splitted[1]
            if(int(hour) >= local_hour):
                if(int(hour) == local_hour):
                    if(int(minute) >= local_min):
                        out.append([i,int(hour),int(minute),int(arr2[k]['isvideocall'])])
                else:
                    out.append([i,int(hour),int(minute),int(arr2[k]['isvideocall'])])
    except :
        pass

for i in range(len(out)):
    
    x = {'id': out[i][0]}
    url="http://192.168.43.198/LoginRegister/bed.php"
    r3 = requests.post(url, json=x)
    arr3=json.loads(r3.text)
    #print(arr3)
    for k in range(len(arr3)):
        out[i].append(int(arr3[k]['roomid']))
        out[i].append(arr3[k]['color'])
# Result array
#[ [patientid ,hour, minute, (0->measure 1->call 2->both) ,roomid ,bed_color],..]

print(out)
print(len(out))
class CronSet:
    def __init__(self):
        self._crontab = CronTab(tabfile="/home/pi/Documents/cron_jobs.txt")

    def add_job(self, minute, hour, day, month,cmd,comment):
        subprocess.call('crontab -l > /home/pi/Documents/cron_jobs.txt', shell=True)        

        cmd =cmd
        comment=comment
        job = self._crontab.new(cmd,comment)
        job.setall(minute, hour, day, month, None)

    def save(self):
        self._crontab.write()
    def removeall(self):
        self._crontab.remove_all()

def main():
    c = CronSet()
    
    c.removeall()
    for i in range(len(out)):
        if out[i][3]==0:
            c.add_job(out[i][2], out[i][1], '*', '*',"python measure.py","update")
        elif out[i][3]==1:
            c.add_job(out[i][2], out[i][1], '*', '*',"export DISPLAY=:0 && cd /home/pi/Desktop/task3 && python3 hello.py","update")
        else:
            c.add_job(out[i][2], out[i][1], '*', '*',"python both.py","update")
    c.save()
    subprocess.call('crontab /home/pi/Documents/cron_jobs.txt', shell=True)

if __name__ == '__main__':
    main()