#№3Создать три переменные, содержащие возраст трех ваших друзей, в качестве имен
#переменных использовать имена друзей, найти сумму и вывести ее на экран.
anna = 20;
print("Возраст Анны =", anna);
veronika = 15;
print("Возраст Вероники =", veronika);
katia = 19;
print("Возраст Кати =", katia);
summa = anna + veronika + katia;
print("Сумма всех возрастов моих подруг =", summa);


#№4 Создать еще одну переменную равную среднему арифметическому возрасту, и
# вывести это значение на экран
list = [anna, veronika, katia];
kol = len(list);
srednee_arifmeticheskoe = summa/kol;
print("Среднее арифметическое возроста моих подруг =", srednee_arifmeticheskoe);

# Или можно создать:
# srednee_arifmeticheskoe = anna+veronika+katia/3;
#print("Среднее арифметическое возроста моих подруг =", srednee_arifmeticheskoe);
