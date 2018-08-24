def collatz(number):
    while number > 1:
        if number % 2 == 0:
            print(number // 2)
            number = number // 2
        elif number % 2 == 1:
            print(3 * number + 1)
            number = 3 * number + 1

print('Provide a number')

try:
    number = int(input())
    collatz(number)
except:
    print('Please provide only an integer')
    

