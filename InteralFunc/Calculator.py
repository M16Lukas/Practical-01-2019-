class Calculator:
    def __init__(self, input):
        self.input = input  # 리스트 입력 받음

    def sum(self):
        result = 0
        for i in self.input:
            result += i
        return result

    def avg(self):
        final = self.sum()
        return final / len(self.input)


cal1 = Calculator([1, 2, 3, 4, 5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6, 7, 8, 9, 10])
print(cal2.sum())
print(cal2.avg())
