"""写一个读取 TXT 文件、统计词频、输出结果的小程序。"""

# word_dict={}
# with open("test.txt",'r',encoding='utf_8') as f:
#     content=f.read()
# for i in content:
#     if i=='\n':
#         continue
#     word_dict[i]=word_dict.get(i,0)+1
# for x,y in word_dict.items():
#     print(f'{x},{y}')
from pathlib import Path
import json
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# def Count_NUM(file_path):
#     word_dict = {}
#     with open(file_path, 'r', encoding='utf-8') as f:#文件名之后不可以加双引号
#         content = f.read()
#     for i in content:
#         if i == '\n':
#             continue
#         word_dict[i] = word_dict.get(i, 0) + 1
#     for x, y in word_dict.items():
#         print(f'{x},{y}')
def read_file(file_path:Path)->str:
    """读取文本文件"""
    logging.info("准备读取文件：%s",file_path)

    try:
        text=file_path.read_text(encoding="utf_8")
    except FileNotFoundError:
        logging.error("文件不存在：%s", file_path)
        raise
    except PermissionError:
        logging.error("没有权限读取文件：%s", file_path)
        raise
    if not text.strip():
        logging.warning("文件内容为空：%s", file_path)
        raise ValueError(f"输入文件为空:{file_path}")
    logging.info("文件读取成功：%s", file_path)
    return text
def save_result(result:dict[str,int],output_path:Path)->None:
    """保存词频统计结果"""
    try:
        output_path.parent.mkdir(parents=True,exist_ok=True)

        with output_path.open("w",encoding="utf_8")as file:
            json.dump(result,file,ensure_ascii=False,indent=4)

    except OSError as error:
        raise OSError (f"保存结果失败：{error}") from error

def main():
    input_text=input("请输入需要统计的文本文件路径：").strip()
    input_path=Path(input_text.strip('"'))
    output_text=input("请输入结果保存路径（例如 output/result.json）：").strip()
    output_path=Path(output_text.strip('"'))
    try:
        text=read_file(input_path)
        result={}
        for word in text.lower().split():
            word = word.strip(".,!?;:")
            if word:
                result[word]=result.get(word,0)+1

        save_result(result,output_path)
        print(f"统计成功！结果已保存到：{output_path.resolve()}")
    except (FileNotFoundError, PermissionError, ValueError, OSError) as error:
        print(f"程序出错：{error}")




if __name__ == "__main__":
    main()