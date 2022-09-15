# №1 Написать программу для печати указанного списка после удаления 0-го, 4-го и 5-го элементов
print('Задание №1:')
print('Обычный список:');
list_favorite_colors = ['фуксия', 'лиловый', 'голубой', 'белый', 'серый', 'бордовый', 'коричневый', 'пудровый', 'изумрудный'];
print(list_favorite_colors);

print('Преобразованный список:');
del list_favorite_colors[0]
del list_favorite_colors[3:5]
print(list_favorite_colors)


# №2 Написать программу, чтобы добавить список ко второму списку
print('\n\nЗадание №2:')
first_favorite_color = set(['лимонный', 'жёлтый', 'горчичный']);
print('Первый список :', first_favorite_color )
second_favorite_color = set(['фиолетовый', 'синий']);
print('Второй список', second_favorite_color);
all_favorite_colors = first_favorite_color.union(second_favorite_color);
print('Все любимые цвета (два списка):', all_favorite_colors );

# №3 Написать программу для распаковки словаря по парам и вывести результат
dict_fruit_number_vegetables = {'fruit': 'banana', 1: [4,6,8], 'vegetables': 'tomato'};
print('\n\nЗадание №3:')
print('Словарь: ', dict_fruit_number_vegetables)
raspakovka = dict_fruit_number_vegetables.items();
print('Распакованный словарь по парам(ключ-значение): ', raspakovka)


# №001 Предложить пользователю ввести своё имя и вывести приветственное сообщение на экран
print('Введите Ваше имя:');
name = str(input());
print('Здравствуйте,', name, ', хорошего Вам дня!')
# или можно: print('Hello', name);

# №002 Предложить пользователю ввести свою фамилию, после чего вывести приветственное сообщение
print('\nВведите Вашу фамилию:');
first_name = str(input());
print('Здравствуйте,', name, first_name, ', хорошего Вам дня!');
# или можно: print('Hello', name, first_name);

# №003 Напишите код, который выводит вопрос: «What do you call a bear with no teeth?»,
# а в следующей строке выводит ответ: "A gummy bear!". Попробовать обойтись одной строчкой кода
print('\n\nWhat do you call a bear with no teeth? \n"A gummy bear!"')

# №004 Предложить пользователю ввести два числа. Сложите эти числа и выведите результат
print('\nПожалуйста, введите первое число')
first_numder = int(input());
print(' Пожалуйста, введите второе число');
second_numder = int(input());
summa_numbers = first_numder + second_numder;
print('Сумма чисел =', summa_numbers)

# №005 Предложить пользователю ввести три числа. Сложите первые два числа, затем умножьте сумму на третье число.
print('\nПожалуйста, введите три числа')
first_numder1 = int(input());
second_numder1 = int(input());
third_numder1 = int(input());
arithmetic = (first_numder1 + second_numder1)*third_numder1;
print('Результат =',arithmetic );

# №006 Спросите сколько кусков пиццы было у пользователя и сколько кусков он съел.
# Вычислите, сколько кусков пиццы у него осталось, и выведите результат в форме, удобной для пользователя
print('\nСколько кусков пиццы у Вас было?');
were_pieces_of_pizza = int(input());
print('Сколько кусков пиццы Вы вкушали?');
ate_pieces_of_pizza = int(input());
ostslos = were_pieces_of_pizza - ate_pieces_of_pizza;
print('Итого, у вас осталось',ostslos, 'кусков пиццы!' )


# №007 Предложите пользователю ввести его имя и возраст.Увеличьте возраст на 1 и выведите сообщение...
print('\nВведите, пожалуйста, Ваше имя');
name1 = str(input());
print('Введите, пожалуйста, Ваш возраст');
age = int(input());
future_age = age + 1;
print(name1, 'в следующем году Вам будет', future_age);


# №008 Предложите пользователю ввести общую сумму счёта, а затем запросите общее количество участников обеда
# Разделите сумму счёта на количество участников и выведите сумму, которую должен заплатить каждый участник
print('\nВведите, пожалуйста, общую сумму счёта:');
acount = int(input());
print('Введите, пожалуйста, количество участников обеда:');
kolichestvo = int(input());
summa_everyone = acount / kolichestvo;
print('Каждый участник обеда должен заплатить - ', summa_everyone);

# №009 Напишите программу, которая предполагает ввести промежуток времени в днях, а потом выводит
# количество часов, минут и секунт в этом промежутке
print('\nВведите, пожалуйста, количество суток:');
time = int(input());
kolichestvo_time1 = time * 24 * 60;
print('Количество минут в сутках =', kolichestvo_time1 );
kolichestvo_time2 = time * 24 * 60 * 60;
print('Количество секунд в сутках =',kolichestvo_time2);

# №010 В одном килограмме 2,204 фута. Предложите пользователю ввести вес в килограммах и переведите его в фунты
print('\nВведите, пожалуйста, килограммы:');
kg = int(input());
feet = kg * 2.204;
print('Количество футов =', feet);

# №011  Предложите пользователю ввести число больше 100, а затем число меньше 10.
# Сообщите, сколько раз меньшее число помещается в большем, в удобном формате.
print('\nВведите, пожалуйста, число больше 100:');
chislo_big = int(input());
print('Введите, пожалуйста, число меньше 10:');
chislo_little = int(input());
chislo = chislo_big // chislo_little;
print('Маленькое число помещается в большом', chislo, 'раз(-a)');