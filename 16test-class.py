#定义类别、类别的属性（封装在类别中的变数，函式）
class IO:
    supportedSrcs = ["console","file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not supported")
        else:
            print("Read from",src)
#使用类别
IO.supportedSrcs
IO.read("file")
IO.read("Internet")