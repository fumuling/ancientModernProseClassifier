f1 = open("D:\周景怡\周景怡\WHU\大三上\文本理解与数据挖掘\文言文数据qingxi.txt",'r',encoding='utf-8')
f2 = open("D:\周景怡\周景怡\WHU\大三上\文本理解与数据挖掘\文言文去空行.txt",'w',encoding='utf-8')

for line in f1.readlines():
    if line == '\n':
        line = line.strip('\n')
    f2.write(line)

f1.close()
f2.close()