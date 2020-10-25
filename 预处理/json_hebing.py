# 合并json
import os
# 获取目标文件夹的路径
# filedir ='C:/Users/Desktop/04072'
filedir ='D:\周景怡\周景怡\WHU\大三上\文本理解与数据挖掘\chinese-poetry-master\peot22'
# 获取当前文件夹中的文件名称列表
# filenames=os.listdir(filedir)
filenames=os.listdir(filedir)
# 打开当前目录下的result.json文件，如果没有则创建
f = open('D:\周景怡\周景怡\WHU\大三上\文本理解与数据挖掘\chinese-poetry-master\peot22\peot2.json','w',encoding="utf-8")
# 先遍历文件名`在这里插入代码片`
for filename in filenames:
    filepath = filedir+'/'+filename
    # 遍历单个文件，读取行数
    for line in open(filepath, encoding="utf-8"):
        f.writelines(line)
        f.write('\n')
# 关闭文件
f.close()
