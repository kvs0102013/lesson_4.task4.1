# a = int(input('Введите первое число: '))# Поменять числа а и б местами
# b = int(input('Введите второе число: '))
# print(a, b)
# a = a + b
# print('a = ', a)
# b = a - b
# print('b = ', b) 
# a = a - b 
# print(a,b) 

number =  1234 #Четырех значное число наоборот
a = number % 10
b = number % 100 // 10
c = number // 100 % 10
d = number // 1000
print(a,b,c,d)
revers_number = a * 1000 + b * 100 + c * 10 + d 
print( 'Число наоборот:' , revers_number )