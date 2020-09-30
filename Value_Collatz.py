def collatz(number):
    while number != 1:
        print(number)
        if number % 2 == 0:
            number = number // 2
        elif number % 2 == 1:
            number = 3 * number + 1
    else:
        number = 1
        print(number)


print("insert value")
collatz(int(input()))
#aaa