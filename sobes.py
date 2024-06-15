# 19)Создайте лямбда-функцию, которая принимает на вход строку и возвращает ее длину.
# 5) Дается 2 строки "Aidana" и "Adilet" . Вам нужно в результате получить смешанную строку из двух имен, буква за буквой. Результат: "AAiddialneat” 
# 1)Написать функцию, которая выводит на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.

# text = input('Введите текст: ')
# resulttext = (lambda i: len(i), text) 
# print(resulttext)

firstname = 'Aidana'
secondname = 'Adilet'
result = (firstname[0], secondname[0], firstname[1], secondname[1], firstname[2], secondname[2], firstname[3], secondname[3],firstname[4], secondname[4], firstname[5], secondname[5])
print(result)

i = 0
for i in range(6):
    print(i, 0)