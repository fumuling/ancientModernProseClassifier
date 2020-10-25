import json

# def catch_value(file_name, value,position):
#     """提取所需元素的方法"""
#     f = open(file_name, encoding='utf-8')
#     setting = json.load(f)  # 把json文件转化为python用的类型
#     f.close()
#     my_value = setting[position][value]  # 提取元素中所需要的的值
#     return my_value

f = open("D:\周景怡\周景怡\WHU\大三上\文本理解与数据挖掘\chinese-poetry-master\peot11\peot1.json",encoding="utf-8")
setting = json.load(f)
f.close()

for i in range(len(setting)):
    f = open('D:\周景怡\周景怡\WHU\大三上\文本理解与数据挖掘\chinese-poetry-master\peot11\peot1.txt', 'a',encoding="utf-8")
    f.write('\n' + str(setting[i].get("paragraphs")))
    f.close()

