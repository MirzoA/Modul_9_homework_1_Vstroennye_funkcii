def mul_by2(x):
    return x ** 2

my_numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

result = map(mul_by2, my_numbers) # Здесь функция МАР используя функцию mul_by2 каждый элемент списка my_numbers возводит на квадрат
a = (list(result))
def is_odd(x):
    return x % 2

result1 = filter(is_odd, a) # Здесь функция FILTER используя функцию is_odd оставляет нечётные квадраты чисел.
print(list(result1))