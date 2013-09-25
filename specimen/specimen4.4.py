def convert(x):
    result = ''
    if x == 40:
        return 'XL'
    while x >= 10:
        result += 'X'
        x -= 10
    if x == 9:
        result += 'IX'
    elif x >= 5:
        result += 'V' + (x - 5) * 'I'
    elif x == 4:
        result += 'IV'
    else:
        result += x * 'I'
    return result

A = input("Please enter the first Roman numeral: ")
B = input("Please enter the second Roman numeral: ")

Sum = 0

for i in range(1,21):
    if convert(i) == A:
        Sum += i
    if convert(i) == B:
        Sum += i
print(convert(Sum))
