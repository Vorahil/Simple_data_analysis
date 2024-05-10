"""
数据定义的类
"""


class Record:
    def __init__(self, data, order_id, money, province):
        self.data = data  # 订单的日期
        self.order_id = order_id  # 订单的id
        self.money = money  # 订单的金额
        self.province = province  # 订单的省份

    def __str__(self):
        """使返回对应值而不是地址"""
        return f"{self.data},{self.order_id},{self.money},{self.province}"


if __name__ == '__main__':
    record1 = Record(1, 2, 3, 4)
    record2 = Record(1, 2, 3, 4)
    record3 = Record(1, 2, 3, 4)
    list1 = [record1, record2, record3]
    print(list1)
    for record in list1:
        print(record)
