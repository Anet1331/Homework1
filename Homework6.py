# 118 Определите подрограмму, которая предлагает пользователю ввести число и сохранить его в
# переменной null.Определите другую подпрограмму, которая использует значение null
# и проводит отсчёт от 1 до этого числа
def saveee_func():  # Создаю функцию, которая запрашивает у пользователя число
    n = int(input('Введите число: '))  # вмесето null использую переменную n
    return n


useee = saveee_func()  # переменной присваию данную  функцию
for useee in range(1, useee + 1):  # ставлю цикл для подсчёта от 1 до введённого числа
    print(useee)  # вывожу числа в этом цикле (от 1 до числа)


# ОНА НЕ РАБОТАЕТ ТАК КАК НУЖНО, Я НЕ ЗНАЮ.....
# 119 Определите подпрограмму, которая предлагает пользователю выбрать большое и маленькое число,
# а затем генерирует случайное число из диапазона и сохраняет его в переменной с именем comp_num.
# Определите другую подпрограмму, которая выводит сообщение "I am thinking of a number...",
# после чего предлагает пользователю угадать загаданное число.
# Определите третью подпрограмму, которая проверяет совпадает ли comp_num с предложением пользователя.
# Если совпадает,  то подпрограмма выводит сообщение "Correct, you win", в противном случаи цикл продолжается,
# а подпрограмма сообщает, больше или меньше их предложение загаданного числа, и предлагает сделать новую попытку
# до тех пор, пока пользователь не отгадает число.
def number_func():
    a = int(input('\nВведите маленькое число: '))
    b = int(input('Введите большое число: '))
    for i in range(a, b):
        comp_num = i
    return comp_num


comp_num = number_func()
print(comp_num)


def vivod_func():
    vivodd = int(input('I am thinking of a number...'))
    return vivodd

vivodd = vivod_func()

def proverka_func():
    #vivodd = vivod_func()
    while vivodd != comp_num:
        if vivodd > comp_num:
            print('Ваше число больше загаданного, повторите попытку')
            efford_1 = vivod_func()
        elif vivodd < comp_num:
            print('Ваше число меньше загаданного повторите попытк')
            efford_2 = vivod_func()
        else:
            print('Correct, you win')
    return vivodd


itog = proverka_func()
print(itog)