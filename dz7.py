number1 = int(input("введите первое число"))
number2 = int(input("введите второе число"))
numbers = []
for i in range(number1, number2 + 1):
    if i % 7 == 0:
        numbers.append(i)

print("вот все числа которые делятся в этом деапозоне")
print(*numbers) 
