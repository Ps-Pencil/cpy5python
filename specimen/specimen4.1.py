x = input ("Please enter a number between 1 and 20: ")
error = True
while error:
    error = False
    if not x.isdigit():
        x = input("It must be an integer! Please enter again: ")
        error = True
    elif not (int(x) >= 1 and int(x) <= 20):
        x = input("It must be between 1 and 20! Please enter again: ")
        error = True

result = ''

x = int(x)
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
print(result)
