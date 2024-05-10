"""
文件相关的类的定义
"""
import json

from data_define import Record


class FileRecord:
    def read_data(self) -> list[Record]:
        """读取文件的数据，独到的每一条数据转换为Record对象，封装到列表里返回"""
        pass


class TextFileRead(FileRecord):
    def __init__(self, path):  # 输入地址
        self.path = path

    def read_data(self) -> list[Record]:
        """读取文件"""
        record_list: list[Record] = []  # 设置返回值的列表
        f = open(self.path, 'r', encoding="UTF-8")  # 打开文件
        for line in f.readlines():  # 每行读取
            line = line.strip()
            data_list = line.split(",")  # 去除空格，用”，“对数据分割，形成列表
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)  # 每次循环都将数据分割的列表某一行加到返回列表
        f.close()
        return record_list


class JsonFileRead(FileRecord):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        """读取文件"""
        record_list: list[Record] = []
        f = open(self.path, 'r', encoding="UTF-8")
        for line in f.readlines():
            record = Record(json.loads(line)["data"], json.loads(line)["order_id"], int(json.loads(line)["money"]),
                            json.loads(line)["province"])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileRead("D:/001.txt")
    list1 = text_file_reader.read_data()
    print(list1)
    for line in list1:
        print(line)
