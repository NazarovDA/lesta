1. [<u>Задание 1</u>](https://github.com/NazarovDA/lesta/blob/master/task1.py).

К плюсам моей реализации можно отнести большую производительность, так как нет операции деления.
К минусам можно отнести непривычность и сложность в чтении. К плюсам предложенной реализации можно отнести легкую читаемость и распространенность.
К минусам можно отнести повышенную вычислительную сложность.

2. [<u>Задание 2</u>](https://github.com/NazarovDA/lesta/blob/master/task2.py).

Первый вариант FIFO проще понять и он будет эффективнее при небольших размерах очереди. Но при "вытаскивании" элемента весь список будет смещаться, что может сильно заметить выполнение кода, к тому же такой вариант не очень эффективен в плане использования памяти. Второй вариант более эффективный при больших количествахз информации, так как для того, чтоб убрать элемент из очереди нужно будет лишь поменять 1 ссылку. Так же затрачивается меньше памяти. В то же время при маленьких размерах данных, будет больше нагрузки из-за создания обектов очереди.

3. [<u>Задание 3</u>](https://github.com/NazarovDA/lesta/blob/master/task1.py).

Я привел 2 примера алгоритмов, которые можно использовать для сортировки массивов. Согласно проведенным мною тестам, быстрая сортировка будет более эффективна по скорости, тем не менее, согласно теории, в случае наихудшего варианта она будет менее эффективна, чем сортировка вставками. Но надо отметить, что обе эти сортировки в любом случае проиграют встроенному методу sorted(), который использует Timsort.
