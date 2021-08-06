import requests
import json
import time
import requests
import json
import time
### check for time now
time_now = time.localtime() 
day = "2021-05-17"
timeStamp="17:00:00"
id=1
##dictionary to pass to api
x = {"day":day ,"time":timeStamp ,"patientid":id}
## covert dictionary to json object 
sorted_string = json.dumps(x, indent=4, sort_keys=True)
#requesting API
url="http://172.20.10.2/LoginRegister/vrefy.php"
r = requests.post(url, json=x)
print(r.text)