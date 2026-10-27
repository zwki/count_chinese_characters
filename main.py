"""写一个读取 TXT 文件、统计词频、输出结果的小程序。"""

# word_dict={}
# with open("test",'r',encoding='utf_8') as f:
#     content=f.read()
# for i in content:
#     if i=='\n':
#         continue
#     word_dict[i]=word_dict.get(i,0)+1
# for x,y in word_dict.items():
#     print(f'{x},{y}')
def Count_NUM(file_path):
    word_dict = {}
    with open(file_path, 'r', encoding='utf-8') as f:#文件名之后不可以加双引号
        content = f.read()
    for i in content:
        if i == '\n':
            continue
        word_dict[i] = word_dict.get(i, 0) + 1
    for x, y in word_dict.items():
        print(f'{x},{y}')

if __name__=="__main__":
    path=input("请输入txt文件路径：")
    fp=Count_NUM(path)
