import random
import time
import unittest


from task1 import isEven
from task2 import FIFO_1, FIFO_2
from task3 import quick_sort, merge_sort

def exampleIsEven(value):
    return value % 2 == 0

class TestEven(unittest.TestCase):
    def test_even(self):
        for _ in range(1000):
            test_case = random.randint(1, 1000)
            self.assertEqual(exampleIsEven(test_case), isEven(test_case))

class test_FIFO(unittest.TestCase):
    def test_equality(self):
        fifo1 = FIFO_1()
        fifo2 = FIFO_2()

        for _ in range(1000):
            test_case = random.randint(1, 1000)
            fifo1.insert(test_case)
            fifo2.insert(test_case)

        for _ in range(1000):
            self.assertEqual(fifo1.get(), fifo2.get())
            
    def test_correctness(self):
        fifo1 = FIFO_1()
        fifo2 = FIFO_2()

        test_vals = [random.randint(1, 1000000) for _ in range(1000)]

        for test_case in test_vals:
            fifo1.insert(test_case)
            fifo2.insert(test_case)

        for test_case in test_vals:
            self.assertEqual(fifo1.get(), test_case)
            self.assertEqual(fifo2.get(), test_case)

    def test_timings(self):
        fifo1 = FIFO_1()
        fifo2 = FIFO_2()

        test_vals = [random.randint(1, 1000000) for _ in range(10000)]

        print("\nТест скорости добавления в FIFO")

        start1 = time.time()
        for test_case in test_vals:
            fifo1.insert(test_case)
        end1 = time.time()

        start2 = time.time()
        for test_case in test_vals:
            fifo2.insert(test_case)
        end2 = time.time()

        
        print(f"FIFO_1: {end1 - start1}")
        print(f"FIFO_2: {end2 - start2}")

        print("\nТест скорости получения из FIFO")

        start1 = time.time()
        for test_case in test_vals:
            fifo1.get()
        end1 = time.time()

        start2 = time.time()
        for test_case in test_vals:
            fifo2.get()
        end2 = time.time()

        
        print(f"FIFO_1: {end1 - start1}")
        print(f"FIFO_2: {end2 - start2}")

class testSort(unittest.TestCase):
    def test_sort(self):
        test_case = [random.randint(1, 10000) for _ in range(1000)]
        self.assertListEqual(quick_sort(test_case), sorted(test_case))
        merged = test_case[:]
        merge_sort(merged)
        self.assertListEqual(merged, sorted(test_case))
        
    def test_timings(self):
        t1 = []
        t2 = []
        t3 = []
        print("\nСравнение скорости сортировок")
        for _ in range(100):
            test_case = [random.randint(1, 10000) for _ in range(10000)]

            start1 = time.time()
            quick_sort(test_case)
            end1 = time.time()

            start2 = time.time()
            sorted(test_case)
            end2 = time.time()

            start3 = time.time()
            merge_sort(test_case)
            end3 = time.time()

            t1.append(end1 - start1)
            t2.append(end2 - start2)
            t3.append(end3 - start3)

        print(f"Среднее время быстрой сортировки: {sum(t1)/len(t1)}\n Худшее время: {max(t1)}")
        print(f"Среднее время стандартной сортировки: {sum(t2)/len(t2)}\n Худшее время: {max(t2)}")
        print(f"Среднее время сортировки слиянием: {sum(t3)/len(t3)}\n Худшее время: {max(t3)}")



if __name__ == "__main__":
    unittest.main()
