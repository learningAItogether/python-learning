#连线到特定网址,抓取资料
import urllib.request as req

def getData(url):
    i=1
    request = req.Request(url,headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43"
        })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
        #解析资料，取得实际想要的部分
    import bs4
        #beautifulSoup协助解析HTML文件格式
    root = bs4.BeautifulSoup(data,"html.parser") #套件解析Html格式
        #寻找所有的class = "s xst"的<a>链接的电影标题
    titles = root.find_all("div",class_="title")
    
    for title in titles:
        if title.a != None:
            print(i,title.a.string) # a标签里面的字符
            i+=1
        #抓取下一页
    nextpage = root.find("a",string="‹ 上頁") #找到内文是‹ 上頁的标签
    return nextpage["href"]

urlPage="https://www.ptt.cc/bbs/Gossiping/index39346.html"

count = 0
while count<3:
    urlPage = "https://www.ptt.cc/"+getData(urlPage)
    count+=1