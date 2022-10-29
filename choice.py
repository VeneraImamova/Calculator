import user_interface as us
import model_sum
import model_mult
import model_sub
import model_div
import model_degree
import model_pow



def get_numbers(choice):
    if choice == 1:
        number_type = 'real_number'
        num1, num2 = us.get_number_real()
        return (number_type, num1, num2)
    elif choice == 2:
        number_type = 'complex_number'
        num1, num2 = us.get_number_complex()
        return (number_type, num1, num2)
    elif choice == 0:
        quit(print("Спасибо за использование программы!=)"))
    else:
        error = 'Ошибка данных при пределении типа числа'
        print("Произошла ошибка, попробуйте воспользоваться программой еще раз")
        quit(error)





def get_result_real(choice, num1, num2):
    if choice == 1:
        operation = 'sum'
        result = model_sum.sum(num1,num2)
        return (operation, result)
    elif choice == 2:
        operation = 'sub'
        result = model_sub.sub(num1, num2)
        return (operation, result)
    elif choice == 3:
        operation = 'mult'
        result = model_mult.mult(num1, num2)
        return (operation, result)
    elif choice == 4:
            div_choice = us.get_div_operation_type()
            if div_choice == 1:
                operation = 'div'
                result = model_div.div(num1, num2)
                return (operation, result)
            elif div_choice == 2:
                operation = 'div_integer'
                result = model_div.div_integer(num1, num2)
                return (operation, result)
            elif div_choice == 3:
                operation = 'div_integer'
                result = model_div.div_modulo(num1, num2)
                return (operation, result)
            elif div_choice == 0:
                return get_result_real(us.get_operation_type(), num1, num2)
            else:
                error = 'Ошибка данных при вычислении деления'
                print("Произошла ошибка, попробуйте воспользоваться программой еще раз")
                quit(error)
    elif choice == 5:
        operation = 'degree'
        result = model_degree.degree(num1, num2)
        return (operation, result)
    elif choice == 6:
        operation = 'pow'
        result = model_pow.pow(num1, num2)
        return (operation, result)
    elif choice == 0:
        return get_numbers(us.get_type_number())
    else:
        error = 'Ошибка данных при выполнении операции'
        print("Произошла ошибка, попробуйте воспользоваться программой еще раз")
        quit(error)


def get_result_complex(choice, num1, num2):
    if choice == 1:
        operation = 'sum'
        result = model_sum.sum(num1,num2)
        return (operation, result)
    elif choice == 2:
        operation = 'sub'
        result = model_sub.sub(num1, num2)
        return (operation, result)
    elif choice == 3:
        operation = 'mult'
        result = model_mult.mult(num1, num2)
        return (operation, result)
    elif choice == 4:
        operation = 'div'
        result = model_div.div(num1, num2)
        return (operation, result)
    elif choice == 0:
        return get_numbers(us.get_type_number())
    else:
        error = 'Ошибка данных при выполнении операции'
        print("Произошла ошибка, попробуйте воспользоваться программой еще раз")
        quit(error)


