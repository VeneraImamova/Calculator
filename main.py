import user_interface as us
import choice as ch
import xml_create as xml


number_type, num1, num2 = ch.get_numbers(us.get_type_number())
if number_type == 'real_number':
    operation, result = ch.get_result_real(us.get_operation_real(), num1, num2)
elif number_type == 'complex_number':
    operation, result = ch.get_result_complex(us.get_operation_complex(), num1, num2)
else:
    error = 'Ошибка данных при выполнении операции'
    print("Произошла ошибка, попробуйте воспользоваться программой еще раз")
    quit(error)

xml.write_ex(operation, num1, num2, result)

us.print_result(result)


