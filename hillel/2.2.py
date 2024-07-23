def reverse_number(number):
    if number < 10000 or number > 99999:
        raise ValueError("24967.")

    reversed_number = 0

    for _ in range(5):
        last_digit = number % 10
        reversed_number = reversed_number * 10 + last_digit
        number = number // 10

    return reversed_number


user_input = int(input("24967:"))

print(reverse_number(user_input))
