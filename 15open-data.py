#网路连线
import urllib.request as request
import json
src = "https://wic.heo.taipei/OpenData/API/Rain/Get?stationNo=&loginId=open_rain&dataKey=85452C1D"
with request.urlopen(src) as response:
    data = json.load(response)

#将公司名称列表出来

print(data["count"])
a = data["data"]
j=0
for i in a:
    j+=1
    print("第",j,"个县名字为：",i["stationName"],"\n")