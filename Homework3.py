#36 Собачий возраст
x = float(input('Введите человеческий возраст: '))
if x>=10.5:
    print('Вашей собаке меньше 2 лет')
elif x<=0:
    print('ОШИБКА!!! Вы ввели отрицательное число!')
else:
    x=x/4
    print ('Вашей собаке больше 2 лет')
    print('Точный возраст вашей собаки =', x)




#39 Сколько дней в месяце
month = str(input('\nВведите название месяц (на русском языке): '))
if month == 'январь' or month=='март' or month=='май' or month=='июля' or month=='август' or month=='октябрь' or month=='декабрь':
    print('В данном месяце 31 день')
elif month=='февраль':
    print('В данном месяце может быть как 28, так и 29 дней (это зависит от високосный ли год или нет')
else:
    print('В данном месяце 30 день')



#42 Узнать частоту по ноте
nota = str(input('\nВведите название ноты (на английском языке): '))
octava = int(input('Введите номер октавы: '))
if nota=='C' and octava<=8:
    chastota = 261.63;
    chastota = chastota / 2 ** (4 - octava);
    print('Частота = ', chastota )
elif nota=='D' and octava<=8:
    chastota = 293.66;
    chastota = chastota / 2 ** (4 - octava);
    print('Частота = ',chastota )
elif nota=='E'and octava<=8:
    chastota = 329.63;
    chastota = chastota / 2 ** (4 - octava);
    print('Частота = ', chastota)
elif nota=='F'and octava<=8:
    chastota = 349.23;
    chastota = chastota / 2 ** (4 - octava);
    print('Частота = ', chastota)
elif nota=='G'and octava<=8:
    chastota = 392.00;
    chastota = chastota / 2 ** (4 - octava);
    print('Частота = ', chastota)
elif nota=='A'and octava<=8:
    chastota = 440.00;
    chastota = chastota / 2 ** (4 - octava);
    print('Частота = ', chastota)
elif nota=='B'and octava<=8:
    chastota = 493.88;
    chastota = chastota / 2 ** (4 - octava);
    print('Частота = ', chastota)
else:
    print('Вы ввели неверное значение!')



#43 Узнать ноту по частоте
#chastota1 = str(input('\nВведите часототу звука: '))




#49 Китайский гороскоп
year = int(input('\nВведите год рождения: '))
if year%12==0:
    print('По китайскому гороскопу этот год - год Обезьяны')
elif year % 12 == 1:
    print('По китайскому гороскопу этот год - год Петуха')
elif year % 12 == 2:
    print('По китайскому гороскопу этот год - год Собаки')
elif year % 12 == 3:
    print('По китайскому гороскопу этот год - год свиньи')
elif year % 12 == 4:
    print('По китайскому гороскопу этот год - год Крысы')
elif year % 12 == 5:
    print('По китайскому гороскопу этот год - год Быка')
elif year % 12 == 6:
    print('По китайскому гороскопу этот год - год Тигра')
elif year % 12 == 7:
    print('По китайскому гороскопу этот год - год Кролика')
elif year % 12 == 8:
    print('По китайскому гороскопу этот год - год Дракона')
elif year % 12 == 9:
    print('По китайскому гороскопу этот год - год Змеи')
elif year % 12 == 10:
    print('По китайскому гороскопу этот год - год Лошади')
elif year % 12 == 11:
    print('По китайскому гороскопу этот год - год Козы')



#52 Бувенные оценки - в числовые
mark = str(input('\nВведите буквенную оценку: '))
if mark=='A+' or mark=='A':
    print('Числовая оценка = 4,0')
elif mark=='A-':
    print('Числовая оценка = 3,7')
elif mark=='B+' :
    print('Числовая оценка = 3,3')
elif  mark=='B':
    print('Числовая оценка = 3,0')
elif mark == 'B-':
    print('Числовая оценка = 2,7')
elif mark == 'C+':
    print('Числовая оценка = 2,3')
elif mark == 'C':
    print('Числовая оценка = 2,0')
elif mark == 'C-':
    print('Числовая оценка = 1,7')
elif mark == 'D+':
    print('Числовая оценка = 1,3')
elif mark == 'D':
    print('Числовая оценка = 1,0')
elif mark == 'F':
    print('Числовая оценка = 0')
else:
    print('Вы ввели неверное значение!')
