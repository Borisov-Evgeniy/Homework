import multiprocessing
import random

def generate_list(queue):
    my_list = [random.randint(1, 500) for i in range(10)]
    print(my_list)
    queue.put(my_list)
    print(f'Процесс {multiprocessing.current_process().pid} выполнен')

def calculate_sum(queue):
    my_list = queue.get()
    my_sum = sum(my_list)
    print(my_sum)
    queue.put(my_sum)
    print(f'Процесс {multiprocessing.current_process().pid} выполнен')
def calculate_average(queue):
    my_list = queue.get()
    my_sum = queue.get()
    my_avg = my_sum / len(my_list)
    queue.put(my_avg)
    print(f'Процесс {multiprocessing.current_process().pid} выполнен')

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    pr1 = multiprocessing.Process(target=generate_list, args=(queue,))
    pr2 = multiprocessing.Process(target=calculate_sum, args=(queue,))
    pr3 = multiprocessing.Process(target=calculate_average, args=(queue,))

    pr1.start()
    pr1.join()
    pr2.start()
    pr2.join()
    pr3.start()
    pr3.join()

    print(f'Среднее арифметическое: {queue.get()}')
#----------------------------------------------------------------------------------------------------------------

import multiprocessing as mp
import random
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def find_primes(input_file, output_file):
    with open(input_file, 'r') as file_input:
        numbers = file_input.read().split()
    primes = []
    for num in numbers:
        if is_prime(int(num)):
            primes.append(num)
    with open(output_file, 'w') as file_output:
        file_output.write('\n'.join(primes))

def calc_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def calc_factorials(input_file, output_file):
    with open(input_file, 'r') as file_input:
        numbers = file_input.read().split()
    factorials = []
    for num in numbers:
        factorials.append(str(calc_factorial(int(num))))
    with open(output_file, 'w') as file_output:
        file_output.write('\n'.join(factorials))

def main():
    input_file = input("Введите путь к файлу: ")
    with open(input_file, 'w') as file:
        for i in range(100):
            file.write(str(random.randint(1,100)) + " ")

    primes_file = "primes.txt"
    factorials_file = "factorials.txt"

    p1 = mp.Process(target=find_primes, args=(input_file, primes_file))
    p2 = mp.Process(target=calc_factorials, args=(input_file, factorials_file))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    with open(primes_file, 'r') as p_file:
        primes = p_file.read().split()
    with open(factorials_file, 'r') as f_file:
        factorials = f_file.read().split()

    print("Найденные простые числа: ", primes)
    print("Вычисленные факториалы: ", factorials)
    print("Количество простых чисел: ", len(primes))
    print("Количество вычисленных факториалов: ", len(factorials))

if __name__ == "__main__":
    main()


