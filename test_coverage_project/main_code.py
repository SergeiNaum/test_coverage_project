"""
Discription:
           Проект для помощи в выполнении задания покрытие кода тестами
           по профессии Python - разработчик образовательной платформы Hexlet.io.
           Проект содержит 3 модуля:
                                   1) common_conditions - помещены тестовые данные и "условия"
                                   2) common_functions - помещены правильные и не правильные реализации функций
                                                                (right и wrong_N)
                                   3) main - производится запуск всех функций со всеми тестовыми данными

С помощью данного проекта манипулируя наполнением тестовыми случаями можно вывести для визуального анализа результаты
работы правильной и не правильных реализаций функций для дальнейшего написания тестов при которых функция с right
реализацией должна проходить проверку, а остальные функции нет.
"""

import test_coverage_project.common_functions as cf
import test_coverage_project.common_conditions as cc


# Списки вызываемых функций по категориям из модуля common_functions
# для формирования итогового списка func_list
get_func_list = [cf.right_get, cf.get_w1, cf.get_w2, cf.get_w3]
index_of_list = [cf.index_of_right, cf.index_of_w1, cf.index_of_w2, cf.index_of_w3]
slice_list = [cf.my_slice_right, cf.my_slice_w1, cf.my_slice_w2, cf.my_slice_w3]


# Итоговый список всех функций из модуля common_functions
func_list = [get_func_list, index_of_list, slice_list]


# Список тестовых случаев по категориям из модуля common_conditions
test_data_list = [cc.test_data_get, cc.test_data_test_index, cc.test_data_test_slice]


# Список условий по категориям из модуля common_conditions
conditions_list = [cc.conditions_get, cc.conditions_index, cc.conditions_slice]


# Функция вызывающая другие функции из списка func_list с
# аргументами из списка test_data_list для сравнения ожидаемого
# вывода с фактическим


def apply_func_in_loop(func, args_list, conditions):
    """accepts as input functions to be called from func_list"""
    for i, args in enumerate(args_list):
        _, expected_val = conditions[i].split("==")
        result = func(*args)
        print(f"Вызов функции {func.__name__} по условию: {conditions[i]}: результат = {result}")


# Вызываем в цикле функцию  apply_func_in_loop с тестовыми данными и условиями
#  для получения результата
def run(func_list):
    for i, func_list in enumerate(func_list):
        for func in func_list:
            apply_func_in_loop(func, test_data_list[i], conditions_list[i])
