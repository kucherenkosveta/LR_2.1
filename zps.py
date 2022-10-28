a2 = int(input('enter a1'))
a1 = int(input('enter a2'))
b1 = int(input('enter b1'))
digit1 = (a1 + b1) % 10
digit2 = a2 + (a1+b1) // 10
print("Digits of addition: ", digit2, digit1)