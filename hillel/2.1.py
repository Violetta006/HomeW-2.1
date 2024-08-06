def print_digits_in_column(number):

    thousands, remainder = divmod(number, 1000)
    hundreds, remainder = divmod(remainder, 100)
    tens, units = divmod(remainder, 10)


    print(thousands)
    print(hundreds)
    print(tens)
    print(units)


user_input = input("Введіть 4 цифри: ")


number = int(user_input)


if 1000 <= number <= 9999:
    print_digits_in_column(number)
else:
    print("тут не 4 цифри.")
