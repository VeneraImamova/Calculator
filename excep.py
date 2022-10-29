import user_interface

def check_type_number(value):
    if value.isdigit() and int(value) < 3 and int(value) >= 0:
        return int(value)
    else:
        return print("Ошибка, введено неверное значение. Попробуйте еще раз ;)")

def check_number(value):
    if value.isdigit():
        return float(value)
    else:
        return print("Ошибка, введено неверное значение. Попробуйте еще раз ;)")


def check_operation_real(value):
    if value.isdigit() and int(value) < 7 and int(value) >= 0:
        return int(value)
    else:
        return print("Ошибка, введено неверное значение. Попробуйте еще раз ;)")

def check_div_operation (value):
    if value.isdigit() and int(value) < 4 and int(value) >= 0:
        return int(value)
    else:
        return print("Ошибка, введено неверное значение. Попробуйте еще раз ;)")



def check_operation_complex(value):
    if value.isdigit() and int(value) < 5 and int(value) >= 0:
        return int(value)
    else:
        return print("Ошибка, введено неверное значение. Попробуйте еще раз ;)")
