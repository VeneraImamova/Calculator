import excep as ex
from compl import compl


print("Добро пожаловать в калькулятор")

def get_type_number():
    print(
        "С чем Вам предстоит работать?\n \
        1 - рациональные числа \n \
        2 - комплекные числа \n \
        0 - Выход"
        )
    return ex.check_type_number(input("Введите Ваш выбор: "))

def get_number_real():
    num1 = ex.check_number(input("Введите первое вещественное число: "))
    num2 = ex.check_number(input("Введите второе вещественное число: "))
    return (num1, num2)

def get_number_complex():
    num1_a = ex.check_number(input("Введите для первого числа действительную часть: "))
    num1_b = ex.check_number(input("Введите для первого числа мнимую часть: "))
    num1 = compl(num1_a,num1_b)
    num2_a = ex.check_number(input("Введите для второго числа действительную часть: "))
    num2_b = ex.check_number(input("Введите для второго числа мнимую часть: "))
    num2 = compl(num2_a,num2_b)
    return (num1, num2)


def get_operation_real():
    print(
        "Какую операцию Вы хотите выполнить?\n \
        1 - Сложение\n \
        2 - Вычитание\n \
        3 - Умножение\n \
        4 - Деление\n \
        5 - Возведение в степень\n \
        6 - Извлечение корня\n \
        0 - Возврат к предыдущему меню"
        )
    return ex.check_operation_real(input("Введите Ваш выбор: "))

def get_operation_complex():
    print(
        "Какую операцию Вы хотите выполнить?\n \
        1 - Сложение\n \
        2 - Вычитание\n \
        3 - Умножение\n \
        4 - Деление\n \
        0 - Возврат к предыдущему меню"
        )
    return ex.check_operation_complex(input("Введите Ваш выбор: "))

def get_div_operation_type():
    print(
        "Какую операцию Вы хотите выполнить?\n \
        1 - Простое деление\n \
        2 - Целочисленное деление\n \
        3 - Остаток от деления\n \
        0 - Возврат в предыдущее меню"
        )
    return ex.check_div_operation(input("Введите Ваш выбор: "))

def print_result(result):
   return print(f"Результат выполнения операции: {result}")



