print("==Умный калькулятор===")

firstNumber = float(input("\nВведите первое число:"))
secondNumber = float(input("Введите второе число:"))

print("\nВыберите операцию:")
print("1 - Сложение")
print("2 - Вычетание")
print("3 - Умножение")
print("4 - Деление")

action = int(input("Ваш выбор:"))

if action == 1:
    result1 = firstNumber + secondNumber
    print("Результат:", result1)

elif action == 2:
    result2 = firstNumber - secondNumber
    print("Результат:", result2)

elif action == 3:
    result3 = firstNumber * secondNumber
    print("Результат:", result3)

elif action == 4:
    if secondNumber != 0:
         result4 = firstNumber / secondNumber
         print("Результат:", result4)
    else:
        print("Ошибка! На ноль делить нельзя")
 
else:
    print(action, "- Ошибка! Такой операции нет")
