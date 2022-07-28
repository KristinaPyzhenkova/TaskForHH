# Задание №1
# вариант 1
def even_number(n):
    if (n < 2):
        return (n== 0)
    return (even_number(n - 2))
number = int(input("Введите число:"))


# вариант 2
def isEven(value):return str(value)[-1] in ['0','2','4','6','8']

# Вариант 1 решение через рекурсию: явный минус - скорость работы рекурсивного кода,
# а также нельзя проверить большое число из-за максимальной глубины рекурсии.
# Данный способ в текущей задаче не является эффективным решением.
# Вариант 2: схож с реализации из примера по объему памяти и скорости выполнения,
# отличается типами данных при получении ответа

# Задание 2
# Вариант 1
class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0 
    
    def is_empty(self):
        return self.size == 0
  
    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')
    
    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x 

def main():
    m=int(input())
    n=int(input())
    stack = MyQueueSized(n)
    q={'push':1,'pop':2,'peek':3,'size':4}
    for i in range(m):
        a=input().split()
        if q.get(a[0])==1:
            stack.push(int(a[1]))
        elif q.get(a[0])==2:
            if stack.size==0:
                print(None)
            else:
                print(stack.pop())
        elif q.get(a[0])==3:
            if stack.size==0:
                print(None)
            else:
                print(stack.queue[stack.head])
        elif q.get(a[0])==4:
            print(stack.size)

if __name__ == '__main__':
    main()
# Данный алгоритм принимает в m - кол-во команд, n - максимально допустимый размер очереди
# Имеет 4 команды - push x - добавить число x в очередь, pop - удалить число из очереди и вывести на печать,
# peek - напечатать первое число в очереди, size - вернуть размер очереди
# Плюсы: Из-за того, что не нужно снова выделять память, каждая операция выполняется за O(1)
# Минусы: Ограничение на максимальный размер. При переполнении очереди можно расширить массив - но это усложнит реализацию.

# Вариант 2
class OverflowDeque(Exception):
    pass


class EmptyDeque(Exception):
    pass


class Deque:
    def __init__(self, n):
        self.__queue = [None] * n
        self.__max_n = n
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def __next_atr(self, atr, opr):
        if opr == '+':
            return atr + 1
        else:
            return atr - 1

    def __is_empty(self):
        return self.__size == 0

    def __modul_atr(self, atr):
        return atr % self.__max_n

    def push_back(self, x):
        if self.__size == self.__max_n:
            raise OverflowDeque
        self.__queue[self.__tail] = x
        self.__tail = self.__modul_atr(self.__next_atr(self.__tail, '+'))
        self.__size += 1

    def push_front(self, x):
        if self.__size == self.__max_n:
            raise OverflowDeque
        self.__queue[self.__next_atr(self.__head, '-')] = x
        self.__head = self.__modul_atr(self.__next_atr(self.__head, '-'))
        self.__size += 1

    def pop_front(self):
        if self.__is_empty():
            raise EmptyDeque
        x = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = self.__modul_atr(self.__next_atr(self.__head, '+'))
        self.__size -= 1
        return x

    def pop_back(self):
        if self.__is_empty():
            raise EmptyDeque
        x = self.__queue[self.__next_atr(self.__tail, '-')]
        self.__queue[self.__next_atr(self.__tail, '-')] = None
        self.__tail = self.__modul_atr(self.__next_atr(self.__tail, '-'))
        self.__size -= 1
        return x


def main():
    count_command = int(input())
    size_deque = int(input())
    deque = Deque(size_deque)
    for _ in range(count_command):
        list_command = input().split()
        try:
            (
                getattr(deque, list_command[0])(int(list_command[1]))
                if len(list_command) == 2
                else print(getattr(deque, list_command[0])())
            )
        except(EmptyDeque, OverflowDeque):
            print('error')


if __name__ == '__main__':
    main()
# Данный алгоритм принимает в count_command - кол-во команд, size_deque - максимально допустимый размер очереди
# Имеет 4 команды - push_back(value) – добавить элемент в конец дека. Если в деке уже находится максимальное число элементов, вывести «error».
# push_front(value) – добавить элемент в начало дека. Если в деке уже находится максимальное число элементов, вывести «error».
# pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
# pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
# Плюсы: также как в алгоритме выше, но есть доработка: двухстороннюю очередь - позволяет и добавлять, и извлекать элементы с обоих концов.


# Задание 3
def partition(arr, left, right):
    pivot = arr[(left + right) // 2]
    start = left - 1
    end = right + 1
    while True:
        start += 1
        while pivot > arr[start]:
            start += 1
        end -= 1
        while arr[end] > pivot:
            end -= 1
        if start >= end:
            return end
        arr[start], arr[end] = arr[end], arr[start]


def quicksort(arrs, left, right):
    if left < right:
        center = partition(arrs, left, right)
        quicksort(arrs, left, center)
        quicksort(arrs, center + 1, right)
        return arr

# пример запуска
arr = [1,10,2,4,23,31,3]
print(quicksort(arr, 0, len(arr) - 1))

# разделение данных на части меньшего размера
# рекурсивный вызов алгоритма для этих частей
# каждый шаг рекурсии всегда будет уменьшать размер обрабатываемой части.
# объединение результатов

