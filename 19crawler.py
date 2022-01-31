# 抓取网页原始码（HTML）
 #1 网络连线
import urllib.request as req
url = "https://www.m1910.com/"
src ="https://www.btsj5.com/"
 #1打开源代码，#2 找到网络 选择ALL #3 user-agent
request = req.Request(src,headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43"
    })
 #2 获取源代码
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
 #如果打不开 建立request物件，附加Request Headers的资讯

 #3 打印data
#print(data)
# 解析原始码，取得每篇文章的标题
import bs4
root = bs4.BeautifulSoup(data,"html.parser") #用套件进行解析
titles = root.find_all("div",class_ = "cap")
i =0
for title in titles:
    i+=1
    print("第",i,"个标题为：",title.string)
# 找原始码的特色