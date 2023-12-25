# На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.

class FIFO_1:
    def __init__(self):
        self.__buf = []

    def insert(self, value):
        self.__buf.append(value)

    def get(self):
        if len(self.__buf) > 0:
            return self.__buf.pop(0)
        else:
            raise IndexError("Пустая очередь")

class FIFO_obj:
    def __init__(self, value):
        self.value = value
        self.next: 'FIFO_obj' = None        

class FIFO_2:
    def __init__(self):
        self.__head: FIFO_obj = None

    def insert(self, value) -> None:
        if self.__head is None:
            self.__head = FIFO_obj(value)
        else:
            tmp: FIFO_obj = self.__head
            while tmp.next is not None:
                tmp = tmp.next
            tmp.next = FIFO_obj(value)

    def get(self):
        if not self.__head:
            raise IndexError("Пустая очередь")
        else:
            temp = self.__head
            self.__head = self.__head.next
            return temp.value
            