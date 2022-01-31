#总结：获取文章标题。1 获取真正的网址 2 观察什么格式数据 3 解析Json格式，去除看不懂部分
#连线到特定网址，抓取资料
import urllib.request as req
url ="https://medium.com/_/api/home-feed"
request = req.Request(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")  
#print(data) #根据观察取得的资料为Json格式
#解析资料，获取文章标题
import json
data = data.replace("])}while(1);</x>","")
data = json.loads(data) #把原始资料整理为字典/ 列表的表示格式
#取得Json资料中的文章的标题
posts = data["payload"]["references"]["Post"]
for key in posts:
    post = posts[key] #取出字典中的每一个key
    print(post["title"]) #取出单篇文章下的title