#储存档案
file = open("data.text",mode="w",encoding="utf-8") #开启
file.write("Hello File\nSecond line\n") #操作
file.write("测试中文\n棒")
file.close() #关闭

with open("data.text",mode="w",encoding="utf-8") as file:
    file.write("5\n5")
#读取档案
#把档案中的数字文字一行行的读取出来，并计算
sum = 0
with open("data.text",mode="r") as file:
    for line in file:
        print(line)
        sum+=int(line)
print("文章中数字相加为：",sum)
#使用JSON格式读取、复写档案
import json
with open("config.json",mode="r") as file:
    data =json.load(file)
print(data)
data["name"] = "new name"
print("name:",data["name"])
print("version:",data["version"])

with open("config.json",mode="w") as file:
    json.dump(data,file)